from indic_transliteration import sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate
data = 'ellarum dense kellikku'
print(transliterate(data, sanscript.HK, sanscript.MALAYALAM))
