
import glob
import os
ELM_EXAMPLE_DATA_PATH = os.environ.get('ELM_EXAMPLE_DATA_PATH')
if ELM_EXAMPLE_DATA_PATH:
    ELM_HAS_EXAMPLES = True
    ELM_EXAMPLE_DATA_PATH = os.path.expanduser(ELM_EXAMPLE_DATA_PATH)
    args = ('landsat-pds',
            'L8',
            '015',
            '033',
            '*',
            '*.TIF',)
    TIF_FILES = glob.glob(os.path.join(ELM_EXAMPLE_DATA_PATH, *args))
    if not TIF_FILES:
        # handling system for saving example GeoTiffs
        # ("landsat-pds" was not part of local file name)
        TIF_FILES = glob.glob(os.path.join(ELM_EXAMPLE_DATA_PATH, *(('tif',)  + args[1:])))
    HDF5_FILES = glob.glob(os.path.join(ELM_EXAMPLE_DATA_PATH,
                                        'hdf5',
                                        '2016',
                                        '01',
                                        '01',
                                        'imerg',
                                        '*.HDF5'))
    HDF4_FILES = glob.glob(os.path.join(ELM_EXAMPLE_DATA_PATH,
                                        'hdf4',
                                        '*.hdf'))
    NETCDF_FILES = glob.glob(os.path.join(ELM_EXAMPLE_DATA_PATH,
                                          'netcdf',
                                          '*.nc'))
else:
    ELM_HAS_EXAMPLES = False
    ELM_EXAMPLE_DATA_PATH = None
    TIF_FILES = []
    HDF5_FILES = []
    HDF4_FILES = []
    NETCDF_FILES = []

def assertions_on_metadata(meta):
    required_keys = ('meta', 'band_meta')
    for key in required_keys:
        assert key in meta

def assertions_on_band_metadata(band_meta):
    required_keys = ('sub_dataset_name', )
    for key in required_keys:
        assert key in band_meta

