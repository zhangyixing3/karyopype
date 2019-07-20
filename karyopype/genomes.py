import os
from pathlib import Path

import pandas as pd


def filter_cannonical(df):
    """Retains only cannonical chromosomes in first column."""
    df = df[df.loc[:,0].str.match("chr[0-9|X|Y]+[a|b]?$")]
    return df

def get_chromsizes(species, chromsizes=None, cannonical=True):
    """Get chromsizes file for species."""
    # extract species name from available files
    csizes = Path("data/chromsizes") 
    snames = [sp.split(".")[0] for sp in os.listdir(csizes)]
    if chromsizes is not None:
        csdf = pd.read_csv(chromsizes, sep='\t', header=None)
        # filter cannonical by default for now
        csdf = filter_cannonical(csdf)
        csdict = pd.Series(csdf[1].values, index=csdf[0]).to_dict() 
    elif species not in snames:
        raise Exception("Species not yet supported, please provide a chromsizes file.")
    else: 
        csfile = csizes / f"{species}.chrom.sizes"
        csdf = pd.read_csv(csfile, sep='\t', header=None)
        csdf = filter_cannonical(csdf)
        csdict = pd.Series(csdf[1].values, index=csdf[0]).to_dict() 
    
    return(csdict)