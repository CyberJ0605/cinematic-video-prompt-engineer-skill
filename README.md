# Cinematic Video Prompt Engineer Skill

电影感视频提示词工程师 Codex skill。

它用于把剧情梗概、人物关系、场景设定和情绪方向，改写成适合 AI 视频模型生成的电影感视频提示词。默认采用“打磨模式”：先诊断剧情，再给出电影化改写策略、可选参考图提示词，最后输出可复制的视频提示词。

## 适合用于

- 8-15 秒 AI 视频片段
- 情绪戏、亲密张力、悬疑、家庭冲突、回忆蒙太奇
- 人物头部特写和微表情表现
- 产品 / 人物质感短片
- 群像和大场面的 15 秒压缩
- 长剧情拆分成多条 15 秒提示词
- 用户满意第一条后继续生成下一条视频提示词

## 不适合直接用于

- 完整长片剧本
- 小说润色、标题、口播稿
- 一次性生成超过 15 秒的复杂剧情
- 缺少人物、场景、情绪目标的空泛需求
- 高复杂度武术动作设计，仍建议提供动作参考样本
- 依赖大量屏幕文字、字幕、UI 内容才能理解的画面
- 露骨性内容、未成年人性化、非自愿性内容、过度血腥内容

## 安装

把仓库里的 `cinematic-video-prompt-engineer` 文件夹复制到你的 Codex skills 目录。

Windows 默认路径：

```powershell
C:\Users\你的用户名\.codex\skills\cinematic-video-prompt-engineer
```

如果你已把 skills 目录迁移到其他位置，例如：

```powershell
D:\Codex\skills
```

则放到：

```powershell
D:\Codex\skills\cinematic-video-prompt-engineer
```

安装后的结构应为：

```text
cinematic-video-prompt-engineer/
  SKILL.md
  agents/
    openai.yaml
  references/
    style_patterns.md
```

不要出现同名嵌套目录：

```text
cinematic-video-prompt-engineer/cinematic-video-prompt-engineer/
```

## 使用

在 Codex 中调用：

```text
$cinematic-video-prompt-engineer
```

示例：

```text
请用 $cinematic-video-prompt-engineer 处理这个剧情：
深夜医院走廊，男人收到母亲抢救失败的消息，却因为年幼女儿在身边，只能蹲下给她系鞋带，把眼泪憋回去。
```

## 输出内容

默认输出：

```text
【剧情诊断】
【电影化改写策略】
【建议先生成的参考图】
【最终视频提示词】
```

如果用户只想要最终提示词，可以明确说“只给最终提示词”。

## 案例展示

以下视频由本 skill 输出的提示词生成，用于展示不同类型剧情的可控效果。

### 案例 1：情绪特写，古风女子从笑到哭

**原始剧情**

保持同一位古代宫廷女子不变，用超近面部长镜头表现她从强撑微笑到彻底破防落泪。

**调用方式**

```text
请用 $cinematic-video-prompt-engineer 写一段古代宫廷女子从笑到哭的超近面部长镜头情绪戏，保持人物、服装、烛光宫殿背景不变，全程无台词。
```

**生成视频**

<video src="./assets/demos/emotional-closeup.mp4" controls width="720"></video>

[查看视频文件](./assets/demos/emotional-closeup.mp4)

### 案例 2：悬疑，独居女孩发现陌生钥匙

**原始剧情**

深夜独居女孩回到家，发现玄关鞋柜上多了一把不属于自己的钥匙。她以为是自己记错了，走进客厅后，听见卧室里传来很轻的手机震动声。

**调用方式**

```text
请用 $cinematic-video-prompt-engineer 处理这个剧情：
深夜独居女孩回到家，发现玄关鞋柜上多了一把不属于自己的钥匙。她以为是自己记错了，走进客厅后，听见卧室里传来很轻的手机震动声。
```

**生成视频**

<video src="./assets/demos/suspense-key.mp4" controls width="720"></video>

[查看视频文件](./assets/demos/suspense-key.mp4)

### 案例 3：多人对话戏，除夕饭桌冲突

**原始剧情**

除夕夜饭桌上，一家三口吃饭。父亲突然宣布要把家里的老房子卖掉，母亲假装夹菜不说话，女儿停下筷子问为什么。父亲说这是为了她以后好，女儿意识到父母其实早就决定了，气氛变得很冷。

**调用方式**

```text
请用 $cinematic-video-prompt-engineer 处理这个剧情：
除夕夜饭桌上，一家三口吃饭。父亲突然宣布要把家里的老房子卖掉，母亲假装夹菜不说话，女儿停下筷子问为什么。父亲说这是为了她以后好，女儿意识到父母其实早就决定了，气氛变得很冷。
```

**生成视频**

<video src="./assets/demos/dialogue-scene.mp4" controls width="720"></video>

[查看视频文件](./assets/demos/dialogue-scene.mp4)

## 非 Codex 用户

Claude、ChatGPT、DeepSeek、Kimi、通义、豆包等工具一般不能直接安装 Codex skill，但可以使用通用提示词版本。

复制下面文件中的内容给对应 AI：

```text
PROMPT_VERSION.md
```

然后让它按规则扮演“电影感视频提示词工程师”即可。

## 项目文档

维护与交接说明见：

```text
docs/PROJECT_HANDOFF.md
```
