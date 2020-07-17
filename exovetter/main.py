"""
A sketch of an architecture. For discussion

Each vetting test is wrapped in a class that follows this
structure.
"""

import argparse
import typing

T = typing.TypeVar('T')

class ExovetterConfig(typing.NamedTuple):
    input_path: str
    verbose: str

class Vetter():
    def __init__(self, **kwargs) -> None:
        """kwargs stores the configuration parameters common to all TCEs
        For example, for the Odd-even test, it might specify the signficance
        of the depth difference that causes a TCE to fail
        """
        pass

    def apply(self, tce: 'tce', light_curve: 'light_curve') -> typing.Any:
        """Actually run the test. Returns a dictionary of metric values"""
        pass

    def plot(self: T, tce: 'tce', light_curve: 'light_curve') -> typing.Any:
        """Optional, generate a diagnostic plot"""
        pass


class Lpp(Vetter):
    """
    The LPP vetter is an example of a Vetter class.
    """

    def apply(self: T, tce: 'tce', light_curve: 'light_curve') -> typing.Any:
        """
        Actual implementation of LPP is called here
        """
        pass

class OddEven(Vetter):
    """
    The odd even test. We can have many such tests
    """
    pass


def capture_options() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='exovetter utility')
    parser.add_argument('-v', '--verbose', help='Log details verbosely', default=False, action='store_true', type=bool)
    parser.add_argument('-i', '--input', help='Input Path?', default=None, type=str)
    return parser.parse_args()

def build_config(options: argparse.Namespace) -> ExovetterConfig:
    return ExovetterConfig(options.input, options.verbose)

def main() -> None:
    options = capture_options()
    config = build_config(options)

    tceTable = pd.read_csv('tcelist.csv')
    sectorList = np.arange(25)

    #Initialise vetters. The list of vetters can be hardcoded, or
    #maybe loaded from a file.
    vetterList = []
    for v in [Lpp, OddEven]:
        vetterList.append( v(**config) )

    output = []
    for i, tce in tceTable.iterrows():
        #Load lightcurve data, possibly using lightKurve package
        lightcurve = loadLightCurve(tce.ticId, sectorList)

        metrics = dict()
        for v in vetterList:
            resDict = v.apply(tce, lightcurve)
            metrics.update(resDict)

        #metrics is a dictionary of all metrics for a single TCE from all tests
        #output is a list of such dictionaries.
        output.append(metrics)

    df = makeDataFrameFromListOfDicts(output)
    return df
