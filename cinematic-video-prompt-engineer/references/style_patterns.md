# Style Patterns

This reference captures the current house style for cinematic video prompts. Treat it as a living style library: add distilled rules and compact examples, not long pasted source prompts.

## Core Shape

The best prompts usually follow this order:

1. A short summary that includes duration, structure, emotional premise, and visual premise.
2. Optional model adaptation only if the user specifies a model.
3. Time-based shot design.
4. Camera, lens, framing, movement, and depth of field.
5. Physical action and composition.
6. Light, color, atmosphere, and environmental motion.
7. Character performance: inner logic, micro-reactions, physiological reactions.
8. Dialogue, voiceover, or inner monologue with timing.
9. Sound design and ending.

## Time Axis

Use time only when it improves generation clarity.

- For one continuous emotional beat: `0-3s / 3-8s / 8-12s`.
- For multi-shot prompts: `镜头 01`, `镜头 02`, etc.
- Each time block should contain a visible change: action, gaze, light, spatial relation, or sound.
- Avoid stuffing unrelated story events into a single 15s prompt.
- Do not end important dialogue or peak action exactly at the final second. Reserve 1-2 seconds for reaction, breath, silence, sound tail, or visual continuation.
- Time allocation should follow drama, not equal division. If a shot contains a line plus a complex action, give it more time or simplify it.
- If the ending feels rushed, remove a detail or split the prompt instead of making the final beat abrupt.

## Camera Language

Prefer specific but generation-friendly terms:

- 景别: `ECU`, `CU`, `MCU`, `MS`, `LS`.
- 焦段: `24mm`, `35mm`, `50mm`, `85mm`, `100mm macro`, `200mm`.
- 运镜: `Slow Push in`, `Track-in`, `Handheld Backward Tracking`, `Tilt down`, `Tilt up`, `Pan`, `Snap Pull Back`.
- Lens texture: shallow depth of field, anamorphic flare, bokeh, Chiaroscuro, hard side light, backlight, practical light.

Do not pile up terms. Use the terms that directly serve the scene's emotion.

## Performance Writing

Strong performance prompts use this sequence:

```text
内在逻辑：角色因...而...
显性动机：他/她表面上想...
微反应：眼睑、咬肌、嘴角、视线、手指...
生理反应：呼吸、吞咽、鼻翼、汗、颤抖、身体僵硬...
动作结果：最终做出一个清晰可见的动作。
```

Write emotions as body evidence:

- 压抑: jaw locked, lips pressed flat, shallow breath, hands clenching fabric, gaze avoiding contact.
- 崩塌: breath breaks, fingers release, eyes wet but fixed, smile appearing against the character's will.
- 决绝: still gaze, no blinking, body leans forward before action, breath stops then releases.
- 自由: posture opens, hair and clothes catch wind, eyes lock onto distant light, a small fearless smile.

## Long Facial Close-Up Micro-Expression Timeline

Use this pattern when a long head or face close-up must carry the emotion. It is especially useful for quiet grief, restraint, guilt, disappointment, shock, or emotional freezing. The goal is natural transition, not sudden expression jumps.

Template:

```text
0-2s：人物保持平静的表情，眼神轻轻低垂，嘴唇自然放松。
2-4s：情绪开始轻微变化，嘴唇慢慢轻轻抿住，嘴角开始一点点下压，眼神变得失落。
4-6s：难过逐渐明显但仍然克制，眉头轻轻皱起，嘴唇保持轻抿，眼神带着委屈和隐忍，眼眶微微湿润。
6-8s：人物稳定在隐忍难过的表情中，像在努力忍住眼泪。脸颊出现一两滴细小自然的泪滴或泪痕，但没有大哭，没有抽泣，情绪安静克制。
全过程表情自然过渡，微表情细腻，没有突然变化，没有夸张哭泣。
```

Adapt the emotion words to the scene:

- Shock freeze: relaxed face -> smile stops -> eyes lose focus -> breath stops -> jaw locks.
- Suppressed crying: calm -> lips press -> eyes redden -> tear line forms -> silent breath trembles.
- Guilt: gaze avoids -> blink slows -> mouth tightens -> brow folds inward -> face lowers.
- Anger under restraint: still gaze -> nostrils flare -> jaw hardens -> fingers tense -> eyes stay wet but unblinking.

When using this pattern, keep the camera simple: `ECU/CU`, stable or very slow `Push in`, shallow depth of field, minimal background motion. Do not overload it with complex blocking.

### Ultra-Close Face Long Take: Emotional Arc System

Use this when the entire scene is an ultra-close face performance and the user wants a dense emotional arc without dialogue. This is not only for crying scenes. It can be adapted to grief, shame, love, shyness, joy, guilt, fear, jealousy, cold cruelty, blackening, resolve, or any story where emotion unfolds mainly through eyes and micro-expressions.

Core setup:

```text
电影级超近面部特写，固定镜头或极慢 Push in，柔和自然窗光或烛光在脸上投下淡淡阴影。人物服装与发丝保持简洁真实。前半段尽量无肢体动作，所有表演凝聚在眼神、瞳孔、下眼睑、嘴角、双唇、泪水和呼吸里。全段无台词。
```

General rules:

- The camera may represent another person if the scene is subjective, e.g. `镜头即她的心上人，她像正在与心上人面对面交流一样看向镜头`.
- Keep camera stable: fixed ECU/CU, no shake, no complex blocking.
- Use a clear emotional waveform, not a flat mood: recognition -> reaction -> concealment -> leak -> recovery or collapse.
- For beauty/identity-heavy close-ups, define hair, makeup, clothing, accessories, light, and face stability, but avoid turning it into a fashion poster.
- No dialogue unless the story needs it; the face performs the scene.
- The timeline can be 8-10s for full arcs, or compressed to 4 beats for shorter clips.

#### Complex Grief Arc

Use for ancient costume tragedy, betrayal, lost love, fate, grief after realization, or a character silently accepting irreversible loss.

Emotional waveform:

```text
0-1.5s：失焦的双眼骤然聚拢，瞳孔微微扩散，下眼睑轻轻颤动，表现纯粹震惊与不敢相信。
1.5-2.5s：震惊凝固成冷意，嘴角一侧挑起极淡的、近乎嘲讽的冷笑，笑意不到眼底；目光下垂又抬起，带自嘲与疲惫的了然。
2.5-4s：冷笑渐渐加深成安静而微颤的微笑，像努力维持最后体面；眼眶泛红，泪水在下睫毛处聚满却不落。
4-6s：微笑彻底瓦解，双唇紧抿后开始轻颤；眼神彻底失焦，泪水终于大颗滚落，垂下眼帘，下巴微微抖动，无声哽咽。
6-7s：抽息余韵未散，缓缓低头，下巴轻收，胸腔里逸出极轻的叹息，肩膀微微塌下，像卸下最后的硬撑。
7-8s：深吸一口气，重新抬头，双唇奋力弯起一抹颤巍巍的温柔微笑；泪痕未干，眼底强撑出清透释然。
8-9s：抬手用指背小心擦泪，手触碰泪水瞬间，压抑的抽泣反扑，肩膀不受控抽动，微笑在泪水里失真，新的泪水顺着指缝滑落。
```

Use only when the prompt has enough time, usually 8-10 seconds. For shorter clips, compress to 4 beats:

```text
震惊聚焦 -> 冷笑自嘲 -> 微笑瓦解落泪 -> 强撑释然又被抽泣反扑。
```

Avoid:

- sudden crying before the emotional logic arrives
- exaggerated sobbing or theatrical grimacing
- too much hand/body action in the first half
- beauty-filter skin that erases tear and eyelid detail
- using this full waveform for every sad scene; reserve it for major emotional turns

#### Shy Love / Seeing the Beloved POV Arc

Use when a character sees the person they secretly love, especially in ancient costume, youth romance, first love, reunion, or restrained affection. The camera can be treated as the beloved's point of view.

Core setup:

```text
写实电影摄影质感，柔和午后自然窗光，固定机位，超近面部特写，镜头完全静止。角色为古代大户人家的闺中小姐，发型、发饰、妆容、服装精致但真实。全程无台词，无第二人。镜头即女子的心上人，她的眼神、微表情和情感变化都像正在与心上人面对面交流。
```

Emotional waveform:

```text
0-3s：她猛地停住，呼吸骤然一屏，眼眸因突然看见心上人而微微圆睁，瞳孔轻轻扩散；认出眼前人后，眼眸瞬间柔弯，压抑不住的欢喜从眼底暖暖漾开。
3-5s：羞意漫上心头，两颊泛起淡淡霞色。她慌忙垂下眼帘，睫毛乱颤，却又忍不住抬眼看向镜头；嘴角不受控制地上翘，又拼命往下压，最终凝成羞怯、甜中带怯的浅笑，下巴微微内收。
5-8s：笑意忽然在唇边僵住，眼神惊慌地从镜头上弹开，左右飘忽，不敢再看。她将脸偏向一侧，耳根与脖颈因极度害羞泛红，嘴唇紧抿，喉间极轻滚动，头微微低垂，只剩乱颤睫毛与微促鼻息泄露慌乱。
8-10s：克制许久后，她终于鼓起勇气怯怯抬眼，绵长温柔地直视镜头，像要把心上人的样子印进心里。睫毛狂颤，鼻翼微翕，无声深吸又缓缓呼出；双唇放松，隐秘甜蜜与忐忑期待在一抹恍惚动人的微笑中晕开。
```

Use this arc carefully:

- Best with one face, no second person visible.
- Keep the emotion sweet, restrained, and shy; avoid overt seduction.
- Add quality constraints for face stability when needed: face stable, clear features, natural motion, no blur, no flicker, no shake.
- If the scene is not romance, adapt the same structure: sudden recognition -> emotional leak -> concealment -> renewed courage.

#### Exhausted Silent Collapse Arc

Use when a character has already endured too much and finally collapses inward without dramatic crying. Best for emotional exhaustion, quiet despair, grief after long restraint, hopeless acceptance, powerless love, or a character realizing they cannot change the outcome.

Core setup:

```text
竖屏近景/超近面部特写，固定镜头或极轻微慢推，电影感真实人物表演。人物脸部占画面主体，头上被柔和半透明白纱或浅色衣料轻轻遮挡，服饰有真实褶皱和湿润质感，皮肤带自然油光与细小泪痕，眼眶泛红，睫毛被泪水打湿。下眼睑有明显泪光。整段无夸张动作，无台词，靠眼神、嘴唇、呼吸、眼泪和头部下垂表达情绪耗尽。
```

Emotional logic:

```text
不是嚎啕大哭，而是压抑、无声、心碎、委屈、失望、逐渐失力的哭泣。人物像刚经历了极大的伤害，心理还有一丝硬撑，情绪从无力、深度悲伤、命运感到空洞崩溃。最终不是爆发，而是安静地垮下来。
```

Emotional waveform:

```text
0-1s：人物微微抬着脸，三分之一侧脸靠近镜头，眼睛湿润发红，眼神空洞又受伤，像在看着某个人。下眼睑含满泪水，嘴唇轻轻抿住，肩颈轻微绷紧，呼吸很轻。
1-3s：视线慢慢从前方垂落到下方，眼皮变沉，眼神从看向某人变成向内坠落。泪水沿脸颊无声滑落，嘴角轻轻下压，唇部放松，表情从委屈转成失望，像心里最后一点希望正在慢慢熄灭。
3-5s：她缓缓低头，静默和肩膀失力增加，头部一点点垂下，眼睛不再看镜头。眼神藏到下方，眉头从紧绷变成疲惫，嘴唇轻轻闭合又微微松开，仿佛把哭声吞回去。脸上的泪痕持续变亮，但没有大哭、没有喊叫，只有无声崩溃。
5-8/9s：头彻底低下，自然和旁边衣料靠近，眼睛几乎看不见。整个人安静下来，情绪不是爆发，而是耗尽后的空白。肩膀轻微下沉，呼吸很浅，最后保持微垂姿态，像已经没有力气再哭。
```

Negative requirements:

- no exaggerated body movement
- no dramatic sobbing
- no screaming or visible shouting
- no sudden emotional jump
- no beauty-filter plastic skin
- keep face stable and realistic
- keep tears subtle, natural, and physically plausible

Useful tags:

```text
silent crying, restrained sobbing, fearful hollow eyes, downcast gaze, broken but quiet sadness, emotionally exhausted, quiet collapse
```

## Micro-Expression Action Library

Use these as modular facial-performance beats. Select only the beats that fit the story; do not stack too many expressions in one shot. For a 6-8s close-up, 3-5 beats are usually enough.

### Grief, Shock, and Emotional Freeze

- **失焦转呆滞**: 原本有焦点的双眼骤然紧紧撑住，随后瞳孔轻微扩散，视线像停在空处。
- **眼睑颤动**: 下眼睑轻轻颤动，像身体正在强行承受冲击。
- **笑容冻结**: 嘴角停在半笑的位置，笑意没有抵达眼底，随后嘴角一点点失去弧度。
- **目光回避再抬起**: 角色目光向下一垂，随后又抬起，眼中多了一份自嘲、疲惫或恍然。
- **泪水悬住**: 眼眶开始泛红，泪水在下睫毛处晶莹闪动，聚满却不落下。
- **泪水滚落**: 蓄满的泪水终于大颗滚落，沿着面颊自然流淌。
- **嘴部失控**: 微笑彻底瓦解，双唇紧抿，随后开始抑制不住地轻颤。
- **眼神失焦**: 眼神彻底失焦，空洞地望向前方，仿佛所有光都灭了。

### Numbness, Exhaustion, and Forced Calm

- **瞳孔恐惧涣散**: 瞳孔轻微扩散，视线无法凝聚，像是在回避某种不敢直视的处境。
- **眼睑高频颤动**: 下眼睑高频颤动，是强行压住情绪的本能反应。
- **闭眼滞停**: 角色忽然闭上眼，停留一秒，像在把情绪压回身体里。
- **情绪转平静**: 缓缓吐出一口长气，嘴唇慢慢松开，重心沉下来，眼神从慌乱变成疲惫平静。
- **轻蔑冷笑**: 嘴角缓慢地、不对称地向一侧挑起，笑意不过眼底，眼神依旧锐利。
- **扬起下巴斜睨**: 下巴扬起，目光向下斜睨前方，带轻微俯视感。
- **冷哼鼻息**: 发出一声极轻极冷的鼻息，幅度小但态度明确。
- **情绪转坚定**: 视线向下垂落，随后聚焦在眼前某一点，睫毛停止颤动，再抬眼时眼神变成一种沉静的炽热。

### Surprise, Shyness, and Soft Vulnerability

- **惊讶**: 呼吸骤然一屏，眼睛微微圆睁，瞳孔轻轻扩散。
- **眼神柔弯**: 眼睛瞬间柔弯，一抹压抑不住的欢喜从眼底深处暖暖漾开。
- **羞怯含羞**: 忍不住抬起眼，又含蓄地直接望向镜头或对方，嘴角不受控制地上翘。
- **脸红**: 两颊飞起淡淡霞色。
- **压笑成浅笑**: 拼命想把笑意往下压，最终却藏成一个羞怯、甜中带怯的浅笑，下巴微微内收。
- **被发现心事的娇羞**: 眼神偷偷从镜头上弹开，左右飘忽，不敢看对方，颧骨微红，耳根与脖颈因极度害羞泛起潮红。
- **抿唇咽口水**: 嘴唇紧张抿住，喉间极轻地滚动一下，头微微低垂。
- **羞怯抬头**: 怯怯地再次抬眼，给出柔软而温热的直视，睫毛轻颤，鼻翼微微翕动。

### Calculation, Cruelty, and Dark Resolve

- **笑意褪去**: 笑意从脸上一丝丝抽走，上扬嘴角慢慢拉平，眼里的笑意好像被污水淹没。
- **审视盘算**: 目光聚焦，带着审视与盘算，像在估量对方的利用价值。
- **眼神变阴厉**: 眼神骤然变得阴厉，瞳孔微微收缩，眉头轻压，眉尾挑起不易察觉的弧度。
- **嘴角阴冷勾起**: 嘴角不再平坦，而是向一侧缓慢、极细微地勾起，不是笑，而是一种阴冷的了然。
- **本性毕露**: 整张脸如同面具剥离，露出冷硬骨骼感。
- **眼神凶狠**: 双眼如鹰隼般半眯，眼白在强光下透着冷光，目光像刀一样直刺过来。
- **面部绷紧**: 面颊肌肉绷紧，下颌轻咬合，额头青筋隐隐跳动。
- **阴毒**: 阴毒与恨意从眼底慢慢涌出，眼白泛起淡淡血色，目光像毒蛇亮出尖牙，牢牢锁住对方。

### Tenderness, Disguise, and Controlled Performance

- **宠溺**: 直视镜头，目光缱绻而专注，像在看极珍视的人；眼中没有防备，嘴角带着一缕极淡、跟随融化的笑意。
- **笑意抽离**: 眼睛忽然轻轻一凝，眼底深处有什么东西被悄然抽走，瞳孔极其细微地收缩；目光从绵软缓缓变得沉稳、沉黑，笑意仍浮在表面。
- **伪装剥落**: 眼神向下微微一沉，再抬起时眼中已无半点温度，只剩精光内敛的审视；嘴角笑意缓慢地、一点点地抹平。
- **阴冷笑起**: 嘴角仅挑起一侧，弧度阴冷而刻薄，像冷刃在唇边绽开；眼脸微微眯起，眼神彻底下沉。
- **本性暴露**: 微微抬了抬下巴，眼底残存的玩味与轻蔑被无限放大。整张脸全然陌生，画面定格。

### Timing Guidance

- 0.25-0.5s: tiny flashes such as nostril breath, jaw tightening, eye flick, smile twitch.
- 0.5-1.0s: gaze change, blink hold, tear forming, mouth tightening, chin lift.
- 1.0-1.5s: full emotional transition such as smile fading, forced calm, shy glance returning.
- 1.5-2.0s: complex mask shift such as tenderness turning into calculation or smile becoming cruelty.

Always preserve natural transition: no sudden expression jumps, no exaggerated crying, no theatrical grimacing unless the story demands it.

## Emotion-to-Micro-Expression Map

When the user names an abstract emotion, translate it into visible beats. Choose 3-5 beats that fit the character, scene, and duration. Do not use every beat.

### 悲伤 / Grief

- Eyes lose focus before tears appear.
- Lower eyelids tremble; blinking slows.
- Lips press into a thin line, then soften.
- Breath becomes shallow; shoulders slightly collapse.
- Tears gather at lower lashes, then one tear falls only if the scene needs visible release.

Typical phrase:

```text
眼神先失焦，随后下眼睑细微颤动；嘴唇慢慢抿住，呼吸变浅，泪水悬在下睫毛处却迟迟不落。
```

### 震惊 / Shock

- Breath stops for a beat.
- Eyes widen slightly, then freeze.
- Pupils subtly dilate.
- Jaw loosens or locks.
- Hands stop mid-action.

Typical phrase:

```text
她的呼吸骤然停住，手停在半空，眼睛微微睁大后彻底僵住，瞳孔轻微扩散，像还没有理解这句话。
```

### 强忍哭泣 / Suppressed Crying

- Gaze drops to avoid being seen.
- Lips press hard, mouth corners pull down.
- Throat swallows once.
- Nose and breath tremble silently.
- Hand covers mouth only when the character is trying to hide sound.

Typical phrase:

```text
他迅速低下头，嘴唇死死抿住，喉结艰难滚动一次，鼻息破碎地颤了一下，却没有发出哭声。
```

### 愤怒克制 / Restrained Anger

- Stare becomes still and sharp.
- Jaw hardens; molars press.
- Nostrils flare slightly.
- Blink rate drops.
- Fingers tighten on object or fabric.

Typical phrase:

```text
他的目光突然静下来，眨眼变少，下颌线绷紧，鼻翼轻轻扩张，手指无声扣紧杯沿。
```

### 悔恨 / Regret

- Eyes avoid the other person's face.
- Brow folds inward, not upward.
- Mouth opens slightly but words fail.
- Chin lowers; body folds inward.
- Hand reaches halfway, then stops.

Typical phrase:

```text
他看向对方又迅速移开视线，眉心向内收紧，嘴唇张开却说不出话，伸出的手停在半空。
```

### 愧疚 / Guilt

- Eyes flick down and sideways.
- Blink becomes slow and heavy.
- Lips tighten asymmetrically.
- Shoulder or neck withdraws slightly.
- Voice lowers or pauses before key words.

Typical phrase:

```text
她的视线向下躲开，眨眼变慢，嘴角不对称地绷住，肩膀轻轻缩回，像不敢承受对方的目光。
```

### 羞耻 / Shame

- Head lowers more than gaze.
- Ears, neck, or cheeks redden if visually appropriate.
- Mouth becomes small and controlled.
- Eyes cannot hold contact.
- Body turns slightly away.

Typical phrase:

```text
她低下头，眼睛不敢停在对方脸上，耳根和脖颈慢慢泛红，嘴唇收紧成很小的线。
```

### 羞怯 / Shyness

- Gaze lifts briefly, then escapes.
- Lips press, then a tiny smile leaks out.
- Eyelashes tremble.
- Fingers touch sleeve, cup, hair, or another small object.
- Breath lightens.

Typical phrase:

```text
她怯怯抬眼看了一瞬又移开，睫毛轻颤，嘴角压不住地漏出一点笑意，手指无意识捏住袖口。
```

### 爱意克制 / Restrained Love

- Eyes soften before the mouth moves.
- Gaze lingers half a beat too long.
- Smile almost appears, then is contained.
- Breath steadies near the person.
- Hand moves toward contact, then stops.

Typical phrase:

```text
他的眼神先软下来，目光在她脸上多停了半秒，嘴角几乎要抬起又被压住，伸出的手停在距离她很近的位置。
```

### 嫉妒 / Jealousy

- Gaze fixes on the rival/object first, not the loved person.
- Mouth corners tighten.
- Smile becomes thin or delayed.
- Eyes return to the loved person with controlled sharpness.
- Fingers make a small possessive motion.

Typical phrase:

```text
她先看向那只搭在对方手臂上的手，嘴角轻轻收紧，随后才抬眼看他，笑意很薄，眼神却变得锋利。
```

### 失望 / Disappointment

- Gaze lowers slowly, not suddenly.
- Tiny exhale through nose.
- Mouth corners fall with exhaustion.
- Shoulders lose structure.
- Eyes stop searching for explanation.

Typical phrase:

```text
她的目光慢慢垂下，鼻息很轻地泄出一口气，嘴角疲惫地落下，眼神不再追问。
```

### 释然 / Relief or Release

- Long exhale.
- Jaw and brow release.
- Eyes moisten but calm down.
- Shoulders drop slightly.
- Small smile appears only after the tension leaves.

Typical phrase:

```text
他缓慢吐出一口长气，下颌和眉心终于松开，眼眶仍湿，却不再紧绷，肩膀轻轻落下。
```

### 决绝 / Resolve

- Breath stops, then steadies.
- Eyes lock on a target.
- Chin lifts slightly.
- Blink stops for a beat.
- Hand completes a decisive action.

Typical phrase:

```text
她先屏住呼吸，随后眼神锁定前方，下巴轻轻抬起，眨眼停止一拍，手上的动作终于落定。
```

### 麻木 / Numbness

- Face becomes quiet, almost too still.
- Eyes stay open but unfocused.
- Mouth relaxes without expression.
- Reaction is delayed.
- Voice, if any, is flat and low.

Typical phrase:

```text
他的脸安静得近乎空白，眼睛睁着却没有焦点，嘴唇松开，所有反应都慢了半拍。
```

### 恐惧 / Fear

- Listening precedes looking.
- Pupils dilate; eyes widen but avoid full scream expression.
- Breath becomes shallow.
- Lips part slightly.
- Fingers grip clothing, doorframe, phone, or flashlight.

Typical phrase:

```text
她先停住侧耳听，随后眼睛轻轻睁大，瞳孔扩散，嘴唇微微分开，手指无声抓紧衣角。
```

### 复仇 / Revenge Resolve

- Expression becomes calm, not wild.
- Tears or pain recede behind still eyes.
- Mouth corners flatten.
- Gaze sharpens on the target.
- Body becomes more upright.

Typical phrase:

```text
她眼底的泪意慢慢退到更深处，嘴角拉平，目光重新聚焦，身体一点点站直，脸上只剩冷静的决意。
```

### 阴冷 / Cold Cruelty

- Smile stays on mouth only, not eyes.
- Eyes narrow slightly.
- Mouth corner lifts asymmetrically.
- Head tilts or chin lifts minimally.
- Voice, if any, is soft rather than loud.

Typical phrase:

```text
他的嘴角只向一侧极轻地挑起，笑意不到眼底，眼睛微微眯起，下巴抬了一点，声音反而更轻。
```

### 喜悦克制 / Restrained Joy

- Eyes brighten first.
- Lips press to hide smile.
- Smile leaks through one corner.
- Breath catches lightly.
- Body leans forward a fraction.

Typical phrase:

```text
她的眼睛先亮了一下，随后立刻抿住嘴，笑意还是从一侧嘴角漏出来，身体不自觉向前倾了半寸。
```

### 尴尬 / Awkwardness

- Smile freezes too long.
- Eyes flick sideways seeking escape.
- Throat swallow or dry laugh.
- Hand performs useless small action.
- Silence becomes the joke.

Typical phrase:

```text
他的职业假笑僵在脸上，眼神飞快向旁边求救，喉结滚动一下，手指徒劳地按灭手机。
```

## Sound Design Library

Sound should shape emotion and structure. Prefer concrete diegetic sound over generic music. Use silence actively. In short video prompts, 2-4 sound anchors are usually enough.

### General Sound Rules

- Default to no background music unless the user explicitly asks for music or the scene specifically requires source music. Write `无配乐/不要背景音乐，只保留必要台词人声、环境声、动作音效和物体声`.
- Keep sound grounded in the scene: dialogue/voice, breath, footsteps, cloth, props, impacts, machinery, room tone, weather, crowd texture, and environmental sound.
- Avoid generic score words such as `dramatic music`, `epic BGM`, `sad piano`, or `tense soundtrack` unless music is explicitly requested.
- Use sound to mark turns: a phone vibration, cup click, door lock, monitor beep, thunder, or engine start can carry the story beat.
- Let key dialogue breathe. Do not bury it under music or loud ambience.
- Use sound reduction when shock happens: environment becomes muffled, then one small sound becomes sharp.
- Use sound tail for endings: rain continues, engine fades, room tone returns, music box stops, breath remains.
- Avoid generic phrases like `dramatic music`. If music is needed, describe its role: low cello drone, distant radio song, muted festival TV, single sustained note.
- If no music fits, explicitly say `无配乐，只保留环境声`.

### Hospital / Medical Corridor

Use for death notices, waiting, diagnosis, restrained grief.

- Fluorescent light buzz.
- Distant heart monitor beep or low equipment hum.
- Rubber soles on polished floor.
- Wheelchair wheel squeak.
- Curtain rail or metal tray sound.
- Air conditioner low drone.
- Sound can become muffled after bad news, leaving only breath and a single monitor beep.

Typical phrase:

```text
环境声只有医院空调低鸣、远处心电监护仪规律滴声、护士鞋底掠过地面的轻响；噩耗落下后，走廊声场瞬间发闷，只剩他的呼吸。
```

### Rainy Night / Car Interior

Use for breakup, confession, pressure, loneliness.

- Rain tapping windshield and roof.
- Wiper rubber scraping glass.
- Engine idle low vibration.
- Turn signal tick or hazard light click.
- Distant traffic softened by rain.
- Phone notification or seatbelt friction.
- Sudden silence after engine shuts off.

Typical phrase:

```text
声音以雨刷刮过挡风玻璃的低哑摩擦声为节拍，发动机怠速在车厢里低频震动，台词间隙只剩雨水敲打车顶。
```

### Home / Apartment at Night

Use for phone calls, grief, suspense, isolation.

- Refrigerator hum.
- Phone speaker hiss or vibration on wood.
- Neighbor footsteps through wall.
- Elevator or hallway sound far away.
- Clock tick if the scene needs time pressure.
- Fabric rustle, bare feet on floor.
- Room tone becoming empty after bad news.

Typical phrase:

```text
电话里的声音带着轻微电流底噪，房间里只有冰箱低频声和远处电梯运行声；挂断后，空间忽然空下来，只剩她压在掌心里的破碎鼻息。
```

### Kitchen / Domestic Intimacy

Use for awkward intimacy, family tension, quiet breakup.

- Coffee machine drip.
- Ceramic cup click.
- Water pipe hum.
- Chopsticks touching bowl.
- Knife against cutting board.
- Refrigerator door seal opening.
- Food steam and small tableware sounds can replace music.

Typical phrase:

```text
无配乐，只有咖啡机一滴一滴落下、陶瓷杯轻碰台面的细响，以及两人刻意压轻的呼吸。
```

### Old Room / Memory Object

Use for nostalgia, memory, identity, past/present montage.

- Music box mechanical winding.
- Paper, photo, or cloth friction.
- Dusty drawer creak.
- Floorboard soft groan.
- Distant childhood laughter as memory texture, not literal crowd noise.
- Sound distortion to enter memory; clean room tone to return.

Typical phrase:

```text
发条干涩地咔哒转动，音乐盒旋律断断续续响起，随后混入极远的儿童笑声；回到现实时旋律卡住，只剩房间空调低鸣。
```

### Train Station / Public Waiting Space

Use for reunion, departure, missed chances.

- Distant broadcast with indistinct words.
- Suitcase wheels on concrete.
- Train rail wind.
- Fluorescent buzz or station light flicker.
- Footsteps echo in a large empty space.
- Coat fabric in wind.

Typical phrase:

```text
旧行李箱轮子在水泥地上拖出空旷回声，远处广播含糊不清，铁轨风穿过站台，把两人的沉默拉得很长。
```

### Office / Elevator / Light Comedy

Use for social embarrassment and timing jokes.

- Elevator ding.
- Fluorescent office hum.
- Phone speaker playback.
- Keyboard clacks.
- Coffee lid click.
- Awkward silence after a line.
- One small sound after silence can become the punchline.

Typical phrase:

```text
手机外放的录音在电梯里显得干硬刺耳，话音落下后所有人安静半秒，只剩电梯提示音叮的一声。
```

### Palace / Period Drama Interior

Use for ancient costume grief, power, restraint.

- Candle flame flicker.
- Distant night watch drum or bell.
- Silk sleeve friction.
- Hairpin or bead ornament tiny sound.
- Footsteps behind screen.
- Paper decree unfolded.
- Silence should feel ritualized and oppressive.

Typical phrase:

```text
无配乐，只保留烛火轻响、远处更鼓和衣袖摩擦声；传话结束后，偏殿安静得像被规矩压住。
```

### Disaster / Large Crowd

Use for crowd pressure, panic, public crisis.

- Alarm siren.
- Emergency broadcast.
- Metal groan.
- Glass or tableware sliding and breaking.
- Crowd shouts as a texture, not a muddy wall.
- One named character's voice must cut through the crowd.
- Let the crowd drop out briefly when the protagonist sees the key person/object.

Typical phrase:

```text
警报和广播交叠，金属船体发出低沉扭曲声，盘子沿倾斜地面滑落摔碎；当母亲看见孩子时，人群声短暂发闷，只剩她的呼吸和舱门警报。
```

### Product / Car / Premium Object

Use for brand-like texture without becoming an ad.

- Door close with weight and resonance.
- Engine ignition sequence.
- Leather seat friction.
- Paper folding or pen scratch.
- Tire on gravel.
- Watch crown click, metal bracelet shift, camera shutter, depending on object.
- Sound should feel precise, tactile, restrained.

Typical phrase:

```text
车门关闭声厚重而干净，外界风声被瞬间切断；点火时机械启动声由短促转为稳定低吼，皮革座椅发出细微摩擦。
```

### Suspense Without Monster

Use for fear from space and implication.

- Door lock click.
- Phone vibration in another room.
- Floorboard creak.
- Refrigerator hum.
- Elevator far away.
- Breath becomes too loud.
- Do not use loud sting unless the user wants jump scare.

Typical phrase:

```text
门锁落下后楼道声被切断，屋里只剩冰箱低频声；卧室深处忽然传来极轻的手机震动，嗡的一声后又停住。
```

### Wuxia / Action

Use carefully; current action rules need more reference refinement.

- Rain on bamboo leaves.
- Cloth sleeve cutting air.
- Metal clash with clear contact.
- Footsteps splashing water or landing on wood.
- Sheath friction before blade appears.
- Thunder delayed after lightning.
- Avoid muddy continuous clanging; make each weapon sound correspond to one clear action.

Typical phrase:

```text
雨打竹叶声铺满背景，每一次金属碰撞都对应清晰接触点；剑锋出鞘半寸时只有一声干净鞘响，雷声延迟半秒炸开。
```

## Fight Choreography Prompt Pattern

Use this for staged combat, close-quarters fighting, underground ring scenes, wuxia exchanges, or short action beats where the physical sequence must remain readable. The goal is not literary intensity, but clear attack-defense-counter choreography.

### Core Principles

- Keep the number of active fighters small. For a 10-15s clip, 1v1 is safest; 1v2 or 1v3 needs much simpler beats.
- Define each fighter's identity, outfit, body type, fighting attitude, and visual anchor before the action.
- Write action as a timed chain: attack line -> perception/reaction -> defense/evasion -> counter -> impact/recovery.
- Specify body orientation and footwork: step back, side slip, lower stance, lateral step, pivot, twist, sprawl, level change.
- Specify contact points: forearm block, palm parry, elbow cover, knee to midline, shoulder check, grip at waist, controlled throw.
- Show weight and physics: lowered center of gravity, torso rotation, braced feet, transferred momentum, dust burst, floor impact.
- Camera should respond to the action: handheld follow, low-angle tracking, short shake on near impact, tilt up during lift, snap tilt down on landing.
- Surrounding crowd should be background pressure only, not extra fighters unless the user asks.
- Keep safety and taste clear: staged, non-lethal, no gore, no real injury emphasis.

### Recommended Structure

```text
时长：
画幅比例：
类型：

角色参考：
角色A：...
角色B：...

整体风格：
地点、地面材质、光源、人群位置、摄影风格、动作质感、安全边界。

SHOT 1（00:00-00:05）
Subject:
两名角色的站位、距离、周围环境。

Action:
-00:01：攻击方做出明确攻击，写清攻击路线和目标。
-00:02：防守方捕捉路线，写清闪避方向、重心变化。
-00:03：防守方格挡/拨开/反制，写清接触点。
-00:05：对手调整防线或人群反应，形成下一镜头动机。

Environment:
地面、障碍物、人群、灰尘、可破坏物。

Camera:
机位、焦段、跟随方式、何时震动/上仰/下摇。

Style:
速度、重量、真实感、类型片质感。

Constraints:
角色一致性、围观者不冲入、无血腥、无真实伤害。
```

### Useful Action Verbs

- attack: 后手直拳刺出, 横踢扫向肋部, 顶膝攻击中线, 低扫小腿, 肘击压进, 刀线横切, 剑锋斜挑
- evade: 微后撤, 侧闪, 下潜, 俯身切入, 后仰避开, 横移出拳线, 转髋卸力
- defend: 横向掌板格开, 前臂格挡, 收肘下压, 双臂护头, 肩膀顶住, 剑鞘横挡, 刀背压住
- counter: 顺势抢进内线, 反手扣腕, 鞘尾击腕, 肩撞破开, 抱腰锁住, 借前冲力量抛摔
- impact: 木板炸开灰尘, 脚步在水泥地刹出灰痕, 围观者惊呼后退半步, 金属声短促清脆

### Camera for Fight Scenes

- 24mm wide handheld for close pressure and spatial clarity.
- 35mm medium handheld for readable body movement.
- Low-angle tracking for level changes, knees, throws, and forward drives.
- Short shake only when fist, weapon, or body passes close to camera.
- Tilt up when a body is lifted; fast tilt down or snap pan on controlled landing.
- Avoid excessive blur. Action should be fast but readable.

### Fight Scene Cinematography Rhythm

Use action-film camera techniques to create immediacy, but apply them at specific beats. Do not make the whole scene shaky or tilted.

**Handheld physical shake**

- Use light handheld breathing throughout close combat for realism.
- Use short, sharp shake only on impact beats: punch lands, weapon clash, body hits table, door slams, foot lands after jump.
- Avoid continuous violent shake; it hides choreography.

Useful phrase:

```text
手持摄影带轻微物理呼吸感，击中瞬间产生短促震动，随后迅速稳住，让动作接触点保持清晰。
```

**Dutch angle / 荷兰角**

- Use for imbalance, panic, losing footing, being surrounded, or a power shift.
- Best in brief shots, not as the default framing.
- Works well before a reversal: the frame tilts as the defender loses balance, then returns level when they regain control.

Useful phrase:

```text
镜头短暂转为轻微荷兰角，强化角色失衡和空间压迫；反击成功后构图重新回正。
```

**Overcranking / 升格慢动作**

- Use for one key moment only: flying kick, weapon crossing near the face, body lifted, glass/wood dust exploding, a decisive dodge.
- Keep the setup and recovery at normal speed, so the slow motion feels earned.
- Pair slow motion with clear sound change: impact sound drops low, breath or cloth movement becomes sharp, then real-time sound snaps back.

Useful phrase:

```text
关键击中瞬间进入短暂升格慢动作，灰尘和衣料在逆光中展开；落地后立刻回到实时速度，声音猛地恢复。
```

**Speed ramp / 快慢结合**

- Good rhythm: real-time rush -> brief slow-motion impact -> snap back to fast recovery.
- Use for sprint-then-kick, dodge-then-counter, leap-then-land, throw-then-ground impact.
- Do not speed-ramp every action; choose the emotional or physical peak.

Useful phrase:

```text
动作节奏采用快慢结合：助跑与抢进保持实时高速，击中瞬间短暂升格，落地和反应立即切回实时速度。
```

**Special composition**

- Diagonal composition: useful for protector and protected character, two fighters facing off, or long weapon lines.
- Foreground obstruction: use pillars, door frames, hanging cloth, railings, classroom desks to add depth and danger.
- Low-angle wide shot: useful for heroic entrance, spear sweep, shield charge, or surrounded protagonist.
- Top shot or high angle: use sparingly for geography in crowd fights.

### Fight Rhythm Planning

A strong 10-15s fight should usually have a rhythm arc:

```text
0-3s：建立站位与第一击，实时速度，空间清楚。
3-7s：连续攻防，手持近身，短促震动，动作接触点明确。
7-10s：短暂停顿或失衡，荷兰角/呼吸/对视制造节奏变化。
10-13s：爆发动作，冲刺、腾空、摔投或武器反击。
13-15s：升格冲击后回到实时，留半秒到一秒余韵。
```

For 30s split into two 15s prompts:

- Segment 1: pressure, first exchange, incomplete reversal, tail-frame danger.
- Segment 2: continuation from tail frame, tactical reversal, finishing impact, aftermath.

### Safety and Negative Constraints

Use explicit constraints:

```text
电影特技打斗，非致命，无血腥，无真实伤害；保持角色脸部、发色、服装一致；不要肢体穿模，不要多余手脚，不要武器变形，不要动作方向混乱；围观者只作为背景反应，不冲入打斗。
```

### Common Failure Fixes

- If the fight becomes chaotic, reduce active actions to 2-3 clear exchanges.
- If bodies deform, reduce grappling complexity and avoid simultaneous limb-heavy actions.
- If spatial direction is unclear, anchor the fighters: `A在画面左侧，B在画面右侧`, then maintain screen direction.
- If impact lacks weight, add stance, momentum transfer, floor reaction, dust, cloth movement, and a short camera shake.
- If the crowd distracts, describe them as dark silhouettes forming a fixed semicircle.

## Tavern Brawl / Environmental Fight Pattern

Use this for messy but readable fights in taverns, inns, warehouses, gambling rooms, markets, docks, alleys, or any place where the environment is part of the choreography. This pattern differs from clean ring combat: the scene should use furniture, bottles, pillars, stairs, railings, walls, lamps, dust, and bystanders as action texture.

### Environmental Action Logic

- Start each beat with a clear spatial anchor: who is near the table, pillar, stairs, counter, door, wall, or crowd.
- Make the environment react to impact: table legs scrape, stool flips, wine jars shatter, dust bursts, wooden planks crack, lamps swing, crowd backs away.
- Use objects as temporary obstacles, shields, or impact surfaces, not random decoration.
- Keep one active action per beat. If a fighter kicks a stool, the stool's path and effect should be clear.
- Write the cause-and-effect chain: body movement -> object contact -> object reaction -> opponent reaction -> camera reaction.
- Use short environmental aftermath to sell weight: broken wood settles, liquid spreads, dust hangs in light, bystanders freeze or step back.

### Body and Object Contact Points

Useful contact points:

- palm hits table edge
- shoulder drives opponent into pillar
- boot hooks stool leg
- elbow knocks wine jar aside
- forearm blocks bottle swing
- knee pins opponent against table
- back slams into wooden wall
- hand grabs collar or belt before throw
- opponent rolls across tabletop and knocks bowls aside

Typical phrase:

```text
他右肩压低撞进对手胸口，对手后背重重撞上木柱，柱上的油灯剧烈晃动，桌边酒碗被震得跳起半寸，镜头跟着冲击短促一震。
```

### Camera Switching for Environmental Fights

- Establishing shot first: show room layout, fighters, crowd, tables, door, stairs, or counter.
- Medium handheld tracking for body movement through space.
- Low-angle close shot for kicks, stool sweeps, feet sliding, and floor impact.
- Over-shoulder shot for an incoming object or surprise attack.
- Fast pan or whip pan only when following a thrown body/object; keep the landing clear.
- Short impact shake on collision with table, pillar, wall, or floor.
- Cut to close-up of object reaction only if it helps clarity: cracking tabletop, spinning bottle, dust burst, blade or fist stopping short.
- After a big impact, hold half a beat so the viewer understands the result before the next attack.

### Shot Beat Template

```text
SHOT X（00:00-00:04）
Subject:
A在木桌左侧，B在柜台前，围观者贴墙后退，桌椅形成狭窄通道。

Action:
-00:01：A侧身避开B挥来的酒坛，酒坛擦过肩侧砸上木柱。
-00:02：A左手按住桌沿，右脚勾起地上的木凳踢向B膝前，迫使B后撤。
-00:03：B抬臂挡开木凳，碎木和灰尘飞起；A借遮挡抢进半步，用肩膀顶向B胸口。
-00:04：B后背撞上柜台，柜台上的酒碗连串震落，围观者惊呼散开。

Camera:
手持中景横移跟拍，木凳飞过镜头前方时短促模糊；撞上柜台瞬间镜头轻震，随后停半拍确认结果。
```

### Tavern Brawl Negative Constraints

```text
不要人群冲入打斗，不要道具随机漂浮，不要桌椅位置跳变，不要动作穿模，不要多余肢体，不要过度动态模糊，不要血腥伤害。
```

### Suppression Burst -> Dead Pause -> Finishing Stunt Rhythm

Use this pattern for an intense staged fight where one character overwhelms another, then the scene breathes for a moment before a final cinematic stunt impact. Best for abandoned classroom, warehouse, underground ring, hallway, locker room, train carriage, or other confined spaces with breakable environment.

This pattern is different from exchange-based choreography. It has three dramatic phases:

1. **压制连击 / Suppression burst**: one fighter pins or restricts the other and delivers rapid close-range stunt strikes.
2. **死寂停顿 / Dead pause**: the aggressor releases, steps back, both breathe, and the space becomes tense.
3. **终结式特技冲击 / Finishing stunt impact**: the aggressor sprints, jumps, kicks, throws, tackles, or slams the opponent into a controlled breakaway environment.

Recommended structure:

```text
镜头一（00:00-00:05）
主体：A在画面左侧，B在画面右侧，B被压制在{家具/墙面/擂台边/车厢座椅}前。
动作：
00:00-00:01：A用{手/前臂/衣领抓握/肩膀顶压}限制B的移动。
00:01-00:04：A连续打出近距离快速电影特技拳击/肘击/膝击；B后仰、防守、承受冲击，身体被环境限制。
00:04-00:05：连击节奏达到顶点，镜头随每次击打产生短促震动。
摄影机：中景手持，机位基本固定，每次打击短促剧烈震动，可使用轻微鱼眼暗角制造幽闭压迫。

镜头二（00:05-00:08）
主体：A松开B，B靠在即将倒塌的支撑物旁。
动作：
00:05-00:06：A后退半步或一步，双臂下垂，急促喘息，眼神仍锁定B。
00:06-00:08：B失去支撑，靠住{椅背/墙面/栏杆/桌沿}，神情涣散但仍努力站立。
摄影机：中景轻微拉远，手持微动，节奏从剧烈转为压抑停顿。

镜头三（00:08-00:15）
主体：A从一侧快速冲刺，B在破败环境前摇晃站立。
动作：
00:08-00:10：A突然助跑，头发、衣摆、外套随动作扬起。
00:10-00:12：A腾空跃起或爆发前冲，做出高位特技飞踢/肩撞/膝撞/过肩摔，攻击目标为上胸、肩部、躯干等非致命区域；动作可进入明显慢镜头。
00:12-00:13：击中瞬间摄影机几乎定格，环境道具爆裂倒塌，木屑、灰尘、碎片在逆光中扬起；B以受控特技动作向后倒飞或摔落。
00:13-00:15：B落地后昏沉失力但仍存活，A落地停在前景急促喘息，最终画面停在一片狼藉的全景。
摄影机：全景快速平移跟随助跑；飞踢或撞击瞬间切入动作特写和慢动作；随后镜头下摇或横移跟随倒飞/落地，最终停在环境破坏后的全景。
```

Key writing points:

- Make the initial restriction clear: collar grip, shoulder pin, forearm press, wall pin, chair/table limit, cage edge.
- Rapid strikes should remain staged and non-lethal. Avoid detailed gore; use impact, breath, recoil, furniture vibration, dust.
- The pause is essential. It gives the viewer time to feel the previous impact and prepares the final burst.
- The finishing stunt should target non-lethal areas such as upper chest, shoulder, torso, midline, or controlled side impact.
- Environmental breakaway must be readable: stacked desks, broken chairs, wooden crates, cardboard boxes, padded railing, breakaway wall panels.
- Use lighting particles to sell impact: dust in side backlight, wood chips in cold light, fabric and hair movement.
- Keep identities stable during fast movement: repeat hair color, hairstyle, clothing, and visual anchors in every shot.

Useful style phrases:

- `压迫、暴烈、幽闭，冷灰蓝色调，高频打击震动`
- `爆发前的短暂死寂，窒息般的对峙感`
- `高冲击电影动作特技，强烈光影反差，高潮后归于残酷死寂`
- `鱼眼镜头暗角与轻微畸变，手持摄影的物理震动感`
- `百叶窗强烈侧逆光，光柱中漂浮灰尘颗粒`

Safety constraints for this rhythm:

```text
仅表现电影特技打斗，非致命，无血腥、无死亡、无骨折、无颈部折断、无开放伤口、无明确重伤；角色落地为受控特技动作，仍然存活；保持角色脸部、发色、身材、服装一致。
```

### Epic Crowd Fight / Protector Entrance

Use this pattern for cinematic crowd fights where a central character is surrounded and a protector or hero enters to break the siege: palace coups, throne hall sieges, bodyguard rescues, battlefield entrances, gang encirclement, spear/sword heroics, and multi-segment continuation using previous final frames.

This pattern is about action staging, character hierarchy, continuity, and camera movement. Do not force a 3D animation style unless the user explicitly requests it.

Core cinematic intent:

```text
电影感史诗群战，主角被层层包围，护卫/将军/英雄作为动作锚点强势入场，利用长兵器横扫、飞踢、冲刺、慢动作冲击和高速跟拍打破围困。画面强调人物站位、群体压力、角色连续性、空间层级和强烈冲击感。
```

Continuity rules:

- Preserve the same visual style across all segments, but let the style follow the user's requested medium: live-action cinematic, realistic period drama, stylized fantasy, 3D animation, etc.
- State that character faces, costumes, hairstyles, weapons, soldier designs, and location remain consistent with previous segment/reference material.
- If continuing, start with `生成上个视频最后一帧画面衔接后续剧情` or `开头延续上一条尾帧`.
- Use material references explicitly when present, e.g. `公主和古代士兵们站位参考素材1`, `上个视频最后一帧参考素材2`.
- Keep the location name consistent, such as `金銮殿`, `废弃教室`, `地下擂台`, `宫门台阶`, or the user's exact scene label.

Recommended segment structures:

**1. Encirclement setup, 5-8s**

```text
画面一：低角度侧面跟拍核心人物走向权力中心或空间中心，镜头缓慢上移推进到侧脸特写；人物眼神一横，单臂发力甩袖/拔剑/抬手，衣袍或武器在空中划出巨大弧度。动作同步瞬间镜头拉远至全景，核心人物被士兵/敌人近距离团团围住。
画面二：切到多位敌人面部近景，敌人高举武器准备进攻，齐声怒喝关键台词。禁止背景音乐，仅保留环境音效和人声，禁止字幕。
```

**2. Protector entrance and crowd fight, 12-15s**

```text
画面一：保护者从高处落下或从人群外高速切入，落在被保护者正前方，挥动长枪/长刀/剑鞘/盾牌横扫重击击倒前排数名敌人；如有台词，语气冰冷狠厉。随后切到对角线构图，左右分别为保护者与被保护者面部特写，表情贴合身份。
画面二：镜头紧跟保护者继续在人群中打斗，长兵器横扫、短促飞踢、肩撞、转身回击，多段分镜切换，环绕高速跟拍、慢动作、面部特写、高速摄影跟拍交替使用。敌人密集簇拥、层层包围，保护者重击多个敌人，动作一气呵成，画面冲击力强。
```

**3. Tail-frame continuation, 5-8s**

```text
画面一：生成上个视频最后一帧画面衔接后续剧情，镜头拉远到中远景，保护者与被保护者相互靠近或并肩站立，合力御敌。无台词，仅生成打斗音效和环境音效，不配背景音乐，禁止字幕。
```

Action design rules:

- For mass fights, do not ask every enemy to perform unique actions. Use `前排数名敌人`, `叛军层层包围`, `敌人密集簇拥`, and keep one hero action as the visual anchor.
- Hero action can be heightened but should match the requested tone: falling from above, spear sweep, flying kick, shield charge, high-speed tracking, slow motion impact.
- Maintain readable hierarchy: protected character as emotional center, protector as action anchor, soldiers/enemies as surrounding pressure.
- Combine fast action with one or two hero close-ups to preserve character emotion and identity.
- If the scene is very crowded, use wide shots for geography and close-ups for identity, not medium shots full of indistinct bodies.

Sound and text constraints:

```text
禁止配背景音乐，仅生成打斗音效、环境音效、怒喝声、兵器碰撞声、脚步声、衣袍破风声。禁止画面生成字幕。
```

Negative constraints:

```text
保持角色外貌、服装、发型、武器和敌方造型一致，不要风格漂移，不要字幕水印，不要角色脸部变形，不要服装发型跳变，不要敌人数量失控导致主体丢失，不要武器变形，不要动作穿模。
```

## Dialogue and Offscreen Lines

When dialogue carries the plot turn, write the actual line. Avoid vague placeholders.

- Phone call: include the caller's key sentence, even if muffled or offscreen.
- Doctor, police, family notice: include the exact notice line in plain speech.
- Inner monologue or voiceover: mark it as `内心OS` or `画外音`, and place it on the time axis.
- Keep lines short enough for the shot duration.

Examples:

```text
电话中传来压低的男声："I'm sorry... there was a crash. He didn't make it."
医生摘下口罩，低声说："我们尽力了，但她没能撑过来。"
```

## Light and Atmosphere

Make atmosphere physical:

- Moving streetlight stripes across a face.
- Wind lifting hair, paper, grass, shirt collar, dust.
- Window reflections splitting the face.
- Hard light cutting through blinds.
- Cold interior shadow versus warm exterior light.
- Engine vibration, cloth friction, footsteps on wood, room tone, breath, sudden silence.

Prefer dynamic light over static adjectives. Say what the light does to the face, object, or space.

## Structure Selection

Choose structure before writing shot details. Always state the chosen structure in the diagnosis, and explain the reason in one sentence. If more than one structure fits, choose one primary structure and one secondary support.

### Structure Selection Table

| Structure | Use When | Best For | Avoid When | Prompt Strategy |
|---|---|---|---|---|
| **单场景一镜到底 / Single Take** | One space, one continuous emotional shift, few actions, no major time jump | restrained grief, confrontation pause, ritual, waiting, subtle intimacy | many locations, action complexity, multiple plot turns | Use one camera path, simple blocking, strong micro-reactions, sound continuity |
| **单场景连续剪辑 / Multi-Shot Sequence** | One location but several physical beats or reaction angles are needed | kitchen tension, hospital corridor, car interior conflict, interrogation | very abstract memory, large time span | Use 3-5 shots: establish space, key object/action, face reaction, ending breath |
| **跳剪压缩 / Jump Cuts** | Time needs compression while staying in one emotional thread | preparation, decision, panic escalation, ritual, product/person process | scene requires smooth emotional realism | Use repeated visual anchor; each cut advances state clearly |
| **蒙太奇 / Montage** | Memory, dream, symbolic contrast, parallel images, theme rather than linear action | childhood recall, grief objects, identity transformation, longing | direct dialogue scene, precise physical action | Use sound or object as transition anchor; keep fragments sensory and partial |
| **连续动作剪辑 / Continuous Action Editing** | Character moves through space under pressure | chase, escape, crossing rooms, storm/rain movement | tiny emotional beats, complex multi-person combat without reference | Keep direction consistent; define start/end spatial goal; limit actions |
| **格斗动作编排 / Fight Choreography** | 1v1 or limited multi-person staged combat with clear attack-defense beats | boxing, close combat, controlled stunt throw, wuxia exchange, underground ring | many attackers, unclear character references, gore, lethal injury emphasis | Define roles, attack line, defense, counter, footwork, contact point, camera response, safety constraints |
| **多人对话交叉剪辑 / Dialogue Cross-Cutting** | 2-4 people in one scene, power shifts through speech and silence | family dinner, office confrontation, breakup, negotiation | no meaningful dialogue or no relationship tension | Define seating/standing positions, who holds power, key lines, reaction shots |
| **长特写微表情 / Close-Up Micro-Expression** | Emotion is carried mainly by face/head with minimal action | shock, suppressed crying, shame, hidden love, inner collapse | plot needs many events or spatial movement | Use ECU/CU, stable or slow push, timed facial-muscle progression |
| **产品/人物质感片 / Product-Person Texture Film** | Product, place, or persona matters as much as plot | car, watch, founder, artist, venue, premium object | story requires many dramatic turns | Use tactile details, material, light, sound, controlled gesture, brand-like restraint |
| **大场面压缩 / Large-Scene Compression** | Crowd, disaster, ceremony, battlefield, launch, courtroom, banquet | chaos with one human anchor, public pressure, group reaction | no clear protagonist or visual anchor | Pick one visual anchor; show crowd as pressure; use 4-5 clear nodes |
| **长剧情拆分 / Sequential Prompt Split** | Story exceeds 15s or final prompt would exceed 2000 chars | reunion, investigation, travel, multi-stage emotional arc | one small moment already fits under 15s | Split by emotional turning points; make each ending a usable tail-frame reference |
| **剧情续写 / Continuation Segment** | User approves a segment and asks to continue | short-film sequences, tail-frame workflows, multi-part emotional arcs | no prior segment context exists | Begin from previous ending, preserve identity/scene/props, add only one new event |
| **主观镜头 / POV or Subjective Camera** | User needs immersion into a character's perception | fear, dizziness, memory trigger, entering unknown space | multi-character dialogue needs facial reactions | Use breath, hand edges, focus shifts, sound distortion; keep POV coherent |
| **匹配剪辑 / Match Cut Structure** | Two times/places/actions mirror each other | past vs present, childhood/adulthood, before/after identity | simple linear action is clearer | Match hand, object, gaze, light, or sound across cuts |

### Quick Decision Rules

- If the core is **one emotion changing inside one body**, choose `长特写微表情` or `单场景一镜到底`.
- If the core is **relationship pressure through words**, choose `多人对话交叉剪辑`.
- If the core is **a body moving toward a goal**, choose `连续动作剪辑`.
- If the core is **a staged fight**, choose `格斗动作编排`; keep fighters few and action beats explicit.
- If the core is **time, memory, or symbolism**, choose `蒙太奇` or `匹配剪辑`.
- If the core is **a process compressed into moments**, choose `跳剪压缩`.
- If the core is **a product/person/place aura**, choose `产品/人物质感片`.
- If the core is **large chaos but one person matters most**, choose `大场面压缩`.
- If the story cannot breathe within 15s, choose `长剧情拆分`.
- If the user asks to continue from an approved prompt, choose `剧情续写`.

### Hybrid Structures

Use hybrid labels when useful, but do not overcomplicate the final prompt.

Examples:

- `主结构：多人对话交叉剪辑；辅助：长特写微表情`
- `主结构：连续动作剪辑；辅助：主观镜头`
- `主结构：格斗动作编排；辅助：手持近身冲击感`
- `主结构：蒙太奇；辅助：匹配剪辑`
- `主结构：大场面压缩；辅助：单人物视觉锚点`
- `主结构：剧情续写；辅助：尾帧参考`

### Structure Failure Warnings

- Do not choose single take just because it sounds cinematic; use it only when the action can physically unfold in one continuous space.
- Do not choose montage when the user needs a clear cause-and-effect event.
- Do not put more than one major location change into a short single-take prompt.
- Do not write large crowd scenes without a visual anchor.
- Do not write long dialogue at the final second. Give reaction and aftertaste.

## Director-Level Shot Continuity Rules

Use these rules when writing multi-shot prompts. They make the prompt feel directed and editable, not just visually descriptive.

### Shot Size Progression

Avoid cutting between two adjacent shot sizes that are too close, because it can feel like a jump cut rather than an intentional edit.

Avoid:

- 全景 -> 中景
- 中景 -> 近景
- 近景 -> 特写
- 特写 -> 大特写

Prefer stronger size contrast or a motivated bridge:

- 全景 -> 近景 / 特写
- 中景 -> 特写 / 大特写
- 特写 -> 中景 / 全景
- 全景 -> 环境道具插入 -> 特写

If adjacent shot sizes are necessary, motivate the cut with action, sound, eyeline, object movement, or a clear emotional turn.

### Camera Angle Change

When cutting between shots of the same subject or same interaction, change the camera's horizontal angle by at least 30 degrees. This prevents awkward jump cuts and gives the edit a real perspective shift.

Examples:

- Shot 1: front-left 3/4 angle.
- Shot 2: side angle over the other character's shoulder, at least 30 degrees away.
- Shot 3: reverse angle or object insert.

Do not write repeated same-angle close-ups unless the scene intentionally uses a locked-off long take.

### Insert / Transitional Shots

Use insert shots when the scene needs breathing room or when long dialogue needs visual punctuation.

Good inserts:

- a hand tightening around a cup
- rain running down a car window
- a phone screen going dark
- chopsticks stopping above a bowl
- a candle flame shaking
- a ring, letter, key, cup, sword, music box, or old sweater
- empty chair, doorway, hallway, window reflection

Use inserts to:

- break long dialogue without losing tension
- show what a character avoids saying
- create a pause before a reveal
- bridge between two similar shot sizes
- give the editor a cutaway

Do not overuse inserts. In a 10-15s prompt, 1-2 inserts are usually enough.

### Ending Breath

Do not end the video on a line delivery, sudden facial expression, or unfinished action unless the user explicitly wants an abrupt cut. Leave 1-2 seconds for:

- a silent reaction
- breath settling
- eye contact holding
- sound tail
- the object after the action
- a character choosing not to speak
- a held frame for the next segment's tail-frame reference

This is especially important for dialogue, crying, confession, shock, and confrontation scenes.

### Match-on-Action Editing

When one action is important, split it across two different shot sizes or angles so the edit feels intentional.

Pattern:

```text
镜头01：中景，角色抬手伸向门把手，动作开始。
镜头02：特写，手指握住门把手并缓慢转动，延续同一动作。
```

Good match actions:

- reaching for a cup, ring, key, letter, sword, phone, door handle
- turning the head to look back
- raising a hand to wipe tears
- sitting down, standing up, stepping forward
- drawing a blade or pushing it back into the sheath
- starting a punch in medium shot, landing/parrying in close shot

Rules:

- The second shot should continue the same action, not restart it.
- Change shot size and horizontal camera angle.
- Keep object hand/side continuity clear.
- Use this to make simple actions feel cinematic without adding extra plot.

## Continuation and Tail-Frame Workflow

Use when the user says `继续`, `接着往下写`, `下一段`, `下一镜`, `延续上一条`, or wants to use the previous video's tail frame as reference.

### Continuation Principles

- Continue from the previous final image, not from a fresh setup.
- Keep character identity, age, hairstyle, clothing, makeup, injury state, and emotional residue consistent.
- Keep setting, lighting, weather, time of day, color palette, camera texture, and sound bed consistent unless the story intentionally changes.
- Keep key props consistent in design, position, and narrative meaning.
- Progress emotion instead of replaying it.
- Add only one main new event or emotional turn per 15s segment.
- Leave the ending as a clean next tail-frame if more continuation may follow.

### Continuation Diagnosis

Use this compact form:

```text
【接续判断】
上一段结尾状态：...
下一段情绪推进：...
连续性注意：人物服装、场景光线、关键道具、尾帧构图需要沿用...
```

### Reference Image Rules for Continuation

- If the next segment uses the same character, same scene, and same key props, say: `沿用上一段尾帧和已有参考图，不新增参考图。`
- If a new character appears, add `新增人物参考图`.
- If a new location appears, add `新增场景参考图`.
- If a new key prop appears, add `新增关键道具参考图`.
- If a costume, injury, makeup, or emotional state visibly changes and must remain stable later, add an updated character reference.

### Continuation Opening Phrases

Use clear continuity phrases in the final prompt:

```text
开头延续上一条尾帧：...
保持同一人物、同一服装、同一场景光线和同一道具位置。
上一段结尾的情绪不重置，继续从...推进到...
```

### Good Continuation Moves

- Shock -> numb stillness.
- Numbness -> one decisive action.
- Suppressed crying -> private collapse.
- Argument -> silent aftermath.
- Discovery -> cautious approach.
- Reunion recognition -> first touch.
- Chase miss -> breathless decision.
- Suspense sound -> slow move toward source.

### Bad Continuation Moves

- Repeating the same reveal from the previous segment.
- Jumping to a new location without a transition or user request.
- Changing clothing, lighting, age, or prop design accidentally.
- Adding multiple new plot events in one 15s segment.
- Starting with a generic establishing shot when the previous tail frame should be used.

## Prompt Compression

Final prompts should be direct and proportionate to scene complexity. The 2000-character limit is a ceiling, not a target. It applies only to the copy-ready final prompt, not to the diagnosis or strategy sections in workshop mode.

Length targets:

- 500-800 Chinese characters: simple one-person, one-action, one-emotion scenes.
- 800-1300 Chinese characters: default range for most 8-15s cinematic prompts.
- 1300-2000 Chinese characters: complex scenes such as multi-person dialogue, large-scene compression, montage, long-story splits, or spatial action.

If the prompt exceeds 1300 characters, each extra detail must improve generation stability, emotional clarity, spatial continuity, or failure prevention. If not, cut it.

- Do not include empty boilerplate such as `视频模型：通用 AI 视频模型`. If no model is specified, omit it.
- Put duration and structure into the first summary line.
- Merge repeated labels.
- Keep only the strongest sensory details.
- Remove generic praise words like "高级", "震撼", "大片感" unless replaced by concrete light, motion, sound, or performance.
- If more detail is required, split into multiple prompts instead of overloading one.

## Visual Reference Image Prompt Patterns

Use these optional text-to-image prompts as visual anchors before video generation. They are not the final video prompt. Keep them consistent with the final prompt. The user may generate these references first for more control, or skip them and generate video directly.

### Character Reference

Purpose: stabilize identity, age, temperament, costume, and facial baseline.

Include age range, face impression, hair, clothing, emotional baseline, shot size, lighting, background, film texture, and color palette.

Template:

```text
人物参考图：{身份/年龄/时代}，{脸型与气质}，{发型与服装}，{情绪基调}，{镜头距离}，{光线与背景}，真实电影质感，低饱和色调，细腻皮肤纹理，非写真摆拍。
```

Example:

```text
人物参考图：中国古风女子，二十七岁左右，清瘦克制，鹅蛋脸，眉眼柔和但带疲惫感，黑发盘成低髻，素雅青灰色宫装，少量银色发簪，表情平静但眼眶微湿，头部特写，烛光侧照，深色宫殿背景，真实古装电影质感，低饱和色调。
```

### Scene Reference

Purpose: stabilize layout, light source, materials, and action space.

Include location, spatial layout, foreground/midground/background, light source, color temperature, key objects, usable action path, atmosphere, era, and materials. Use `无人物` when the scene reference should be clean.

Template:

```text
场景参考图：{地点}，{空间结构}，前景{...}，中景{...}，背景{...}，{主要光源与色调}，{材质与氛围}，真实电影场景质感，空间纵深清晰，无人物。
```

Example:

```text
场景参考图：深夜独居女性公寓玄关到客厅的连续空间，前景左侧是玄关鞋柜，中景是半暗客厅，背景右侧卧室门半掩，玄关暖黄小灯与窗外冷蓝城市光混合，低照度现实主义电影质感，空间纵深清晰，无人物。
```

### Key Prop Reference

Purpose: stabilize objects that carry story information.

Use only for important props: old sweater, music box, rejection letter, phone, ring, sword, cup, car, watch.

Template:

```text
关键道具参考图：{道具}，{年代/材质/磨损细节}，{与剧情有关的标记}，{光线与背景}，真实电影道具质感，微距或近景，细节清晰。
```

Example:

```text
关键道具参考图：一只生锈的旧音乐盒，暗红木质外壳，边角磨损，金属发条氧化，盒盖有细小划痕，放在旧木桌上，月光侧照，微距近景，真实电影道具质感，细节清晰。
```

### Product or Vehicle Reference

Purpose: stabilize premium object structure and material.

Template:

```text
产品参考图：{产品/车辆}，{颜色与材质}，{角度}，{环境与光线}，真实品牌片电影质感，结构准确，材质自然，不要错误文字标识。
```

### Reference Image Count

- Use 1 reference for a simple emotional close-up.
- Use 2 references for most scenes: character + scene.
- Use 3 references only when a prop/product is central or the scene is historically/stylistically demanding.
- Avoid giving separate reference prompts for every minor object.

### Continuation References

- For continuation, reuse prior tail frame and existing references by default.
- Add new reference prompts only for new visual anchors.
- If using a previous tail frame, the scene reference can be omitted unless the camera moves into a new space.
- If a new character enters an existing scene, provide only the new character reference and state that the existing scene reference remains unchanged.

### Reference Consistency Check

Before finalizing, ensure reference prompts and video prompt share:

- same character age, clothing, hairstyle, and emotional baseline
- same setting, era, color palette, and lighting
- same key prop design
- no contradiction between still-image pose and video action.

## Negative Constraints

Use negative constraints only when they prevent likely generation failure:

- 不要卡通感，不要塑料皮肤，不要过度磨皮。
- 不要错误文字、水印、字幕。
- 不要背景音乐，不要额外配乐；只保留必要台词人声、环境声、动作音效、物体声。
- 不要多余肢体、脸部畸变、动作穿模。
- 不要过度快剪 if continuity matters.

### Negative Constraint Library

Pick the smallest useful set for the scene. Avoid bloated lists that repeat every possible failure mode.

**Universal core**

```text
负面约束：不要字幕水印，不要背景音乐，不要脸部畸变，不要多余手指或肢体，不要卡通感。
```

When the scene has no visible hands or full body, omit hand/body constraints.

**Emotional close-up**

Risks: overacting, sudden emotion jump, plastic skin, beauty filter.

```text
不要夸张哭喊，不要突然表情变化，不要过度磨皮，不要塑料皮肤，不要脸部畸变。
```

**Dialogue scene**

Risks: theatrical acting, messy mouth movement, bad eye lines, subtitles.

```text
不要舞台剧式表演，不要夸张争吵，不要嘴型持续乱动，不要视线方向混乱，不要字幕水印。
```

**Romance or intimacy but non-explicit**

Risks: sexualization, melodrama, unwanted physical escalation.

```text
不要露骨性暗示，不要突然拥抱亲吻，不要偶像剧式夸张表演，不要过度柔光磨皮。
```

**Suspense without monster**

Risks: horror clichés, jump scare, supernatural insertion.

```text
不要鬼怪，不要血腥，不要突脸惊吓，不要尖叫，不要夸张恐怖音乐。
```

**Action, chase, or physical movement**

Risks: motion confusion, duplicated bodies, impossible direction, warped limbs.

```text
不要动作穿模，不要空间方向混乱，不要多余肢体，不要人物瞬移，不要过度动态模糊。
```

**Wuxia or combat**

Risks: fantasy overextension, weapon deformation, messy multi-person fights.

```text
不要飞天玄幻，不要夸张光效，不要血腥，不要武器变形，不要肢体穿模，不要多人动作混乱。
```

This area still needs stronger reference examples before heavy use.

**Crowd, disaster, or large scene**

Risks: uncontrolled crowd, protagonist lost, disaster becoming monster/fantasy.

```text
不要人物数量失控，不要主角丢失，不要海怪或超自然，不要过度血腥，不要场景结构变形。
```

**Product, vehicle, or premium object**

Risks: ad-like exaggeration, fake material, object deformation.

```text
不要广告式夸张炫技，不要塑料质感，不要车身或产品结构变形，不要过度慢动作，不要错误文字标识。
```

**Period drama or ancient costume**

Risks: modern styling, fantasy game look, costume inconsistency.

```text
不要现代妆容，不要现代饰品，不要廉价影楼古风，不要游戏CG感，不要服装发饰跳变。
```

**Memory, dream, or montage**

Risks: too clear, too literal, over-glowy fantasy.

```text
不要过度梦幻发光，不要恐怖化，不要记忆画面过于完整清晰，不要场景无逻辑跳变。
```

**Phone, screen, or text**

Risks: unreadable text, random letters, fake UI, subtitle pollution.

```text
不要生成错误文字，不要乱码界面，不要过多手机屏幕文字，不要字幕水印。
```

If key information is on a phone, prefer offscreen voice or a simple visible notification rather than relying on readable screen text.

**Food, hands, or table scenes**

Risks: hand/finger errors, object warping, continuity issues.

```text
不要手指畸形，不要餐具穿模，不要筷子变形，不要杯子或盘子数量跳变。
```

### When to Omit Negative Constraints

Omit or shorten them when:

- The user asks for a very compact prompt.
- The scene has few generation risks.
- The final prompt is near the 2000-character limit.

Minimum fallback:

```text
负面约束：不要字幕水印，不要背景音乐，不要脸部畸变，不要风格跑偏。
```

## Quality Self-Check

Run this silently before giving the final answer. Do not print it unless the user asks for a critique, debug pass, or improvement report.

### Story and Structure

- Does the diagnosis name the emotional core and visual core?
- Is the chosen structure explicitly stated and justified?
- Does the duration fit the content instead of defaulting to 15s?
- If the story exceeds 15s or 2000 characters, does the answer recommend splitting and clearly state what this prompt covers?
- If this is a split prompt, does the first segment end on a usable tail-frame reference and the next segment continue from it?

### Prompt Usability

- Is the final prompt copy-ready and under 2000 Chinese characters when possible?
- Is there no empty boilerplate such as `视频模型：通用 AI 视频模型`?
- Does the first summary line include duration and structure?
- Are technical terms useful rather than decorative?
- Are abstract words translated into visible action, light, sound, object, or performance?
- If reference-image prompts are included, are they optional, concise, and consistent with the final video prompt?
- For continuation, does the next prompt start from the previous ending and preserve identity, scene, lighting, sound bed, and key props?

### Time and Rhythm

- Are time blocks playable, with enough duration for action, camera movement, line delivery, and reaction?
- Is key dialogue or peak action not placed at the final instant?
- Does the ending leave 1-2 seconds for breath, reaction, sound tail, or visual afterimage?
- Are there too many events for the duration? If yes, remove details or split.
- Is shot duration based on dramatic weight instead of equal mechanical division?

### Dialogue and Sound

- If the plot implies a key spoken line, is the actual line written?
- Are phone calls, doctor/police notices, confessions, breakups, voice messages, or offscreen lines concrete?
- Is key dialogue short enough for the time block?
- Does sound design include concrete diegetic sound rather than generic music?
- Does the prompt avoid background music by default and keep only necessary dialogue/voice, ambient sound, Foley, movement, object, and action sound effects?
- Is silence or sound reduction used when it would strengthen shock, tension, or aftermath?

### Character Performance

- Are emotions expressed through eyes, lips, jaw, breath, hands, posture, and timing?
- For long close-ups, is there a smooth micro-expression timeline with no sudden jump?
- Are 3-5 micro-expression beats chosen instead of an overloaded facial-action list?
- Is the performance natural for the character's situation, age, status, and relationship?
- Are tears, crying, anger, or fear restrained unless the story specifically needs a large outburst?

### Camera and Visual Logic

- Is the camera movement physically plausible?
- Does each shot have a clear subject and composition?
- For action or crowd scenes, is spatial direction clear?
- For large scenes, is there one visual anchor the model can follow?
- For product/person texture scenes, are materials, tactile details, and light concrete?
- For memory/dream scenes, is there a transition anchor such as sound, object, gesture, or match cut?
- In multi-shot prompts, do adjacent shots avoid overly similar shot sizes unless motivated?
- When cutting between shots of the same subject, does the camera angle change by at least 30 degrees?
- Are insert shots used when long dialogue or emotional pauses need breathing room?
- Does the ending leave a 1-2s performance pause or visual/sound tail?
- If one action is split across shots, does the second shot continue the same action with match-on-action continuity?

### Negative Constraints

- Are negative constraints scene-specific and concise?
- Do they target likely failures: subtitles/watermarks, face distortion, extra fingers, hand errors, motion confusion, style mismatch, modern styling in period scenes, fake product material?
- Are irrelevant constraints omitted?

### Safety and Taste

- Does the prompt avoid explicit sexual content, sexualized minors, and non-consensual sexual material?
- For violence, does it focus on staging, suspense, consequence, or emotion rather than gore?
- Does intimacy stay within the user's requested tone and boundaries?

### Final Pass

- Would a video model know what to show in each second?
- Would a director or cinematographer understand the scene's physical execution?
- Is the prompt cinematic because of concrete choices, not generic adjectives?
- Is the answer useful for workshop mode: diagnosis and strategy concise, final prompt dominant?
