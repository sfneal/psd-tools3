from __future__ import absolute_import, unicode_literals

import io
import os

import pytest

from psd_tools.psd import PSD
from ..utils import all_files, check_write_read

try:
    from IPython.lib.pretty import pprint
except ImportError:
    from pprint import pprint

# It seems some fixtures made outside of Photoshop has different paddings.
BAD_PADDINGS = {
    '1layer.psd': 1,
    '2layers.psd': 2,
    'broken-groups.psd': 2,
    'transparentbg-gimp.psd': 2,
}

BAD_UNICODE_PADDINGS = {
    'broken-groups.psd': 2,    # Unicode aligns 2 byte.
    'unicode_pathname.psd': 2,    # DescriptorBlock aligns 2 byte.
    'unicode_pathname.psb': 2,    # DescriptorBlock aligns 2 byte.
}


# @pytest.mark.parametrize('filename', [full_name('layer_effects.psd')])
@pytest.mark.parametrize('filename', all_files())
def test_psd_read_write(filename):
    basename = os.path.basename(filename)
    with open(filename, 'rb') as f:
        expected = f.read()

    with io.BytesIO(expected) as f:
        psd = PSD.read(f)
        # pprint(psd)

    padding = BAD_PADDINGS.get(basename, 4)
    with io.BytesIO() as f:
        psd.write(f, padding=padding)
        f.flush()
        output = f.getvalue()

    if basename in BAD_UNICODE_PADDINGS:
        pytest.xfail('Broken file')
    assert len(output) == len(expected)
    assert output == expected


@pytest.mark.parametrize('filename', all_files())
def test_psd_write_read(filename):
    with open(filename, 'rb') as f:
        psd = PSD.read(f)
    check_write_read(psd)
    check_write_read(psd, encoding='utf_8')


def test_psd_from_error():
    with pytest.raises(AssertionError):
        PSD.frombytes(b'\x00\x00\x00\x00')
