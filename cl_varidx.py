# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Climate information dashboard.
# 
# Class definition: RCP and RCPs.
#
# Contributors:
# 1. rousseau.yannick@ouranos.ca
# (C) 2021-2022 Ouranos Inc., Canada
# ----------------------------------------------------------------------------------------------------------------------

# External libraries.
import glob
import os
from typing import List, Union, Optional

# Dashboard libraries.
import cl_gd
import cl_object
from cl_constant import const as c
from cl_context import cntx


def code_props(
) -> dict:

    """
    --------------------------------------------------------------------------------------------------------------------
    Get a dictionary of codes and properties.

    Returns
    -------
    dict
        Dictionary of codes and properties.
        Cell 1: Long description
        Cell 2: Short description (for y-label).
        Cell 3: Units.
        Cell 4: Precision (number of decimal places to show).
    --------------------------------------------------------------------------------------------------------------------
    """

    return {

        # Variables (CORDEX):
        c.V_TAS:                    ["Température moyenne",              "Température",           "°C",    1],
        c.V_TASMIN:                 ["Température minimale journalière", "Température",           "°C",    1],
        c.V_TASMAX:                 ["Température maximale journalière", "Température",           "°C",    1],
        c.V_UAS:                    ["Vitesse du vent (dir. est)",       "Vitesse",               "km/h",  0],
        c.V_VAS:                    ["Vitesse du vent (dir. nord)",      "Vitesse",               "km/h",  0],
        c.V_SFCWINDMAX:             ["Vitesse du vent",                  "Vitesse",               "km/h",  0],
        c.V_PS:                     ["Pression barométrique",            "Pression barométrique", "Pa",    0],
        c.V_RSDS:                   ["Radiation solaire",                "Radiation solaire",     "Pa",    0],
        c.V_PR:                     ["Cumul de précipitation",           "Cumul",                 "mm",    0],
        c.V_EVSPSBL:                ["Évapotranspiration",               "Cumul",                 "mm",    0],
        c.V_EVSPSBLPOT:             ["Évapotranspiration potentielle",   "Cumul",                 "mm",    0],
        c.V_HUSS:                   ["Humidité spécifique",              "Humidité spécifique",   "",      2],
        c.V_CLT:                    ["Couvert nuageux",                  "Couvert nuageux",       "%",     1],
        c.V_SNW:                    ["Neige au sol",                     "Hauteur (en eau)",      "mm",    0],

        # Variables (ECMWF: ERA5 and ERA5-Land):
        c.V_ECMWF_D2M:              ["Point de rosée",                   "Point de rosée",        "",      1],
        c.V_ECMWF_T2M:              ["Température moyenne",              "Température",           "°C",    1],
        c.V_ECMWF_T2MMIN:           ["Température minimale journalière", "Température",           "°C",    1],
        c.V_ECMWF_T2MMAX:           ["Température maximale journalière", "Température",           "°C",    1],
        c.V_ECMWF_SP:               ["Pression barométrique",            "Pression barométrique", "Pa",    0],
        c.V_ECMWF_TP:               ["Précipitation",                    "Cumul",                 "mm",    0],
        c.V_ECMWF_U10:              ["Vitesse du vent (dir. est)",       "Vitesse",               "km/h",  0],
        c.V_ECMWF_U10MIN:           ["Vitesse du vent min. (dir. est)",  "Vitesse",               "km/h",  0],
        c.V_ECMWF_U10MAX:           ["Vitesse du vent max. (dir. est)",  "Vitesse",               "km/h",  0],
        c.V_ECMWF_V10:              ["Vitesse du vent (dir. nord)",      "Vitesse",               "km/h",  0],
        c.V_ECMWF_V10MIN:           ["Vitesse du vent min. (dir. nord)", "Vitesse",               "km/h",  0],
        c.V_ECMWF_V10MAX:           ["Vitesse du vent max. (dir. nord)", "Vitesse",               "km/h",  0],
        c.V_ECMWF_UV10:             ["Vitesse du vent",                  "Vitesse",               "km/h",  0],
        c.V_ECMWF_UV10MIN:          ["Vitesse du vent min.",             "Vitesse",               "km/h",  0],
        c.V_ECMWF_UV10MAX:          ["Vitesse du vent max.",             "Vitesse",               "km/h",  0],
        c.V_ECMWF_SSRD:             ["Radiation solaire",                "Radiation solaire",     "Pa",    0],
        c.V_ECMWF_E:                ["Évaporation",                      "Cumul",                 "mm",    0],
        c.V_ECMWF_PEV:              ["Évapotranspiration potentielle",   "Cumul",                 "mm",    0],
        c.V_ECMWF_SH:               ["Humidité spécifique",              "Humidité spécifique",   "",      2],
        c.V_ECMWF_SNW:              ["Neige au sol",                     "Hauteur (en eau)",      "mm",    0],

        # Variables (ENACTS):
        c.V_ENACTS_TMIN:            ["Température minimale journalière", "Température",           "°C",    1],
        c.V_ENACTS_TMAX:            ["Température maximale journalière", "Température",           "°C",    1],
        c.V_ENACTS_RR:              ["Précipitation",                    "Cumul",                 "mm",    0],
        c.V_ENACTS_PET:             ["Évapotranspiration potentielle",   "Cumul",                 "mm",    0],

        # Variables (CHIRPS):
        c.V_CHIRPS_PRECIP:          ["Précipitation",                    "Cumul",                 "mm",    0],

        # Indices:
        c.I_ETR:                    ["Ecart extrême de température",     "Température",           "°C",    1],
        c.I_TX90P:                  ["Nombre de jours chauds (Tmax > 90e)", "Nbr. jours", "jours", 0],
        c.I_HEAT_WAVE_MAX_LENGTH:   ["Durée maximale des vagues de chaleur (Tmax ≥ {1}; Tmin ≥ {2}; " +
                                     "{3} jours consécutifs)", "Durée", "jours", 0],
        c.I_HEAT_WAVE_TOTAL_LENGTH: ["Durée totale des vagues de chaleur (Tmax ≥ {1}; Tmin ≥ {2}; " +
                                     "{3} jours consécutifs)", "Durée", "jours", 0],
        c.I_HOT_SPELL_FREQUENCY:    ["Nombre de périodes chaudes (Tmax ≥ {1}; {2} jours consécutifs)",
                                     "Nbr. périodes", "périodes", 0],
        c.I_HOT_SPELL_MAX_LENGTH:   ["Durée maximale des périodes chaudes (Tmax ≥ {1}; {2} jours consécutifs)",
                                     "Durée", "jours", 0],
        c.I_HOT_SPELL_TOTAL_LENGTH: ["Durée totale des périodes chaudes (Tmax ≥ {1}; {2} jours consécutifs)",
                                     "Durée", "jours", 0],
        c.I_TGG:                    ["Valeur moyenne (à partir de Tmin et Tmax)", "Température", "°C", 1],
        c.I_TNG:                    ["Température minimale", "Nbr. mois", "", 1],
        c.I_TNX:                    ["Valeur maximale de Tmin", "Température", "°C", 1],
        c.I_TXG:                    ["Valeur moyenne de Tmax", "Température", "°C", 1],
        c.I_TXX:                    ["Température maximale", "Température", "°C", 1],
        c.I_TNG_MONTHS_BELOW:       ["Nbr mois frais (moyenne(Tmin) < {1}°C)", "Nbr. mois", "mois", 1],
        c.I_TX_DAYS_ABOVE:          ["Nombre de jours chauds (Tmax > {1})", "Nbr. jours", "jours", 0],
        c.I_TN_DAYS_BELOW:          ["Nombre de jours frais (Tmin < {1})", "Nbr. jours", "jours", 0],
        c.I_TROPICAL_NIGHTS:        ["Nombre de nuits chaudes (Tmin > {1})", "Nbr. jours", "jours", 0],
        c.I_WSDI:                   ["Indice de durée des périodes chaudes (Tmax ≥ {1}; {2} jours consécutifs)",
                                     "Indice", "", 0],
        c.I_RX1DAY:                 ["Cumul de précipitation (1 jour)", "Cumul", "mm", 0],
        c.I_RX5DAY:                 ["Cumul de précipitation (5 jours)", "Cumul", "mm", 0],
        c.I_CDD:                    ["Nombre de jours secs consécutifs (P < {1} mm)", "Nbr. jours", "jours", 0],
        c.I_CWD:                    ["Nombre de jours pluvieux consécutifs (P ≥ {1} mm)", "Nbr. jours", "jours", 0],
        c.I_DRY_DAYS:               ["Nombre de jours secs (P < {1} mm)", "Nbr. jours", "jours", 0],
        c.I_WET_DAYS:               ["Nombre de jours pluvieux (P ≥ {1} mm)", "Nbr. jours", "jours", 0],
        c.I_PRCPTOT:                ["Cumul de précipitation", "Cumul", "mm", 0],
        c.I_R10MM:                  ["Nombre de jours avec P ≥ 10 mm", "Nbr. jours", "jours", 0],
        c.I_R20MM:                  ["Nombre de jours avec P ≥ 20 mm", "Nbr. jours", "jours", 0],
        c.I_SDII:                   ["Intensité moyenne des précipitations", "Intensité", "mm/day", 0],
        c.I_RAIN_SEASON_START:      ["Début de la {1}saison de pluie", "Jour", "", 0],
        c.I_RAIN_SEASON_END:        ["Fin de la {1}saison de pluie", "Jour", "", 0],
        c.I_RAIN_SEASON_LENGTH:     ["Durée de la {1}saison de pluie", "Nbr. Jours", "jours", 0],
        c.I_RAIN_SEASON_PRCPTOT:    ["Cumul de précipitation pendant la {1}saison de pluie", "Cumul", "mm", 0],
        c.I_DRY_SPELL_TOTAL_LENGTH: ["Durée totale des périodes sèches (P < {1} mm/jour; {2} jours consécutifs)",
                                     "Nbr. jours", "jours", 0],
        c.I_WG_DAYS_ABOVE:          ["Nombre de jours avec vent fort directionnel (Vmoy ≥ {1}; de {3}±{4}°)",
                                     "Nbr. jours", "jours", 0],
        c.I_WX_DAYS_ABOVE:          ["Nombre de jours avec vent fort (Vmax ≥ {1})",
                                     "Nbr. jours", "jours", 0],
        c.I_DROUGHT_CODE:           ["Code de sécheresse", "Code", "", 0]
    }


class VarIdx(cl_object.Obj):
    
    """
    --------------------------------------------------------------------------------------------------------------------
    Class defining the object VarIdx.
    --------------------------------------------------------------------------------------------------------------------
    """

    # Parameters.
    _params = []

    # Ensemble name.
    _ens = ""

    def __init__(
        self,
        code: str,
        ens: Optional[str] = ""
    ):

        """
        ----------------------------------------
        Constructor.

        # Parameters.
        code: str
            Variable or index code.
        ens: Optional[str]
            Ensemble name.
        ----------------------------------------
        """

        # Variable or index name.
        vi_name = extract_vi_name(code)

        # Variable or index description.
        if (code == "") or (vi_name not in dict(code_props()).keys()):
            desc = ""
        else:
            desc = dict(code_props())[vi_name][0]

        # Ensemnble name.
        if ens != "":
            self._ens = ens
        else:
            if code in c.V_CORDEX:
                self.ens = c.ENS_CORDEX
            elif code in c.V_ECMWF:
                self.ens = c.ENS_ERA5
            elif code in c.V_ENACTS:
                self.ens = c.ENS_ENACTS
            elif code in c.V_CHIRPS:
                self.ens = c.ENS_CHIRPS

        super(VarIdx, self).__init__(code=code, desc=desc)

    @property
    def name(
        self
    ) -> str:

        """
        ----------------------------------------
        Extract name.

        Returns
        -------
        str
            Name.
        ----------------------------------------
        """

        pos = self.code.rfind("_")
        if pos >= 0:
            tokens = self.code.split("_")
            if tokens[len(tokens) - 1].isdigit():
                return self.code[0:pos]

        return self.code

    @property
    def identifier(
        self
    ) -> str:

        """
        ----------------------------------------
        Extract identifier.

        The identifier is the number at the end of the code if there are multiple indices with the same name
        but with different parameters.

        Returns
        -------
        str
            Identifier.
        ----------------------------------------
        """

        return self.code.replace(self.name, "").replace("_", "")

    @property
    def desc(
        self,
    ) -> str:

        """
        ----------------------------------------
        Get description.

        Returns
        -------
        str
            Description.
        ----------------------------------------
        """

        desc = dict(code_props())[self.name][0]

        # Number of parameters.
        n_param = len(self.params)

        def format_centile(
            _param: str,
            _unit: str
        ) -> str:
            is_centile = "p" in _param
            return _param.replace("p", "") + ("e centile" if is_centile else _unit)

        for i in range(1, len(self.params) + 1):

            param = str(self.params[i - 1])
            val = ""
            key = "{" + str(i) + "}"

            # Assign 1st parameter.
            if (i == 1) and (key in desc):
                if self.name in [c.I_RAIN_SEASON_START, c.I_RAIN_SEASON_END, c.I_RAIN_SEASON_LENGTH,
                                 c.I_RAIN_SEASON_PRCPTOT]:
                    val = self.identifier
                    if val != "":
                        val += "ère " if val == "1" else "e "
                elif self.name in [c.I_HEAT_WAVE_MAX_LENGTH, c.I_HEAT_WAVE_TOTAL_LENGTH, c.I_HOT_SPELL_MAX_LENGTH,
                                   c.I_HOT_SPELL_FREQUENCY, c.I_HOT_SPELL_TOTAL_LENGTH, c.I_TX_DAYS_ABOVE,
                                   c.I_TN_DAYS_BELOW, c.I_TROPICAL_NIGHTS, c.I_WG_DAYS_ABOVE, c.I_WX_DAYS_ABOVE]:
                    unit = ""
                    if self.name in [c.I_HEAT_WAVE_MAX_LENGTH, c.I_HEAT_WAVE_TOTAL_LENGTH, c.I_HOT_SPELL_MAX_LENGTH,
                                     c.I_HOT_SPELL_FREQUENCY, c.I_HOT_SPELL_TOTAL_LENGTH, c.I_TX_DAYS_ABOVE,
                                     c.I_TN_DAYS_BELOW, c.I_TROPICAL_NIGHTS]:
                        unit = VarIdx(c.V_TASMAX).unit
                    elif self.name in [c.I_WG_DAYS_ABOVE, c.I_WX_DAYS_ABOVE]:
                        unit = VarIdx(c.V_SFCWINDMAX).unit
                    val = format_centile(param, unit)
                elif self.name in [c.I_WSDI]:
                    unit = VarIdx(c.V_TASMAX).unit
                    val = format_centile("90p" if param == "nan" else param, unit)
                elif param != "nan":
                    val = param
                desc = desc.replace(key, val)

            # Assign 2nd parameter.
            elif (i == 2) and (key in desc):
                if self.name == c.I_PRCPTOT:
                    val = param if n_param >= 2 else "1"
                elif self.name in [c.I_HEAT_WAVE_MAX_LENGTH, c.I_HEAT_WAVE_TOTAL_LENGTH]:
                    unit = VarIdx(c.V_TASMAX).unit
                    val = format_centile(param, unit)
                elif param != "nan":
                    val = param
                desc = desc.replace(key, val)

            # Assign 3rd parameter.
            elif (i == 3) and (key in desc):
                if self.name == c.I_PRCPTOT:
                    val = param if n_param >= 3 else "365"
                elif param != "nan":
                    val = param
                desc = desc.replace(key, val)

            # Assign 4th parameter.
            if (i == 4) and (key in desc):
                if param != "nan":
                    val = param
                desc = desc.replace(key, val)

        # Special cases.
        if (self.name == c.I_PRCPTOT) and (n_param >= 2):
            desc += "(" + str(self.params[0]) + " à " + str(self.params[1]) + ")"
        if (self.name == c.I_DRY_SPELL_TOTAL_LENGTH) and (n_param >= 5):
            desc = desc.replace(")", "; " + str(self.params[3]) + " à " + str(self.params[4]) + ")")

        return desc

    @property
    def label(
        self
    ) -> str:

        """
        ----------------------------------------
        Combine description and unit.

        Returns
        -------
        str
            Combine description and unit.
        ----------------------------------------
        """

        label = dict(code_props())[extract_vi_name(self.code)][1]

        unit = str(self.unit)
        if (unit not in ["", "1"]) and (unit not in label):
            label += " (" + unit + ")"

        return label

    @property
    def unit(
        self
    ) -> str:
    
        """
        ----------------------------------------
        Get unit.

        Returns
        -------
        str
            Unit.
        ----------------------------------------
        """

        return dict(code_props())[extract_vi_name(self.code)][2]

    @property
    def precision(
        self
    ) -> int:

        """
        ----------------------------------------
        Get precision (number of decimals).

        Returns
        -------
        int
            Precision (number of decimals).
        ----------------------------------------
        """

        return dict(code_props())[extract_vi_name(self.code)][3]

    @property
    def is_var(
        self
    ) -> bool:
        
        """
        ----------------------------------------
        Determine if the instance is a recognized climate variable.

        Returns
        -------
        bool
            True if the current instance is a recognized climate variable.
        ----------------------------------------
        """

        return self.name in (c.V_CORDEX + c.V_ECMWF + c.V_ENACTS + c.V_CHIRPS)

    @property
    def is_idx(
            self
    ) -> bool:

        """
        ----------------------------------------
        Determine if the instance is a recognized climate index.

        Returns
        -------
        bool
            True if the current instance is a recognized climate index.
        ----------------------------------------
        """

        return self.name in c.indices

    @property
    def is_var_or_idx(
        self
    ) -> bool:

        """
        ----------------------------------------
        Determine if the instance is a recognized climate variable or climate index.

        Returns
        -------
        bool
            True if the current instance is a recognized climate variable or climate index.
        ----------------------------------------
        """

        return self.is_var or self.is_idx

    @property
    def is_summable(
        self
    ) -> bool:

        """
        ----------------------------------------
        Determine if the variable is summable.

        An summable variable can have its values summed up for any given frequency. For instance, we can calculate the
        the sum of precipitation values in one month. This is not the case for temperature, for which a mean
        value can be calculated instead.
        ----------------------------------------
        """

        summable_variables = [c.V_PR, c.V_EVSPSBL, c.V_EVSPSBLPOT, c.V_ECMWF_TP, c.V_ECMWF_E, c.V_ECMWF_PEV,
                              c.V_ENACTS_RR, c.V_ENACTS_PET, c.V_CHIRPS_PRECIP]

        return self.name in summable_variables

    @property
    def is_volumetric(
        self
    ) -> bool:

        """
        ----------------------------------------
        Determine if the variable is a volumetric.

        An volumetric variable has a volume. For instance, an amount of precipitation has a corresponding height, area
        or volume. This is not the case for temperature.
        ----------------------------------------
        """

        volumetric_variables = [c.V_PR, c.V_EVSPSBL, c.V_EVSPSBLPOT, c.V_SNW, c.V_ECMWF_TP, c.V_ECMWF_E, c.V_ECMWF_PEV,
                                c.V_ECMWF_SNW, c.V_ENACTS_RR, c.V_ENACTS_PET, c.V_CHIRPS_PRECIP]

        return self.name in volumetric_variables

    @property
    def is_group(
            self
    ) -> bool:

        """
        ----------------------------------------
        Determine if the instance is a group of indices.
        ----------------------------------------
        """

        return group(self.code) == self.code

    @property
    def ens(
        self
    ) -> str:

        """
        ----------------------------------------
        Get ensemble name.

        Returns
        -------
        str
            Ensemble name.
        ----------------------------------------
        """

        return self._ens

    @ens.setter
    def ens(
        self,
        ens: str
    ):

        """
        ----------------------------------------
        Set ensemble name.

        Parameters
        ----------
        ens: str
            Ensemble name.
        ----------------------------------------
        """

        self._ens = ens

    @property
    def params(
        self
    ) -> List[any]:

        """
        ----------------------------------------
        Get parameters.

        Returns
        -------
        List[any]
            Parameters.
        ----------------------------------------
        """

        # By default, use the available parameters.
        params = self._params

        # If no parameters are set, use those in the configuration file.
        if len(params) == 0:
            params = cntx.idx_params_from_code(self.code)

        return params

    @params.setter
    def params(
        self,
        params: List[any]
    ):

        """
        ----------------------------------------
        Set parameters.

        Parameters
        ----------
        params: List[any]
            Parameters.
        ----------------------------------------
        """

        self._params = params

    def convert_name(
        self,
        ens: str
    ) -> Union[any, str]:

        """
        ----------------------------------------
        Convert from CORDEX variable name to the equivalent variable name in another set (ERA5*, ENACTS, CHIRPS)
        (or the opposite).

        Parameters
        ----------
        ens: str
            Ensemble.
        ----------------------------------------
        """

        # Equivalences.
        #        CORDEX          ERA5*              ENACTS           CHIRPS
        #        ---------------------------------------------------------------------
        equi = [[c.V_SFTLF,      c.V_ECMWF_LSM,     "",              ""               ],
                [c.V_TAS,        c.V_ECMWF_T2M,     "",              ""               ],
                [c.V_TASMIN,     c.V_ECMWF_T2MMIN,  c.V_ENACTS_TMIN, ""               ],
                [c.V_TASMAX,     c.V_ECMWF_T2MMAX,  c.V_ENACTS_TMAX, ""               ],
                [c.V_PR,         c.V_ECMWF_TP,      c.V_ENACTS_RR,   c.V_CHIRPS_PRECIP],
                [c.V_UAS,        c.V_ECMWF_U10,     "",              ""               ],
                [c.V_VAS,        c.V_ECMWF_V10,     "",              ""               ],
                [c.V_SFCWINDMAX, c.V_ECMWF_UV10MAX, "",              ""               ],
                [c.V_PS,         c.V_ECMWF_SP,      "",              ""               ],
                [c.V_RSDS,       c.V_ECMWF_SSRD,    "",              ""               ],
                [c.V_EVSPSBL,    c.V_ECMWF_E,       "",              ""               ],
                [c.V_EVSPSBLPOT, c.V_ECMWF_PEV,     c.V_ENACTS_PET,  ""               ],
                [c.V_HUSS,       c.V_ECMWF_SH,      "",              ""               ],
                [c.V_SNW,        c.V_ECMWF_SNW,     "",              ""               ]]

        # Loop through equivalences.
        for i in range(len(equi)):

            # Verify if there is a match.
            if self.name in equi[i]:
                if self.ens == c.ENS_CORDEX:
                    if ens in [c.ENS_ERA5, c.ENS_ERA5_LAND]:
                        return equi[i][1]
                    elif ens == c.ENS_ENACTS:
                        return equi[i][2]
                    elif ens == c.ENS_CHIRPS:
                        return equi[i][3]
                else:
                    return equi[i][0]

        return None

    def equi_path(
        self,
        p: str,
        vi_code_b: str,
        rcp: str
    ) -> str:

        """
        ----------------------------------------
        Determine the equivalent path for another variable or index.

        Parameters
        ----------
        p: str
            Path associated with the current instance.
        vi_code_b: str
            Name of climate variable or index to replace with.
        rcp: str
            Emission scenario.
        ----------------------------------------
        """

        # Determine if we have variables or indices.
        vi_code_a = self.code
        varidx_b = VarIdx(vi_code_b)
        a_is_var = self.name in cntx.vars.code_l
        b_is_var = varidx_b.name in cntx.vars.code_l
        fn = os.path.basename(p)

        # No conversion required.
        if vi_code_a != vi_code_b:

            # Variable->Variable or Index->Index.
            if (a_is_var and b_is_var) or (not a_is_var and not b_is_var):
                p = p.replace(self.name, varidx_b.name)

            # Variable -> Index (or the opposite)
            else:

                # Variable -> Index.
                if a_is_var and not b_is_var:
                    p = cntx.d_idx(vi_code_b)

                # Index -> Variable.
                else:
                    if rcp == c.REF:
                        p = cntx.d_ref(vi_code_b)
                    else:
                        p = cntx.d_scen(c.CAT_QQMAP, vi_code_b)
                # Both.
                if rcp == c.REF:
                    p += varidx_b.name + "_" + c.REF + "." + cntx.f_data_out
                else:
                    p += fn.replace(self.name + "_", varidx_b.name + "_")

        return p

    @property
    def requirements(
        self
    ) -> List[str]:

        """
        ----------------------------------------
        List the climate variables and indices that are required to calculate the current climate index.

        Parameters
        ----------
        List[str]
            List of climate variable and index codes.
        ----------------------------------------
        """

        vi_code_l = []

        # Temperature.
        if self.name in [c.I_TNX, c.I_TNG, c.I_TROPICAL_NIGHTS, c.I_TNG_MONTHS_BELOW, c.I_HEAT_WAVE_MAX_LENGTH,
                         c.I_HEAT_WAVE_TOTAL_LENGTH, c.I_TGG, c.I_ETR, c.I_TN_DAYS_BELOW]:
            vi_code_l.append(c.V_TASMIN)

        if self.name in [c.I_TX90P, c.I_TX_DAYS_ABOVE, c.I_HOT_SPELL_FREQUENCY, c.I_HOT_SPELL_MAX_LENGTH,
                         c.I_HOT_SPELL_TOTAL_LENGTH, c.I_TXG, c.I_TXX, c.I_WSDI, c.I_HEAT_WAVE_MAX_LENGTH,
                         c.I_HEAT_WAVE_TOTAL_LENGTH, c.I_TGG, c.I_ETR]:
            vi_code_l.append(c.V_TASMAX)

        # Precipitation.
        if self.name in [c.I_RX1DAY, c.I_RX5DAY, c.I_CWD, c.I_CDD, c.I_SDII, c.I_PRCPTOT, c.I_R10MM, c.I_R20MM,
                         c.I_WET_DAYS, c.I_DRY_DAYS, c.I_RAIN_SEASON_START, c.I_RAIN_SEASON_END,
                         c.I_RAIN_SEASON_PRCPTOT, c.I_RAIN_SEASON_LENGTH, c.I_DRY_SPELL_TOTAL_LENGTH, c.I_RAIN_SEASON]:

            if self.name != c.I_RAIN_SEASON_LENGTH:
                vi_code_l.append(c.V_PR)

            if self.name in [c.I_RAIN_SEASON_END, c.I_RAIN_SEASON]:
                if c.V_EVSPSBLPOT in cntx.vars.code_l:
                    vi_code_l.append(c.V_EVSPSBLPOT)
                elif c.V_EVSPSBL in cntx.vars.code_l:
                    vi_code_l.append(c.V_EVSPSBL)
                else:
                    vi_code_l.append("nan")

            if self.name in [c.I_RAIN_SEASON_END, c.I_RAIN_SEASON_LENGTH, c.I_RAIN_SEASON_PRCPTOT]:
                vi_code_l.append(self.code.replace(self.name, c.I_RAIN_SEASON_START))

            if self.name == c.I_RAIN_SEASON:
                vi_code_l.append("nan")

            if (self.name in [c.I_RAIN_SEASON_END, c.I_RAIN_SEASON]) and (len(self.params) > 7):
                vi_code_l.append(str(self.params[len(self.params) - 1]))

            if self.name in [c.I_RAIN_SEASON_LENGTH, c.I_RAIN_SEASON_PRCPTOT]:
                vi_code_l.append(self.code.replace(self.name, c.I_RAIN_SEASON_END))

        # Temperature-precipitation.
        if self.name == c.I_DROUGHT_CODE:
            vi_code_l.append(c.V_TAS)
            vi_code_l.append(c.V_PR)

        # Wind.
        if self.name == c.I_WG_DAYS_ABOVE:
            vi_code_l.append(c.V_UAS)
            vi_code_l.append(c.V_VAS)

        elif self.name == c.I_WX_DAYS_ABOVE:
            vi_code_l.append(c.V_SFCWINDMAX)

        return vi_code_l

    def list_simulations(
        self,
        rcp_code: str
    ) -> List[str]:

        """
        ----------------------------------------
        List simulations to consider.

        A climate index can be excluded, based on:
        - exception lists
        - the availability of dependencies (climate scenarios and indices).

        Parameters
        ----------
        rcp_code: str
            Emission scenario.

        Returns
        -------
        List[str]
            List of simulations.
        ----------------------------------------
        """

        if self.is_var:
            sim_code_l = self.list_simulations_for_scen(rcp_code)
        else:
            sim_code_l = self.list_simulations_for_idx(rcp_code)

        return sim_code_l

    def list_simulations_for_scen(
        self,
        rcp_code: Optional[str]
    ) -> List[str]:

        """
        ----------------------------------------
        List available simulations.

        Parameters
        ----------
        rcp_code: Optional[str]
            Emission scenario code.

        Returns
        -------
        List[str]
            List of simulation codes.
        ----------------------------------------
        """

        # List all simulations.
        p_sim_ref_l, p_sim_fut_l = cntx.list_cordex(self.name, rcp_code=rcp_code)

        # Filter simulations.
        sim_code_l = []
        for p_sim_fut in p_sim_fut_l:
            sim_code = os.path.basename(os.path.dirname(p_sim_fut)) + "_" + os.path.basename(p_sim_fut)
            if not cntx.exclude_simulation(self.name, sim_code, c.CAT_SCEN):
                sim_code_l.append(sim_code)

        sim_code_l.sort()

        return sim_code_l

    def list_simulations_for_idx(
        self,
        rcp_code: Optional[str]
    ) -> List[str]:

        """
        ----------------------------------------
        List simulations to consider.

        A climate index can be excluded, based on:
        - exception lists
        - the availability of dependencies (climate scenarios and indices).

        Parameters
        ----------
        rcp_code: Optional[str]
            Emission scenario.

        Returns
        -------
        List[str]
            List of simulations.
        ----------------------------------------
        """

        # Function that extracts simulation code from a path.
        def extract_sim_code(
            p: str
        ) -> str:
            if (c.CAT_SCEN + cntx.sep + c.CAT_OBS in p) or ("_" + c.REF in p):
                return c.REF
            else:
                return os.path.basename(p).replace(vi_name_0 + "_", "").replace("." + cntx.f_data_out, "")

        # List required climate variables and indices.
        vi_code_l = self.requirements

        # Verify if variable or index is available for the current station.
        for vi_code in vi_code_l:
            if ((vi_code != "nan") and
                ((not os.path.isdir(cntx.d_scen(c.CAT_QQMAP, vi_code))) and
                 (not os.path.isdir(cntx.d_idx(vi_code))))):
                return []

        # List simulation files for the first variable. As soon as there is no file for one variable, the
        # analysis for the current RCP needs to abort.
        varidx_0 = VarIdx(vi_code_l[0])
        vi_code_0 = varidx_0.code
        vi_name_0 = varidx_0.name
        vi_code_grp_0 = group(vi_code_0) if varidx_0.is_group else vi_code_0

        sim_code = "*_" + rcp_code
        if varidx_0.is_var:
            p_sim_l = [cntx.p_scen(c.CAT_OBS, vi_name_0, c.REF)] +\
                      list(glob.glob(cntx.p_scen(c.CAT_QQMAP, vi_name_0, sim_code)))
        else:
            p_sim_l = [cntx.p_idx(vi_code_grp_0, vi_name_0, c.REF)] +\
                      list(glob.glob(cntx.p_idx(vi_code_grp_0, vi_name_0, sim_code)))

        if not p_sim_l:
            return []

        sim_code_l = []

        # Select the simulations that are not present in an exception list.
        p_sim_filter_l = []
        for p_sim in p_sim_l:
            sim_code = extract_sim_code(p_sim)
            if (not cntx.exclude_simulation(self.name, sim_code)) and os.path.exists(p_sim):
                p_sim_filter_l.append(p_sim)
                sim_code_l.append(sim_code)
        p_sim_l = p_sim_filter_l

        # Ensure that simulations are available for other variables than the first one.
        if len(vi_code_l) > 1:

            # Loop through simulations.
            for p_sim_i in p_sim_l:

                # Determine if there is at least one dataset missing.
                missing = False
                for vi_code_j in vi_code_l[1:]:
                    if vi_code_j != "nan":
                        p_sim_j = varidx_0.equi_path(p_sim_i, vi_code_j, rcp_code)
                        if not os.path.exists(p_sim_j):
                            missing = True
                            break

                # Remove simulation code.
                if missing:
                    sim_code = extract_sim_code(p_sim_i)
                    if sim_code in sim_code_l:
                        sim_code_l.remove(sim_code)

        sim_code_l.sort()

        return sim_code_l


class VarIdxs(cl_object.Objs):
    
    """
    --------------------------------------------------------------------------------------------------------------------
    Class defining the object VarIdxs.
    --------------------------------------------------------------------------------------------------------------------
    """

    def __init__(
        self,
        *args
    ):

        """
        ----------------------------------------
        Constructor.
        ----------------------------------------
        """

        super().__init__()

        if len(args) > 0:
            if args[0] == "*":
                self.load()
            else:
                self.add(args[0])

    def load(
        self
    ):

        """
        ----------------------------------------
        Load items.
        ----------------------------------------
        """
        
        code_l = []

        # Codes.
        project_code = cntx.project.code if cntx.project is not None else ""
        view_code = cntx.view.code if cntx.view is not None else ""
        if view_code == c.VIEW_CLUSTER:
            view_code = c.VIEW_TS

        # The items are extracted from file names.
        # ~/<project_code>/<view_code>/*/*.csv
        if view_code == c.VIEW_TBL:

            pattern = project_code + "/<view_code>/*/*.csv"
            pattern = pattern.replace("<view_code>/", view_code + "/")

            p_l = list(cntx.files(pattern)[cl_gd.PROP_PATH])
            for p_i in p_l:
                code = os.path.basename(os.path.dirname(p_i))
                if code not in code_l:
                    code_l.append(code)

        # The items are extracted from directory names.
        # ~/<project_code>/<view_code>/<varidx_code>/*
        elif view_code in [c.VIEW_TS, c.VIEW_MAP, c.VIEW_CYCLE, c.VIEW_TS_BIAS, c.VIEW_CLUSTER, c.VIEW_TAYLOR]:

            pattern = project_code + "/<view_code>/*"
            if view_code == c.VIEW_CYCLE:
                pattern = pattern.replace("<view_code>/", view_code + "*/")
            else:
                pattern = pattern.replace("<view_code>/", view_code + "/")

            p_l = list(cntx.files(pattern)[cl_gd.PROP_PATH])
            p_l = list(set([p.replace(project_code + "/", "") for p in p_l]))
            code_l = list(set([p.split("/")[1] for p in p_l if len(p.split("/")) > 0]))

            # Remove any item that is not a climate variable or climate index.
            if view_code == c.VIEW_MAP:
                code_l = [code for code in code_l if VarIdx(code).is_var_or_idx]

        code_l.sort()

        self.add(code_l)

    def add(
        self,
        item: Union[str, List[str], VarIdx],
        ens: Optional[str] = "",
        inplace: bool = True
    ):

        """
        ----------------------------------------
        Add one or several items.

        Parameters
        ----------
        item : Union[str, List[str], VarIdx]
            Item (code, list of codes or instance of VarIdx).
        ens: Optional[str]
            Ensemble name.
        inplace : bool
            If True, modifies the current instance.
        ----------------------------------------
        """

        items = []

        if isinstance(item, VarIdx):
            items = [item]

        else:
            code_l = item
            if isinstance(item, str):
                code_l = [item]
            for i in range(len(code_l)):
                items.append(VarIdx(code_l[i], ens))

        return super(VarIdxs, self).add(items, inplace)

    @property
    def desc_l(
        self
    ) -> List[str]:

        """
        ----------------------------------------
        Get a list of descriptions.

        Returns
        -------
        List[str]
            Descriptions.
        ----------------------------------------
        """

        desc_l = []

        for item in self._items:
            desc_l.append(item.desc)
        desc_l.sort()

        return desc_l

    @property
    def name_l(
        self
    ) -> List[str]:

        """
        ----------------------------------------
        Get a list of names.

        Returns
        -------
        List[str]
            Names.
        ----------------------------------------
        """

        name_l = []

        for item in self._items:
            name_l.append(item.name)

        return name_l


def extract_vi_name(
    vi_code: str
) -> str:

    """
    --------------------------------------------------------------------------------------------------------------------
    Extract name.

    Parameters
    ----------
    vi_code: str
        Variable or index code.

    Returns
    -------
    str
        Variable or index name.
    --------------------------------------------------------------------------------------------------------------------
    """

    pos = vi_code.rfind("_")
    if pos >= 0:
        tokens = vi_code.split("_")
        if tokens[len(tokens) - 1].isdigit():
            return vi_code[0:pos]

    return vi_code


def group(
    vi_code: str = ""
) -> str:

    """
    --------------------------------------------------------------------------------------------------------------------
    Get the name of a group of indices.

    Parameters
    ----------
    vi_code : str, optional
        Variable or index code.

    Returns
    -------
    str
        Group name.
    --------------------------------------------------------------------------------------------------------------------
    """

    for key in list(c.i_groups.keys()):
        if vi_code in c.i_groups[key]:
            return key

    return ""


def explode_idx_l(
    idx_group_l
) -> [str]:

    """
    --------------------------------------------------------------------------------------------------------------------
    Explode a list of index names or codes, e.g. [rain_season_1, rain_season_2] into
    [rain_season_start_1, rain_season_end_1, rain_season_length_1, rain_season_prcptot_1,
     rain_season_start_2, rain_season_end_2, rain_season_length_2, rain_season_prcptot_2].

    Parameters
    ----------
    idx_group_l: [str]
        List of climate index groups.
    --------------------------------------------------------------------------------------------------------------------
    """

    idx_l_new = []

    # Loop through index names or codes.
    for i in range(len(idx_group_l)):
        idx_code = idx_group_l[i]

        # Loop through index groups.
        in_group = False
        for key in c.i_groups:

            # Explode and add to list.
            if c.i_groups[key][0] in idx_code:
                in_group = True

                # Extract instance number of index (ex: "_1").
                no = idx_code.replace(idx_code, "")

                # Loop through embedded indices.
                for k in range(len(c.i_groups[key][1])):
                    idx_l_new.append(c.i_groups[key][1][k] + no)

        if not in_group:
            idx_l_new.append(idx_code)

    return idx_l_new
