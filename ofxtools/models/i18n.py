# coding: utf-8
"""
Data structures for international support - OFX Section 5
"""
# local imports
from ofxtools.Types import (
    OneOf,
    Decimal,
)
from ofxtools.models.base import (
    Aggregate,
)


__all__ = ['CURRENCY', 'ORIGCURRENCY', ]


# 3-letter language codes
ISO639_2 = ('AAR', 'ABK', 'ACE', 'ACH', 'ADA', 'ADY', 'AFA', 'AFH', 'AFR',
            'AIN', 'AKA', 'AKK', 'SQI', 'ALE', 'ALG', 'ALT', 'AMH', 'ANG',
            'ANP', 'APA', 'ARA', 'ARC', 'ARG', 'HYE', 'ARN', 'ARP', 'ART',
            'ARW', 'ASM', 'AST', 'ATH', 'AUS', 'AVA', 'AVE', 'AWA', 'AYM',
            'AZE', 'BAD', 'BAI', 'BAK', 'BAL', 'BAM', 'BAN', 'EUS', 'BAS',
            'BAT', 'BEJ', 'BEL', 'BEM', 'BEN', 'BER', 'BHO', 'BIH', 'BIK',
            'BIN', 'BIS', 'BLA', 'BNT', 'BOS', 'BRA', 'BRE', 'BTK', 'BUA',
            'BUG', 'BUL', 'MYA', 'BYN', 'CAD', 'CAI', 'CAR', 'CAT', 'CEB',
            'CEL', 'CHA', 'CHB', 'CHE', 'CHG', 'ZHO', 'CHK', 'CHM', 'CHN',
            'CHO', 'CHP', 'CHR', 'CHV', 'CHY', 'CMC', 'COP', 'COR', 'COS',
            'CPE', 'CPF', 'CPP', 'CRE', 'CRH', 'CRP', 'CSB', 'CUS', 'CES',
            'DAK', 'DAN', 'DAR', 'DAY', 'DEL', 'DEN', 'DGR', 'DIN', 'DIV',
            'DOI', 'DRA', 'DSB', 'DUA', 'DUM', 'NLD', 'DZO', 'EFI', 'EGY',
            'EKA', 'ELX', 'ENG', 'ENM', 'EPO', 'EST', 'EWE', 'EWO', 'FAN',
            'FAO', 'FAT', 'FIJ', 'FIL', 'FIN', 'FON', 'FRA', 'FRM', 'FRO',
            'FRR', 'FRS', 'FRY', 'FUL', 'FUR', 'GAA', 'GAY', 'GBA', 'GEM',
            'KAT', 'GEZ', 'GIL', 'GLA', 'GLE', 'GLG', 'GLV', 'GMH', 'GOH',
            'GON', 'GOR', 'GOT', 'GRB', 'GRC', 'ELL', 'GRN', 'GSW', 'GUJ',
            'GWI', 'HAI', 'HAT', 'HAW', 'HEB', 'HER', 'HIL', 'HIM', 'HIN',
            'HIT', 'HMN', 'HMO', 'HRV', 'HSB', 'HUN', 'HUP', 'IBA', 'IBO',
            'ISL', 'IDO', 'III', 'IJO', 'ILE', 'ILO', 'INA', 'INC', 'IND',
            'INE', 'INH', 'IPK', 'IRA', 'IRO', 'ITA', 'JAV', 'JBO', 'JPN',
            'JPR', 'JRB', 'KAA', 'KAB', 'KAC', 'KAL', 'KAM', 'KAN', 'KAR',
            'KAS', 'KAW', 'KAZ', 'KBD', 'KHA', 'KHI', 'KHM', 'KHO', 'KIK',
            'KIN', 'KIR', 'KMB', 'KOK', 'KOM', 'KON', 'KOR', 'KOS', 'KPE',
            'KRC', 'KRL', 'KRO', 'KUA', 'KUM', 'KUR', 'KUT', 'LAD', 'LAH',
            'LAM', 'LAO', 'LAT', 'LAV', 'LEZ', 'LIM', 'LIN', 'LIT', 'LOL',
            'LOZ', 'LTZ', 'LUA', 'LUB', 'LUG', 'LUI', 'LUN', 'LUO', 'LUS',
            'MKD', 'MAD', 'MAG', 'MAH', 'MAI', 'MAK', 'MAL', 'MAN', 'MRI',
            'MAP', 'MAR', 'MAS', 'MSA', 'MDF', 'MDR', 'MEN', 'MGA', 'MIC',
            'MIN', 'MIS', 'MKH', 'MLG', 'MLT', 'MNC', 'MNI', 'MNO', 'MOH',
            'MON', 'MOS', 'MUL', 'MUN', 'MUS', 'MWL', 'MWR', 'MYN', 'MYV',
            'NAH', 'NAI', 'NAP', 'NAV', 'NBL', 'NDE', 'NDO', 'NDS', 'NEP',
            'NEW', 'NIA', 'NIC', 'NNO', 'NOB', 'NOG', 'NON', 'NOR', 'NQO',
            'NSO', 'NUB', 'NWC', 'NYA', 'NYM', 'NYN', 'NYO', 'NZI', 'OCI',
            'OJI', 'ORI', 'ORM', 'OSA', 'OSS', 'OTA', 'OTO', 'PAA', 'PAG',
            'PAL', 'PAM', 'PAN', 'PAP', 'PEO', 'FAS', 'PHI', 'PHN', 'PLI',
            'POL', 'PON', 'POR', 'PRA', 'PRO', 'PUS', 'QUE', 'RAJ', 'RAP',
            'RAR', 'ROA', 'ROH', 'ROM', 'RON', 'RUN', 'RUP', 'RUS', 'SAD',
            'SAG', 'SAH', 'SAI', 'SAL', 'SAM', 'SAN', 'SAS', 'SAT', 'SCN',
            'SCO', 'SEL', 'SEM', 'SGA', 'SGN', 'SHN', 'SID', 'SIN', 'SIO',
            'SIT', 'SLA', 'SLO', 'SLV', 'SMA', 'SME', 'SMI', 'SMJ', 'SMN',
            'SMO', 'SMS', 'SNA', 'SND', 'SNK', 'SOG', 'SOM', 'SON', 'SOT',
            'SPA', 'SRD', 'SRN', 'SRP', 'SRR', 'SSA', 'SSW', 'SUK', 'SUN',
            'SUS', 'SUX', 'SWA', 'SWE', 'SYC', 'SYR', 'TAH', 'TAI', 'TAM',
            'TAT', 'TEL', 'TEM', 'TER', 'TET', 'TGK', 'TGL', 'THA', 'BOD',
            'TIG', 'TIR', 'TIV', 'TKL', 'TLH', 'TLI', 'TMH', 'TOG', 'TON',
            'TPI', 'TSI', 'TSN', 'TSO', 'TUK', 'TUM', 'TUP', 'TUR', 'TUT',
            'TVL', 'TWI', 'TYV', 'UDM', 'UGA', 'UIG', 'UKR', 'UMB', 'UND',
            'URD', 'UZB', 'VAI', 'VEN', 'VIE', 'VOL', 'VOT', 'WAK', 'WAL',
            'WAR', 'WAS', 'CYM', 'WEN', 'WLN', 'WOL', 'XAL', 'XHO', 'YAO',
            'YAP', 'YID', 'YOR', 'YPK', 'ZAP', 'ZBL', 'ZEN', 'ZHA', 'ZND',
            'ZUL', 'ZUN', 'ZXX', 'ZZA')

LANG_CODES = ISO639_2

# Currency codes
ISO4217 = ('AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN',
           'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BOV',
           'BRL', 'BSD', 'BTN', 'BWP', 'BYR', 'BZD', 'CAD', 'CDF', 'CHE', 'CHF',
           'CHW', 'CLF', 'CLP', 'CNY', 'COP', 'COU', 'CRC', 'CUC', 'CUP', 'CVE',
           'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EEK', 'EGP', 'ERN', 'ETB', 'EUR',
           'FJD', 'FKP', 'GBP', 'GEL', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD',
           'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'INR', 'IQD', 'IRR',
           'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW',
           'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL',
           'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MUR',
           'MVR', 'MWK', 'MXN', 'MXV', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK',
           'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG',
           'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK',
           'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'STD', 'SVC', 'SYP', 'SZL', 'THB',
           'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX',
           'USD', 'USN', 'USS', 'UYI', 'UYU', 'UZS', 'VEF', 'VND', 'VUV', 'WST',
           'XAF', 'XAG', 'XAU', 'XBA', 'XBB', 'XBC', 'XBD', 'XCD', 'XDR', 'XOF',
           'XPD', 'XPF', 'XPT', 'XTS', 'XXX', 'YER', 'ZAR', 'ZMK', 'ZWL', 'CNH')

CURRENCY_CODES = ISO4217

# 2-letter Country codes
ISO3166_1a2 = ('AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AO', 'AQ', 'AR', 'AS',
               'AT', 'AU', 'AW', 'AX', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG',
               'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BQ', 'BR', 'BS', 'BT',
               'BV', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI',
               'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY',
               'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH',
               'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB',
               'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GP', 'GQ',
               'GR', 'GS', 'GT', 'GU', 'GW', 'GY', 'HK', 'HM', 'HN', 'HR', 'HT',
               'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT',
               'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP',
               'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS',
               'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH',
               'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU',
               'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NF', 'NG', 'NI',
               'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG',
               'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PS', 'PT', 'PW', 'PY', 'QA',
               'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG',
               'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'SS', 'ST',
               'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TF', 'TG', 'TH', 'TJ', 'TK',
               'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG',
               'UM', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU',
               'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW')

# 3-letter Country codes
ISO3166_1a3 = ('ABW', 'AFG', 'AGO', 'AIA', 'ALA', 'ALB', 'AND', 'ANT', 'ARE',
               'ARG', 'ARM', 'ASM', 'ATA', 'ATF', 'ATG', 'AUS', 'AUT', 'AZE',
               'BDI', 'BEL', 'BEN', 'BFA', 'BGD', 'BGR', 'BHR', 'BHS', 'BIH',
               'BLM', 'BLR', 'BLZ', 'BM', 'BOL', 'BRA', 'BRB', 'BRN', 'BTN',
               'BVT', 'BWA', 'CAF', 'CAN', 'CCK', 'CHE', 'CHL', 'CHN', 'CIV',
               'CMR', 'COD', 'COG', 'COK', 'COL', 'COM', 'CPV', 'CRI', 'CUB',
               'CXR', 'CYM', 'CYP', 'CZE', 'DE', 'DJI', 'DMA', 'DNK', 'DOM',
               'DZA', 'EC', 'EGY', 'ERI', 'ESH', 'ESP', 'EST', 'ETH', 'FIN',
               'FJI', 'FLK', 'FRA', 'FRO', 'FSM', 'GAB', 'GBR', 'GEO', 'GGY',
               'GHA', 'GIB', 'GIN', 'GLP', 'GMB', 'GNB', 'GNQ', 'GRC', 'GRD',
               'GRL', 'GTM', 'GUF', 'GUM', 'GUY', 'HKG', 'HMD', 'HND', 'HRV',
               'HTI', 'HUN', 'IDN', 'IMN', 'IND', 'IOT', 'IRL', 'IRN', 'IRQ',
               'ISL', 'ISR', 'ITA', 'JAM', 'JEY', 'JOR', 'JPN', 'KAZ', 'KEN',
               'KGZ', 'KHM', 'KIR', 'KNA', 'KOR', 'KWT', 'LAO', 'LBN', 'LBR',
               'LBY', 'LCA', 'LIE', 'LKA', 'LSO', 'LT', 'LUX', 'LVA', 'MAC',
               'MAF', 'MAR', 'MCO', 'MDA', 'MDG', 'MDV', 'MEX', 'MHL', 'MKD',
               'MLI', 'MLT', 'MMR', 'MNE', 'MNG', 'MNP', 'MOZ', 'MRT', 'MSR',
               'MTQ', 'MUS', 'MWI', 'MYS', 'MYT', 'NAM', 'NCL', 'NER', 'NFK',
               'NGA', 'NIC', 'NI', 'NLD', 'NOR', 'NPL', 'NR', 'NZL', 'OMN',
               'PAK', 'PAN', 'PCN', 'PER', 'PHL', 'PLW', 'PNG', 'POL', 'PRI',
               'PRK', 'PRT', 'PRY', 'PSE', 'PYF', 'QAT', 'RE', 'RO', 'RUS',
               'RWA', 'SA', 'SDN', 'SEN', 'SGP', 'SGS', 'SHN', 'SJM', 'SLB',
               'SLE', 'SLV', 'SMR', 'SOM', 'SPM', 'SRB', 'STP', 'SUR', 'SVK',
               'SVN', 'SWE', 'SWZ', 'SYC', 'SYR', 'TCA', 'TCD', 'TGO', 'THA',
               'TJK', 'TKL', 'TKM', 'TLS', 'TON', 'TTO', 'TUN', 'TUR', 'TUV',
               'TWN', 'TZA', 'UGA', 'UKR', 'UMI', 'URY', 'USA', 'UZB', 'VAT',
               'VCT', 'VEN', 'VGB', 'VIR', 'VNM', 'VUT', 'WLF', 'WSM', 'YEM',
               'ZAF', 'ZMB', 'ZWE')

COUNTRY_CODES = ISO3166_1a3


class CURRENCY(Aggregate):
    """ OFX section 5.2 """
    currate = Decimal(required=True)
    cursym = OneOf(*CURRENCY_CODES, required=True)


class ORIGCURRENCY(Aggregate):
    """ OFX section 5.2 """
    currate = Decimal(required=True)
    cursym = OneOf(*CURRENCY_CODES, required=True)


class Origcurrency(object):
    """ Mixin providing property aliases and CURRENCY/ORIGCURRENCY mutex """
    mutexes = [("currency", "origcurrency"), ]

    @property
    def curtype(self):
        cur = self.currency or self.origcurrency
        if cur:
            return (cur).__class__.__name__

    @property
    def cursym(self):
        cur = self.currency or self.origcurrency
        if cur:
            return cur.cursym

    @property
    def currate(self):
        cur = self.currency or self.origcurrency
        if cur:
            return cur.currate
