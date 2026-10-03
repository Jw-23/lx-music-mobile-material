# LX Music Mobile · Material 3 云端构建

本仓库保存 Material 3 改造源码补丁与 GitHub Actions 构建流程。构建会拉取 [LX Music Mobile 官方项目](https://github.com/lyswhut/lx-music-mobile)的完整源码，固定提交为 `fb8480728d875fa5e0da25eebd3a26bb71723aae`，应用补丁后生成可直接安装、不依赖开发服务器的 APK。

改造包含浅色／深色 Material 主题、歌曲与播放器的一键收藏、收藏状态实时刷新、歌单搜索、直接新建、歌曲数量、播放全部，以及新建歌单并添加歌曲。

## 下载 APK

1. 打开本仓库 **Actions → Build Material APK**。
2. 选择成功完成的构建，下载 **Artifacts → lx-music-material-apk**。
3. 解压后安装文件名以 **universal.apk** 结尾的 APK；也可按手机架构选择 arm64-v8a 或 armeabi-v7a。

首次提交工作流会自动构建；之后也可以在 Actions 页点击 **Run workflow**。下载包包含 SHA256 校验值和构建提交信息，保留 30 天。

应用名称为 **LX Music Material**，包名 `cn.toside.music.mobile.material`，可与官方应用同时安装。该个人测试版本采用官方源码仓库中的开发签名密钥，不是官方发行版，也不会继承官方应用的数据。歌单可用原有导入导出功能迁移。

## 构建内容

- `patches/lx-material.patch`：实际界面与收藏、歌单逻辑改造，以及 9 项行为检查。
- `scripts/configure-build.py`：设置独立安装包名与显示名称。
- `.github/workflows/android.yml`：配置 Node 20、Java 17、Android SDK / NDK，执行行为检查、生成主题、编译 Release APK 并验证签名。

完整官方源码及图片、字体和 Gradle Wrapper 在云端检出，避免缺失二进制资源。

源项目采用 Apache-2.0 及其 README 补充协议；补丁沿用原项目许可。原始 LICENSE 与协议随构建源码保留。
