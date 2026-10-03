"""Give the personal Material build its own install identity."""
from pathlib import Path
import sys

root = Path(sys.argv[1])
gradle = root / 'android/app/build.gradle'
source = gradle.read_text()
original = 'applicationId "cn.toside.music.mobile"'
assert source.count(original) == 1, 'Unexpected upstream application ID configuration'
source = source.replace(original, 'applicationId "cn.toside.music.mobile.material"')
gradle.write_text(source)
strings = root / 'android/app/src/main/res/values/strings.xml'
source = strings.read_text()
assert '<string name="app_name">LX Music</string>' in source
strings.write_text(source.replace('<string name="app_name">LX Music</string>', '<string name="app_name">LX Music Material</string>'))
print('Prepared cn.toside.music.mobile.material (can coexist with official LX Music)')
