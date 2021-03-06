# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Honeybee Window Surface

-

    Args:
        _geo: A list of input geometry.
        names_: A name or a list of names for input geometry. If the name is not
            provided Honeybee will assign a random name to the surface.
        radMat_: A Radiance material. If radiance matrial is not provided the
            component will use the type to assign the default material 
            (%60 transmittance)for the surface.
        epProp_: EnergyPlus properties.
    Returns:
        report: Reports, errors, warnings, etc.
        HBWinSrf: Honeybee window surface. Use this surface directly for daylight
            simulation or add it to a honeybee surface or a honeybee zone for
            energy simulation.
"""

ghenv.Component.Name = "HoneybeePlus_Honeybee Window Surface"
ghenv.Component.NickName = 'HBWinSrf'
ghenv.Component.Message = 'VER 0.0.03\nAUG_04_2017'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '00 :: Create'
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from honeybee.hbfensurface import HBFenSurface
    from honeybee.radiance.properties import RadianceProperties
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))

if len(_geo)!=0 and _geo[0]!=None:
    isNameSetByUser = False
    if names_:
        isNameSetByUser = True

    if radMat_:
        assert radMat_.isGlassMaterial, \
            TypeError('Radiance material must be a Window material not {}.'.format(type(m)))
        radProp_ = RadianceProperties(radMat_, True)
    else:
        radProp_ = RadianceProperties()

    epProp_ = None
    HBWinSrf = HBFenSurface.fromGeometry(names_, _geo, isNameSetByUser, radProp_, epProp_)