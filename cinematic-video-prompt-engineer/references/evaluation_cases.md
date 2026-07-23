# Formal Evaluation Set

Use this file only when testing or revising the skill. Do not load it during ordinary prompt generation.

## Scoring Rubric

Score each case out of 100:

- Story diagnosis and structure choice: 15
- Duration and pacing feasibility: 15
- Camera, axis, eyeline, and spatial continuity: 15
- Character performance and emotional clarity: 15
- Dialogue timing and sound design: 10
- Reference-image consistency: 10
- Prompt clarity, compression, and length compliance: 10
- Scene-specific negative constraints and safety: 10

Pass levels:

- 90-100: production-ready
- 80-89: usable with minor revision
- 70-79: major weakness in one area
- below 70: revise rules or output strategy

Automatic failure conditions:

- final prompt exceeds 2000 Chinese characters without recommending a split
- single segment exceeds 15 seconds
- key plot-changing dialogue is omitted
- dialogue cannot physically fit its assigned time
- continuation resets character, scene, prop, or emotional state
- action direction becomes contradictory or axis flips without motivation
- unsafe explicit sexual content, sexualized minors, or gore-focused violence

## Evaluation Procedure

For each case:

1. Generate the answer in workshop mode.
2. Measure only the copy-ready final prompt against the 2000-character ceiling.
3. Check timing beat by beat.
4. Mark continuity states: position, direction, held object, costume, light, emotional residue.
5. Record failures and update rules only when the failure is generalizable.

---

## Case 01: Quiet Grief Close-Up

Input:

```text
古代宫廷女子得知深爱之人明日将被赐死。她独自站在烛火前，不能哭出声，只能慢慢接受消息。要求10秒超近面部固定镜头，无台词。
```

Expected:

- Structure: long close-up micro-expression / emotional arc.
- No unnecessary scene cuts or body blocking.
- Smooth progression from reception to restraint to one controlled release.
- Character reference only; scene reference optional.
- No background music; candle, breath, distant drum may remain.
- Final prompt target: 500-800 characters.

Failure checks:

- sudden crying before emotional buildup
- too many facial beats for 10s
- theatrical grimacing or beauty-filter language

## Case 02: Two-Person Dialogue and Axis

Input:

```text
除夕饭桌上，父亲宣布卖掉老房子，母亲沉默回避，女儿发现父母早已决定。15秒，多人对话，克制冲突。
```

Expected:

- Structure: dialogue cross-cutting with one insert shot.
- Establish father, mother, daughter positions.
- Preserve screen-left/right and eyelines in close-ups.
- Key lines are explicit and timed.
- Insert may use chopsticks, bowl, steam, or hand movement.
- Dialogue ends before final 1-2s silence.

Failure checks:

- reverse-shot eyelines flip
- three long lines packed into a few seconds
- no reaction time after daughter's final line

## Case 03: Phone-Call Shock

Input:

```text
深夜公寓，女孩接到男友车祸去世的电话。先轻松聊天，听到噩耗后笑容冻结，挂断后捂嘴无声痛哭。15秒三段跳剪。
```

Expected:

- Caller states the actual news.
- Dialogue delivery time fits.
- Smile freeze uses micro-expression progression.
- Phone remains in the same hand unless a transfer is shown.
- Sound shifts from phone noise/room tone to muffled shock and suppressed breath.
- Ending leaves silent aftermath.

Failure checks:

- vague phrase such as “对方说出噩耗”
- phone changes hands or position without action
- crying starts instantly

## Case 04: Suspense Spatial Continuity

Input:

```text
独居女孩回家发现玄关多了一把陌生钥匙，走进客厅后听见卧室里传来手机震动。15秒，不出现鬼怪或袭击者。
```

Expected:

- Scene reference defines玄关、客厅、卧室门的 spatial relationship.
- Character movement direction remains continuous.
- Suspense comes from sound and withheld information.
- No jump scare, monster, or unexplained location flip.

Failure checks:

- bedroom switches screen side
- protagonist teleports between spaces
- loud horror music replaces environmental sound

## Case 05: Match-on-Action Emotional Prop

Input:

```text
分手后的两个人在清晨厨房同时伸手拿同一只杯子，手指碰到后都假装没事。10秒。
```

Expected:

- Use match-on-action: medium start of reach -> close continuation at cup.
- Change shot size and horizontal camera angle.
- Cup position and which hands touch remain consistent.
- One short exchange only; leave ending breath.

Failure checks:

- reach action restarts in the second shot
- cup jumps location or hand side
- adjacent similar shot sizes without motivation

## Case 06: 1v1 Fight Choreography

Input:

```text
废旧仓库地下擂台，两名成年女性进行10秒真人格斗。第一轮拳腿试探，第二轮近身反摔。多人围观但不参与。
```

Expected:

- Structure: fight choreography.
- 2 shots, 6-8 total action beats.
- Attack line, evasion, contact point, footwork, weight transfer, camera response.
- Stable A/B screen positions until a visible pivot or throw.
- Use 2-4 principal camera methods selected for specific fight beats; no unmotivated stacking of orbit, whip pan, push-in, slow motion, and impact hold.
- Final prompt 1300-1800 characters, under 2000.
- Staged, non-lethal, no gore.

Failure checks:

- more than 10 action beats
- crowd enters fight
- throw occurs without level change/grip/momentum setup
- camera tricks obscure contact points, landing positions, or the attack-defense chain

## Case 07: Environmental Fight

Input:

```text
古代赌坊翻脸，江湖赌客利用赌桌、骰盅、长凳和木柱反制两名打手。15秒，无血腥。
```

Expected:

- Clear room layout and environmental anchors.
- Cause-effect chain: body -> prop contact -> prop reaction -> opponent reaction -> camera reaction.
- 2-3 shots, no more than 10 beats.
- Props do not teleport or randomly break.
- Final prompt under 2000 characters.

Failure checks:

- too many simultaneous attackers/actions
- furniture positions change between shots
- impact lacks environmental consequence

## Case 08: Large-Scene Compression

Input:

```text
暴风雨夜客轮倾斜，乘客逃生，母亲逆流寻找孩子，最后隔着正在关闭的防水舱门看见他。15秒。
```

Expected:

- One visual anchor: mother's distinctive clothing.
- Crowd acts as pressure, not competing protagonists.
- 4-5 clear story nodes maximum.
- Spatial direction toward the watertight door remains consistent.
- Child's line, if used, finishes before final held reaction.

Failure checks:

- protagonist lost in crowd
- disaster spectacle overwhelms story
- final line lands at 15.0s with no breath

## Case 09: Long Story Split and Tail Frame

Input:

```text
30秒剧情：多年未归的男人在深夜老火车站与年迈母亲重逢。拆成两个15秒，并用第一段尾帧生成第二段。
```

Expected:

- Segment 1: discovery and approach; stable tail-frame composition.
- Segment 2: begins from exact previous state; recognition and touch.
- Same clothing, light, bench, sweater, positions, and sound bed.
- Each final prompt under 2000 characters.

Failure checks:

- second segment restarts with a new establishing shot
- mother already recognizes him in segment 1
- prop or lighting changes

## Case 10: Continuation with New Character and Location

Input:

```text
上一段：女孩在公寓接到男友去世的电话，结尾蜷缩在地板上。继续下一段：她赶到医院，第一次见到男友的姐姐。
```

Expected:

- Continuation diagnosis explains emotional and spatial transition.
- Reuse protagonist reference; add new sister character reference and hospital scene reference.
- Preserve protagonist clothing, phone, tear state, and emotional residue unless a time gap is stated.
- Do not replay the phone reveal.

Failure checks:

- no new visual references
- protagonist appears freshly composed without transition
- too many hospital events in one segment

## Case 11: Vague Input Handling

Input:

```text
我要一个很震撼、很电影感的视频。
```

Expected:

- Ask one concise question covering missing foundation: protagonist, setting, and intended emotion/transformation.
- Do not invent a full story immediately.

Failure checks:

- generic spectacle prompt
- asks for lenses, lighting, or other technical details before story foundations

## Case 12: Reference Consistency

Input:

```text
古代闺中小姐在午后窗边突然看见心上人，10秒超近面部特写，无台词。先给人物参考图，再给视频提示词。
```

Expected:

- Character prompt and video prompt match age, hairstyle, hairpins, clothing, light, makeup, and emotional baseline.
- Camera may represent the beloved's POV.
- No second person visible.
- No contradictory lighting or fashion-poster pose.

Failure checks:

- character details drift between reference and video prompt
- overt seduction replaces restrained shy love
- camera movement conflicts with fixed-close-up request

## Case 13: Automatic Compression

Input:

```text
请把一个包含3名角色、4个镜头、两段台词、雨夜车内争吵和一次下车动作的15秒提示词压缩到2000字以内，但保留剧情和情绪。
```

Expected:

- Apply the compression ladder before splitting.
- Remove repeated style/light/sound descriptions first.
- Preserve plot-changing dialogue, spatial continuity, reaction, and ending breath.
- If still overloaded, reduce shot/event count or recommend splitting.

Failure checks:

- removes the core reveal or listener reaction
- compresses into unreadable fragments
- leaves repeated style boilerplate while cutting causality

## Case 14: Character Bible Continuity

Input:

```text
连续三段古风短片使用同一位26岁宫廷女子：第一段发簪完整，第二段逃跑时左侧发簪掉落，第三段躲进偏殿继续剧情。
```

Expected:

- Canonical identity remains stable.
- Temporary state updates after segment 2: left hairpin missing, hair slightly loose, clothing wet/dusty if established.
- Segment 3 does not restore the missing hairpin.
- Reference assets mark `更新状态`, not a new identity.

Failure checks:

- face, age, costume, or hair color drifts
- missing accessory resets
- state change occurs without visible action

## Case 15: Scene Bible and Prop State

Input:

```text
在同一间深夜公寓连续生成两段：第一段女孩把手机放在客厅地板右侧并走向卧室；第二段她听见敲门后返回客厅。
```

Expected:

- Apartment layout, bedroom side, door, light direction, and travel direction remain stable.
- Phone remains on the floor until picked up on screen.
- The second segment begins from the previous tail-frame state.

Failure checks:

- phone appears in hand without pickup
- bedroom/door swaps side
- lighting or time resets

## Case 16: Output Mode Selection

Inputs:

```text
A：直接给我最终提示词，不要分析。
B：先诊断剧情，我想一起调整。
C：这是一个连续5段短片，请维护人物和场景一致性。
```

Expected:

- A uses compact mode.
- B uses workshop mode.
- C uses continuous-short-film mode with character/scene continuity and tail-frame anchors.

Failure checks:

- outputs the same structure for all three
- compact mode includes unnecessary references
- continuous mode omits reusable continuity records

## Case 17: Coquettish Soft Refusal Close-Up

Input:

```text
年轻女子在亲密但安全的关系里小声说“我不要”，她不是真的拒绝，而是带点娇嗔、害羞和被宠爱的任性。6秒固定面部特写，不要露骨，不要夸张撒娇。
```

Expected:

- Structure: ultra-close face long take / coquettish soft refusal arc.
- The line `我不要` is explicitly written and timed.
- Performance reads as gentle, safe, playful softness: gaze dodges then returns, mouth suppresses a smile, body does not retreat.
- No real fear, coercion, disgust, explicit seduction, childish baby voice, or cartoonish pout.
- Final prompt target: 500-800 characters.

Failure checks:

- interprets the refusal as fear or non-consent
- turns the scene into overt sexualization or exposed-body emphasis
- uses exaggerated idol-drama acting instead of subtle micro-expression
- omits the spoken line

## Case 18: General Camera Movement Function

Input:

```text
15秒心理悬疑：男人在空荡地铁站发现站台对面的人和自己长得一模一样。先是普通等待，然后听见广播故障声，抬头看见对面，世界感突然失衡，最后他没有逃，只是僵住。
```

Expected:

- Camera movement is selected by function, not stacked as decoration.
- Ordinary waiting can use `Static` or subtle `Handheld`; discovery can use `Pan` or `Push-In`; psychological vertigo may use one brief `Dolly Zoom` or `Dutch Angle Static`.
- No more than 2-3 principal moves in the final prompt.
- Movement has readable start/end subjects and leaves 1-2s frozen aftermath.
- Station geography and screen direction remain clear.

Failure checks:

- piles up `Push-In`, `Orbit`, `Zoom`, `Whip Pan`, `Handheld`, and `Dutch Angle` in the same beat
- uses `Dolly Zoom` without a major realization
- camera movement obscures the double's position or the protagonist's reaction
- ending cuts immediately at the discovery without aftermath

## Case 19: Live Performance Realism

Input:

```text
晚上家里餐桌前，年轻女性对镜头解释为什么她没有去参加朋友婚礼。她表面平静，其实很在意这件事。10秒，手机实拍感，半身近景，一杯水放在桌上。
```

Expected:

- Strategy mentions live performance realism or psychological motive.
- Performance is driven by one motive: restrained explanation of something that matters to her.
- Eye line, pauses, voice pace, mouth corners, breath, and small gestures align with that motive.
- Body language is low-amplitude and incidental: slight head dip, small nod, fingers near cup, sleeve adjustment, tiny weight shift.
- Biomechanics are linked: eyes move before head, neck/shoulders follow, breath affects chest/voice, hand movement involves wrist/forearm/sleeve.
- Object contact has weight and sequence: fingertips approach cup, contact, slight pressure/friction, cup remains stable.
- Environment responds subtly: hair, sleeve folds, cup reflection, warm light/shadow, room tone.
- Camera/light/focus stay consistent with phone indoor realism; no commercial studio look.

Failure checks:

- fixed fake smile or empty eyes
- gestures added only to make the frame busy
- isolated head/hand movement with frozen shoulders and no breath
- hand/cup penetration, cup drift, or object movement before contact
- character feels pasted onto the background
- phone realism mixed with perfect studio lighting, plastic skin, or ad-like stabilization

## Case 20: Ordinary Drama One-Take Blocking

Input:

```text
15秒一镜到底：深夜厨房里，妻子发现丈夫藏在水槽下的诊断报告。丈夫从客厅走进来想解释，她没有立刻质问，只是把报告慢慢推回原处，最后两人隔着厨房岛台沉默对视。
```

Expected:

- Structure: single take, ordinary drama one-take blocking.
- Clear start frame and spatial anchors: kitchen island, sink cabinet, living-room entrance, report.
- One physically possible camera path, not multiple invisible cuts.
- Blocking changes relationship pressure: wife near sink/island, husband entering from living-room side, island between them at the end.
- Use `Rack Focus` or `Focus Pull` only if it clarifies report -> wife reaction -> husband entrance.
- Keep screen direction, prop position, lighting, and body distance continuous.
- End with 1-2s held silence after the report is pushed back.

Failure checks:

- says one-take but describes unrelated camera angles or cuts
- report jumps from hand to drawer/counter without visible action
- husband teleports into the kitchen or changes side of the island
- uses too many camera moves instead of one coherent path
- ends on the line/reveal without silence or reaction

## Case 21: One-Take Character Reveal Ladder

Input:

```text
15秒一镜到底古装府邸庭院群像：嫡长子、嫡长女、庶子、庶女四人暗中对峙。要求从嫡长子面部特写开始，通过环绕、背影遮挡、横移、后拉逐步揭示其他人，最后形成庭院权力站位。无台词。
```

Expected:

- Structure: single take with character reveal ladder.
- Starts on one face only, then reveals others progressively rather than showing all four at once.
- Uses foreground/back/shoulder/table/column masking to keep the one-take path physical.
- Each character has distinct identity anchors: face impression, hair/headdress, costume color/material, posture, status, emotional baseline.
- Pull-back or widening clarifies hierarchy and courtyard layout.
- Stable lighting/atmosphere is summarized once; night courtyard light stays physically plausible: moonlight as soft ambient/edge light, face readability from lantern/candle/corridor/window spill or stone/table bounce, no hard moonlight cutting a face without source logic.
- No duplicate faces, extra people, modern objects, or identity drift.

Failure checks:

- describes cuts while claiming one-take
- reveals four people too fast with no spatial logic
- characters have similar faces/clothes or duplicated identity
- camera path circles/passes through impossible space
- lighting and style tags crowd out blocking, identity, and hierarchy
- cold moonlight or abstract cinematic lighting creates an unrealistic hard face spotlight in an outdoor courtyard

## Case 22: Prompt Sampling Range Control

Input:

```text
做一个10秒破碎记忆闪回：女孩站在雨夜车站，脑中闪回车祸、红伞、碎玻璃、短信。要电影感，情绪是突然想起真相。
```

Expected:

- Strategy names the abstract effect and translates `破碎记忆闪回` into visible fragments rather than leaving it as a style label.
- Final prompt uses a small number of concrete memory shards, such as rain on glass, red umbrella reflected in a puddle, headlight flare, phone vibration, glass shards catching light, and the girl's eyes refocusing.
- The memory fragments are physically compatible; no object is asked to break into fragments and form an impossible unrelated shape at the same time.
- The desired action path is written positively: the girl freezes, visual shards intrude, her gaze locks onto one clue, and she realizes the truth.
- Negative constraints are short and secondary, focused on likely failures such as no subtitles/watermarks, no background music, no face distortion, and no over-glowy fantasy.
- Details are limited to the strongest 4-5 visual anchors so the 10s clip remains playable and not over-specified.

Failure checks:

- only says `破碎记忆闪回` or `电影感特效` without visible screen evidence
- relies on `不要混乱、不要发呆、不要失败` instead of describing the desired visual/action path
- contains contradictory object behavior, impossible lighting, or incompatible camera movement
- lists too many fragments, props, overlays, camera moves, and emotions for 10 seconds
- negative constraints become longer than the positive creative prompt

## Case 23: Execution Stability and Prop Endpoint

Input:

```text
12秒悬疑戏：深夜办公室，女律师发现桌上的U盘里有关键证据，她刚插进电脑，门外响起脚步声，她立刻拔下U盘藏进左手袖口，假装继续看文件。
```

Expected:

- Final prompt opening is reconstructable: office layout, woman position, desk/computer/U-disk start state, shot size, angle, gaze, and practical light source are clear.
- Each shot has one core action and one core camera behavior; camera movement does not compete with the U-disk handling.
- U-disk state is precise: where it starts, which hand inserts it, when it is pulled out, how it is hidden in the left sleeve, and where it ends.
- Ending state is locked because this can continue: woman seated or standing, left sleeve hiding the U-disk, file in front of her, gaze/face pretending calm, door/footstep direction established.
- No unresolved options such as `或`, `或者`, `A/B`, `可选`.
- Sound includes diegetic anchors: computer USB sound, distant footsteps, paper movement, breath or room tone; no background music by default.

Failure checks:

- starts with a vague office mood and does not specify the first frame
- says `她藏好U盘` without holder/hand/contact/final location
- uses several competing camera moves in one shot
- ends before showing the hidden U-disk state and her cover behavior
- includes optional branches like `藏进袖口或抽屉`
- relies mainly on negative constraints instead of positive stable action

## Regression Log Template

Append results in this form when testing:

```text
Date:
Skill version/commit:
Case:
Score:
Observed failure:
Root cause:
Rule changed:
Retest result:
Remaining risk:
```
