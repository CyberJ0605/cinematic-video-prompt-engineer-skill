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

- 90-100: strong prompt-text result; actual media quality still requires generated-result review
- 80-89: usable with minor revision
- 70-79: major weakness in one area
- below 70: revise rules or output strategy

Automatic failure conditions:

- final prompt exceeds the duration-based character ceiling without recommending a split
- single segment exceeds 30 seconds
- repeats a resolved approval, executes an unapproved media action, omits requested deliverables without a stated blocker, or claims unavailable image/video verification
- key plot-changing dialogue is omitted
- dialogue cannot physically fit its assigned time
- continuation resets character, scene, prop, or emotional state
- action direction becomes contradictory or axis flips without motivation
- unsafe explicit sexual content, sexualized minors, or gore-focused violence

## Evaluation Procedure

For each case:

1. Generate the answer in the mode/stage requested by the case; use workshop mode only when unspecified. Keep explicit approval boundaries and host capability conditions.
2. Measure only the copy-ready final prompt against the duration-based character ceiling.
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
- Final prompt 1300-1800 characters when the selected duration is 10-15s; longer 16-30s fight prompts may use up to 2800 characters if every beat is necessary.
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
- Final prompt under the duration-based character ceiling.

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
- Segment 2: preserves the previous story/action state; recognition and touch, with a motivated differentiated opening angle unless a same-shot extension is explicit.
- Same clothing, light, bench, sweater, positions, and sound bed.
- Each final prompt under the duration-based character ceiling.

Failure checks:

- second segment resets the event or repeats discovery; a motivated new angle preserving story state is allowed
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

## Case 24: Dialogue-Driven Performance Control

Input:

```text
15秒情感控诉戏：深夜客厅，女人终于知道丈夫三年前就隐瞒了她父亲病危的消息。她一开始不是哭，而是冷静反击，说：“你一直都知道，对吗？那我这三年算什么？”第一句带攻击，第二句说到“我”时声音变轻，最后才掉下第一滴眼泪。丈夫坐在对面沉默。
```

Expected:

- Strategy mentions dialogue-driven performance control, trigger words, or emotion barrier.
- The prompt does not write `女人悲伤地哭着说` as a single mood label. It treats the dialogue as the expression timeline.
- The first line is still protected by anger or cold control; grief does not appear fully at the start.
- The trigger word is clear, especially `我` or `三年`; the second line changes voice, gaze, face, and body after that word.
- Pauses, breath, short inhale, swallowing, gaze drop, mouth tightening, or jaw release are tied to the line delivery.
- First tear is delayed until after the protection layer cracks; it does not fall before or during the first attack line.
- Optional AU/FACS, if used, appears after natural-language facial actions and stays compact, such as AU1/AU15/AU17 from B to C.
- Husband's listener reaction is included but restrained; he should not steal the scene.
- Ending leaves 1-2s for silence, breath, tear fall, or room tone after the line.

Failure checks:

- emotion jumps directly from anger to crying with no protective layer
- dialogue is pasted under a generic sadness/anger label
- no trigger word, no pause, no breath, no post-line state
- first tear appears too early
- AU codes are dumped without visible natural-language facial action
- listener overacts or interrupts the main performance
- ending cuts immediately after the last word

## Case 25: 30s Duration Selection and Long Prompt Budget

Input:

```text
30秒现实情感对话戏：清晨出租屋，准备搬走的女人把钥匙放在桌上，男人假装平静地说“你走吧，我没事”。女人停住，没有回头，问：“你真的没事，还是只是不想留我？”男人先笑了一下，想把话题带过去，随后终于承认：“我怕我一开口，就会显得太难看。”最后两人没有拥抱，只隔着一张旧餐桌沉默。要求表演自然，有停顿和呼吸，不要大哭。
```

Expected:

- Diagnosis explains why this scene can use 24-30s: dialogue delivery, hesitation, listener reaction, table/keys contact, and emotional aftertaste need time.
- The skill does not claim every prompt should default to 30s; it chooses a specific duration, such as 26s or 28s, only if the scene needs it.
- Final prompt normally stays within the 2200-3400-character target for a 25-30s scene and always below the 4000-character ceiling. Any text beyond 3000 characters must directly support timing, performance, contact realism, spatial continuity, sound, or ending breath.
- Dialogue is timed with pauses and breath. The key lines are explicit and have enough room before and after delivery.
- The man's smile is protective rather than cheerful; grief or collapse does not arrive before the line that triggers it.
- The keys, table, body distance, and eyelines stay consistent.
- Ending leaves at least 2s for silence, room tone, breath, or stillness after the final line.

Failure checks:

- keeps the old 15s maximum and splits even though one 24-30s prompt can carry the scene
- stretches a simple beat to 30s without dramatic reason
- exceeds 4000 Chinese characters without recommending a split, or exceeds 3000 with decorative detail that does not improve generation
- packs all lines together with no pauses or listener reactions
- uses generic sadness labels instead of line-triggered performance changes
- cuts immediately after the final line

## Case 26: 30s Psychological Stage Timeline

Input:

```text
29秒超近情绪长镜头：女人面对即将离开的恋人，从追问到认命，再到想最后记住他的脸，最后含泪放手。她只说两句台词：“真的要走吗？”和“你走吧。”要求前面不要大哭，第一滴泪要很晚才落下，最后是含泪微笑。
```

Expected:

- Strategy names a psychological stage timeline rather than only listing time codes.
- Final prompt uses 4-5 stage titles such as `追问`, `认命`, `记住`, `惋惜`, `放手`.
- Each stage includes visible action/expression evidence and a distinct psychological task.
- The two smiles are differentiated: early smile as self-mockery/acceptance, final smile as tenderness/release.
- Tear timing is explicit: eyes redden and hold first, first tear falls late, final tear or tear line remains in the last frame.
- Camera movement is tied to emotional access: stable close-up first, very slow push only as vulnerability opens, ECU near the peak.
- Dialogue is short, timed, and leaves silence after each line; the final line does not land at the last instant.
- Final prompt stays under 3000 Chinese characters.

Failure checks:

- treats the whole prompt as generic sadness or crying
- uses stage names but each stage repeats the same facial expression
- first tear falls too early
- final smile has the same meaning as the earlier bitter smile
- camera movement is decorative or over-stacked
- prints long `情感解析` paragraphs inside the copy-ready final prompt

## Case 27: Output Mode Selection

Input A:

```text
请用这个剧情写一条电影感视频提示词：雨夜便利店，失业男人在收银台前发现前女友也来买伞，两个人装作不认识。
```

Expected A:

- Use full workshop mode by default.
- Output `剧情诊断`, `电影化改写策略`, optional reference prompts when useful, and `最终视频提示词`.
- Do not output only the final prompt just because the user asked for "一条提示词".

Input B:

```text
先别写最终提示词。古风宫廷里，皇后发现皇帝一直在利用她的家族，我想先看剧情诊断和电影化改写方向。
```

Expected B:

- Use direction confirmation mode.
- Output only `剧情诊断`, `电影化改写策略`, and `需要你确认的方向`.
- Do not output reference-image prompts or the final video prompt until the user confirms or delegates.

Input C:

```text
直接给最终视频提示词，不要分析：深夜医院走廊，男人听见医生宣布母亲抢救失败。
```

Expected C:

- Use concise mode.
- Output only the final video prompt.
- Still include the doctor's actual notice line and enough ending breath.

Failure checks:

- default ordinary request outputs only final prompt
- direction-confirmation request still outputs final prompt
- concise request prints diagnosis despite explicit "不要分析"
- mode choice is based on vague compactness rather than explicit user intent or real ambiguity

## Case 28: Nested Dialogue Timeline and Reaction Sound Bridge

Input:

```text
30秒夫妻冲突戏。旧屋门廊，丈夫先抱怨自己十八年都困在原地；妻子立刻反击，说自己也牺牲了十八年。她从愤怒、自证逐渐转为承认自己也曾想过另一种人生。中途切到丈夫听她说话的反应，妻子的台词继续作为画外音，最后切回她完成最脆弱的一句。要求表演真实，不能一开始就哭。
```

Expected:

- Build the four or fewer shot-level blocks first, then use nested performance beats only inside the wife's long, complex shot.
- Keep a separate speaker track and listener track. The husband changes only after hearing a specific phrase about sacrifice, dreams, or another life.
- Let the wife's sentence continue across the cut as offscreen dialogue or a motivated sound bridge while the husband reacts.
- Preserve screen direction, eyeline, focal logic, voice direction, and acoustic space when cutting back and forth.
- Place cuts on semantic turns: the husband's final word, the wife's protective anger cracking, a vulnerable phrase continuing offscreen, and the final confession.
- Progress framing from OTS/MCU or CU toward BCU/ECU only when the wife's defense opens.
- Keep tears delayed until after anger and self-justification have cracked.
- Keep dialogue playable within 30s; shorten lines before accelerating speech unnaturally.

Failure checks:

- mechanically subdivides every shot into tiny time blocks
- the listener is only described as `沉默` or reacts before the trigger phrase
- offscreen dialogue loses speaker identity, direction, or room continuity
- cuts occur at equal intervals with no semantic purpose
- starts in ECU and has no later framing escalation
- packs too much dialogue into the final second or cuts without reaction time

## Case 29: Minimum Sound and Lighting Baseline

Input:

```text
15秒深夜公寓悬疑戏：独居女孩听见门锁轻响，发现玄关地面多了一把陌生钥匙。她没有尖叫，只屏住呼吸，慢慢看向黑暗走廊。要求写实、克制、不要配乐。
```

Expected:

- Establish one motivated light baseline, such as a warm interior practical light against cooler corridor spill, with a stable source direction.
- Use 2-4 concrete sound anchors, such as lock click, refrigerator hum, bare-foot friction, breath, or a distant elevator.
- Let the key discovery change the sound field through narrowing, muffling, or isolated silence rather than adding generic suspense music.
- Mention shot-local light changes only when the door gap, hallway spill, phone screen, or character movement changes what is illuminated.
- Keep skin tone, eye catchlight, shadow direction, room tone, and acoustic space continuous across cuts.
- Use a compact `整体声音与光影` block or place the same information concisely in the opening summary when the prompt is short.
- Leave an audible and visual ending residue: held breath, corridor hum, key reflection, or distant elevator sound.

Failure checks:

- only says `电影感光影` or `沉浸式音效`
- gives no believable light source or sound bed
- adds dramatic BGM despite the request
- changes light direction between shots without an on-screen cause
- repeats a full lighting breakdown in every shot
- ends at the discovery with no sound tail or visual afterimage

## Case 30: Short-Drama Hook Diagnostic Boundary

Input A:

```text
做成25秒强钩子悬疑短剧：深夜，快递员送来一个写着明天日期的包裹。独居女孩想在男友回家前打开，门外物业却打电话说今晚没有快递员上楼。盒子里是男友正在响铃的手机，屏幕显示来电人正是女孩自己。结尾要让人想继续看。
```

Expected A:

- Activate the short-drama hook and narrative-drive diagnostic because the user explicitly asks for a strong-hook suspense short.
- Diagnose the existing anomaly, immediate goal, active obstacle, information reversal, and unresolved question without insisting on a separate deadly rule.
- Preserve the supplied plot. Do not add a hidden murderer, supernatural identity, countdown, or new culprit unless the user delegates further invention.
- Translate the functions into visible beats: future date, her attempt to open the parcel, the property call, the phone inside, and her own incoming caller identity.
- Use no more beats than can play naturally in 25s, including dialogue/reaction and 1-2s ending residue.
- End with a completed reveal and held reaction while the larger question remains open; do not cut off the phone line or box-opening action halfway.

Input B:

```text
8秒固定镜头情绪特写：母亲看到儿子的大学录取通知书，先不敢相信，确认名字后笑着落下一滴泪。全程无台词，安静克制。
```

Expected B:

- Do not activate the short-drama hook formula merely because the video is short.
- Do not invent an anomaly, deadline, fatal rule, obstacle, identity reversal, or cliffhanger.
- Preserve the performance-led emotional arc and use the micro-expression close-up system.

Failure checks:

- requires all six narrative functions for Input A
- silently rewrites the supplied culprit, identity, relationship, or ending
- mistakes an unresolved answer for an abrupt unfinished action
- adds a twist or danger to Input B
- turns every emotional change into a plot reversal

## Case 31: Dense Dialogue, Interruption, and Playability Boundary

Input A:

```text
做成30秒双人情感对话。姐姐发现弟弟准备替父亲承担一项会毁掉前途的责任，她越说越快，害怕一停下就无法阻止他；弟弟始终低声、礼貌，用“没关系”安慰她，却多次在“我”字上卡住。两人可以温和抢话和短暂重叠，以下关键台词必须完整保留。镜头不要花哨，重点是原生对白、口型、声音和听者反应。
```

Expected A:

- Establish a scene-level performance contract: her speed comes from fear of losing the chance to stop him; his politeness protects him from collapse and tries to reduce her guilt.
- Treat dense dialogue as a playability question rather than applying an automatic word-count cut. Preserve all required lines if local acceleration, motivated overlap, and simplified visual staging allow complete delivery.
- Lock distinct voice identities and temporary vocal states across shots.
- For each interruption, identify the semantic entry trigger, relative volume, brief overlap, who yields, and the interrupted mouth/breath state.
- Protect intentional failed `我—` starts from smoothing, completion, comic repetition, or audio-glitch behavior.
- Use a dialogue-first priority ladder; simplify shot count, camera movement, secondary gestures, and environment activity before proposing dialogue cuts.
- Carry one gesture continuously across cuts, such as his hand rising, hovering, then losing strength and falling. Preserve the relationship's no-touch distance if established.

Input B:

```text
15秒低声告别戏：两个人必须缓慢说完十二句长台词，每句之间停顿一秒，每句都要有吞咽、落泪、对方反应和一次运镜，最后一句说到最后一帧。所有内容都不能删。
```

Expected B:

- Do not claim the scene is playable merely because all dialogue is marked mandatory.
- Diagnose the concrete conflict among slow delivery, twelve one-second pauses, repeated physiological actions, listener reactions, camera moves, and no ending residue.
- First propose simplifying camera and repeated gestures, but recognize that those reductions cannot recover enough time for twelve long lines and pauses.
- Explain the remaining conflict and recommend splitting into multiple clips or ask whether the user prefers preserving every line or preserving the 15s limit. Do not silently edit key dialogue and do not accelerate it unnaturally.

Input C:

```text
结尾她想说“其实我一直——”，却因为终于看见对方已经明白而主动停住。不要补全后半句；用她未闭合的嘴唇、缓慢呼气和对方抬眼回应完成结尾。
```

Expected C:

- Allow the unfinished line because refusing or no longer needing to finish is the completed dramatic action.
- State why speech stops, prevent automatic completion, and hold the mouth, breath, gaze, listener response, or silence long enough to read.
- Do not place the dash at the last frame with no consequence; reserve visible and audible aftermath.

Failure checks:

- compresses Input A only because its word count exceeds a generic speech-rate estimate
- turns overlap into clean alternating turns or mutes the first speaker abruptly
- repeats a cross-cut line in full after the edit
- converts failed speech into comic stuttering or mechanical loops
- accepts Input B without identifying the genuine timing contradiction
- silently deletes mandatory lines from Input B
- treats Input C as permission for an accidental mid-line cutoff

## Case 32: Knowledge State, Non-Human Performance, and Behavioral Payoff

Input A:

```text
30秒写实车站剧情：一只年迈的搜救犬多年后突然听见已经离开的训导员声音。它先怀疑、确认，再慢慢靠近；最后声音消失，它不再继续盯着站口，而是在原来的等待位置趴下。不要把狗拍成人脸式哭泣。
```

Expected A:

- Use species-appropriate performance: ear orientation, half-turn freeze, sniffing, breath, tentative paw placement, tail/spine tension, weight shift, slow aged approach, contact release, and final resting posture.
- Preserve age and locomotion limits; recognition may restore intent but not youthful speed or agility.
- Do not use human tears, smiles, theatrical nodding, or anthropomorphic sobbing.
- Adapt the relationship axis to unequal height using hand, coat, waist, ear, or back foreground anchors rather than forcing a human shoulder-level reverse shot.
- Build a behavioral payoff: habitual watching of the entrance is established, then the final choice not to look back and to lie down proves waiting has ended.

Input B:

```text
25秒科幻情感戏：婚礼前夜，年轻女人开门遇见一位陌生老人。老人提前说出她下一秒会做的生活习惯，动作在画外发生；她从声音和他的神态中逐渐猜到，他可能来自自己的未来。不要解释穿越原理。
```

Expected B:

- Track knowledge state: she begins with no recognition, observes a specific prediction and verification, forms a tentative hypothesis, then receives only enough confirmation to ask a personal future question.
- Keep audience knowledge and character knowledge distinct; do not let her name the relationship before credible evidence arrives, and do not let the visitor explain the mechanism.
- Use prediction -> waiting gap -> offscreen verification -> reaction -> revised hypothesis.
- Keep the camera on her face if the realization matters more than showing the habitual hand action; use precise contact sound, brief offscreen eyeline shift, breath stop, and renewed gaze as proof.
- Select questions from character values: once identity is sufficiently clear, move from `who are you` to what the shared life meant rather than continuing mechanical exposition.

Input C:

```text
20秒深夜小餐馆告别：女人一直想替对面的男人整理歪掉的衣领，却顾及两人的关系边界没有碰他。结尾男人自己整理好衣领，随后把桌上的钥匙推回给她。背景仍有服务员收桌和远处客人低声交谈。
```

Expected C:

- Establish the withheld collar gesture early and preserve it as a relational boundary rather than adding a random symbolic action only at the ending.
- Pay it off through transfer/recontextualization: he completes the grooming action himself, then the key movement becomes the decisive relationship action.
- Keep background workers and guests on plausible independent routines; they do not stop, stare, gather, or mirror the couple's emotion.
- Use a subjective sound arc: ordinary restaurant room tone -> distant ambience recedes after the key decision -> cloth/key/table contact becomes close -> room tone returns after the private beat.

Input D:

```text
列车从两人和摄影机之间驶过，遮挡期间其中一人消失；列车离开后，另一人仍保持原来的站位和视线方向，只剩手里刚刚接过的旧车票。
```

Expected D:

- Allow the train as a motivated foreground occlusion because it belongs to the space and carries a visible path, parallax, wind pressure, reflection, and synchronized sound.
- Preserve camera side, interaction axis, screen direction, lighting, remaining character pose, gaze, hand/prop state, and the first visible post-occlusion composition.
- Do not use the cover to hide unrelated character drift, costume change, flipped geography, or an unexplained camera teleport.

Failure checks:

- gives Input A human tears, smiling, nodding, or sudden youthful movement
- lets a character know identity, death, timeline, or relationship before receiving evidence
- cuts to every object action even when the observer reaction carries the story
- asks generic exposition questions that ignore character priorities
- introduces a new symbolic ending action with no earlier setup
- freezes or redirects all background people toward the protagonist
- turns subjective sound narrowing into arbitrary total silence
- uses foreground occlusion as an unmotivated blackout or continuity reset

## Case 33: Generated Fight Result Surgical Repair

Input:

```text
上一版12秒仓库格斗已经生成：两名成年女性的脸、服装、仓库站位、冷白顶灯和手持摄影都很好。问题只有反摔动作：A没有先降低重心和建立抓握，B就突然翻到地上，右手护腕还从B手上跳到了地面。只修动作和护腕连续性，其他都不要改。
```

Expected:

- Activate generated-result surgical repair rather than rewriting the whole fight.
- Diagnose at most three dominant failures: missing grip/level-change/momentum causality, teleport-like throw, and wrist-guard state discontinuity.
- Lock the successful identities, wardrobe, warehouse layout, fighter positions, cold overhead light, and handheld shooting condition.
- Repair only the attack-defense-counter chain: establish grip, level change, weight transfer, pivot, fall path, landing/recovery, and the wrist guard's holder/contact/final location.
- Keep the original duration and action count playable; do not add a new fighter, weapon, light design, slow-motion showcase, or unrelated camera move.

Failure checks:

- rewrites faces, costumes, warehouse, light, or the accepted camera style
- adds generic negative constraints without repairing throw mechanics
- fixes the throw but leaves the wrist guard teleporting or duplicated
- expands one failed beat into an overloaded new fight sequence
- claims the repaired prompt proves the next generated video will succeed

## Case 34: Single-Variable Camera Revision

Input:

```text
上一版15秒厨房夫妻对话的台词、口型、表演、站位、暖色吊灯和结尾沉默都满意。只把正面固定机位改成从厨房门框后方略带遮挡的观察机位，仍保持原来的180度轴线和人物左右关系，其他内容不变。
```

Expected:

- Treat the request as a single-variable camera revision.
- Preserve dialogue wording/order, lip-sync, performance timing, blocking, character screen-left/right, practical light source, sound bed, and ending silence.
- Change only the physically dependent camera clauses: witness position behind the doorway, height/distance, plausible foreground doorframe occlusion, framing, and focus behavior.
- Keep the doorway observation position physically compatible with the existing axis; do not cross the axis or move either character merely to beautify the composition.
- Do not introduce surveillance, horror, voyeurism, new props, new lighting, or a different story interpretation unless the user asks for it.

Failure checks:

- rewrites dialogue, acting, light, sound, or ending
- changes character blocking or flips screen direction without necessity
- treats the doorframe as a decorative overlay with no physical camera position
- adds unrelated handheld movement, lens flare, fog, or dramatic color grading
- outputs several camera alternatives instead of one resolved revision

## Case 35: Production-Path Routing Without Extra Friction

Input A:

```text
先给我生成人物和场景参考图提示词，图片满意后再写视频提示词：宋代婚礼前夜，新娘独自在喜房里拆下凤冠。
```

Expected A:

- Enter the reference-first path without asking whether the user wants references.
- Output only the current-stage asset plan and needed image prompts; do not pretend the images already exist or append a reference-driven video prompt.

Input B:

```text
直接给8秒视频提示词，不要参考图：清晨厨房，男人把煎糊的鸡蛋偷偷倒掉，妻子在门口看见却忍住笑。
```

Expected B:

- Enter the direct-video path without a route question.
- Output a self-contained prompt and no reference-image section.

Input C:

```text
宋代家族群像连续短片，三名主要人物会在正厅、婚房和祠堂反复出现，服饰身份和空间方位必须稳定。
```

Expected C:

- Because the user has not chosen a route and the task has high drift/reuse cost, ask one concise production-route question.
- If direction selection is also needed, combine the choices into one checkpoint rather than asking twice.

Failure checks:

- asks Inputs A or B to choose a route already specified
- dumps complete reference prompts and a complete video prompt for Input A
- silently defaults Input C to a large mixed package
- adds a production-route checkpoint to a simple low-drift direct request

## Case 36: Minimal Reference Asset Set for Multiple Characters and Scenes

Input:

```text
连续三段宋代家庭故事，有夫妻两位主角、两个只出现一次的仆人，正厅会反复出现，后院只出现一次；第一段先制作参考图。
```

Expected:

- Create individual identity references for the two recurring principals.
- Create a clean scene plate for the recurring main hall when its topology matters.
- Do not automatically create individual identity references for both one-off servants or a clean plate for the one-off backyard.
- Explain briefly which assets are not generated and why.
- Keep the current generation stage to roughly 1-3 active references; if more are truly needed, batch them through an asset plan.

Failure checks:

- creates a reference for every named person and location
- generates identity, relationship, scene, prop, first-frame, and tail-frame references by default
- includes all later locations before the current clip needs them
- omits recurring principal identity or recurring location control

## Case 37: Reference Authority and Static Deduplication

Input:

```text
我已经生成了三张图：参考图1是女主定妆，参考图2是宋代厅堂空景，参考图3是男女主隔桌而坐的首帧。请基于这三张图写15秒对话视频提示词。图片里外貌、服装、场景和灯光都满意，不要重新设计。
```

Expected:

- State a compact mapping: image 1 controls the woman's identity/costume, image 2 controls layout/light, image 3 controls start-frame relationship geometry.
- Treat the supplied visual facts as locked and do not repeat full face, costume, architecture, palette, or lighting descriptions.
- Focus the video prompt on dialogue order, lip-sync, gaze, breath, body/contact changes, camera behavior, sound, and ending state.
- Keep only minimal role/position/prop bindings needed to interpret motion.

Failure checks:

- rewrites the woman's full appearance or proposes a new costume
- introduces a competing room layout, palette, light direction, or first-frame pose
- omits reference mapping so the three images compete for authority
- removes so much binding information that character identity, position, or prop ownership becomes ambiguous

## Case 38: Explicit Timed Delta From a Reference

Input:

```text
参考图里新娘穿着完整红色婚服，视频12秒时她转身，红色外袍从肩上滑落，露出里面早已穿好的白色丧服；外袍最后挂在左肘。其他外貌和房间都保持参考图。
```

Expected:

- Preserve the reference as the starting state.
- Describe the wardrobe change with time, physical cause, contact path, revealed layer, and final state.
- Do not describe the character as wearing only white at the start.
- Avoid repeating unchanged face, hair, room, and lighting descriptions.

Failure checks:

- contradicts the image at the opening
- makes the outer robe disappear, teleport, or return to its initial position
- describes the change without cause or endpoint
- redesigns unrelated static details

## Case 39: Separate Reference-Driven and No-Reference Versions

Input:

```text
这个镜头我要两种版本：一种绑定我现有的人物和场景参考图，另一种不用任何图片也能直接生成。
```

Expected:

- Output two clearly labeled prompts: `参考图驱动版` and `无参考图直出版`.
- The reference-driven version uses mappings and dynamic differences without full static repetition.
- The no-reference version restores the necessary identity, setting, costume, prop, light, and first-frame anchors.
- Both preserve the same story action, timing, dialogue, and ending, while differing in static-information density.

Failure checks:

- gives one ambiguous prompt claimed to work equally well in both modes
- leaves nonexistent reference-image language in the direct version
- fully repeats all static descriptions in the reference-driven version
- changes the story or performance between versions without being asked

## Case 40: Reference-First Continuation Uses Actual State

Input:

```text
上一段已经用参考图生成成功。结尾女主左侧发簪掉落，衣袖被雨打湿，信落在石阶第二级。继续下一段，人物、庭院和灯光都不要重做。
```

Expected:

- Reuse the existing identity and scene references rather than regenerating them.
- Bind the next prompt to the actual previous ending state: missing left hairpin, wet sleeve, letter on the second step.
- Create an updated-state reference only if the changed state will recur or cannot be held reliably through the continuation prompt.
- Focus the new prompt on the next temporal action and emotional turn rather than repeating the full visual bible.

Failure checks:

- restores the hairpin, dries the sleeve, or moves the letter without visible action
- outputs a new generic character or courtyard reference
- repeats the complete identity and scene description
- treats the continuation as an unrelated direct-video prompt

## Case 41: Inspiration Reference vs Production Reference

Input:

```text
我给你两张图：图A是一张经典电影截图，我只喜欢它用门框压住人物的构图；图B是我已经生成满意的宋代女主定妆图。请规划喜房首帧参考图，女主身份必须稳定，但不要照搬电影截图。
```

Expected:

- Classify image A as `灵感参考图` controlling only the declared composition method.
- Classify image B as `生产资产参考图` controlling the woman's identity and approved costume state.
- Build a new, story-specific room, blocking, props, and action rather than copying the source still's cast arrangement, complete topology, palette, or story outcome.
- State the authority of each image so composition inspiration does not overwrite identity and identity reference does not freeze the new first-frame composition.

Failure checks:

- treats the movie still as authority over identity, exact layout, action, and palette
- reproduces a recognizable complete shot or merely swaps the actor
- lets the generated identity image dictate an unrelated pose or camera position
- fails to state which image controls which field

## Case 42: Type-Specific Reference Prompt Density

Input:

```text
为宋代夫妻争执戏制作四类参考图：妻子定妆、正厅空景、夫妻隔桌关系图、桌上和离书关键道具图。图片之后要用于生成视频，请避免提示词过载。
```

Expected:

- Wife identity prompt uses 4-6 stable identity/costume anchors and one emotional baseline, with no husband or relationship action.
- Clean hall prompt prioritizes 4-6 topology/light anchors, entrances/exits/action path, one primary source, and only 2-3 causal environment traces; it contains no people.
- Relationship prompt uses one relationship axis, left/right positions, distance/eyelines, one contact or no-contact state, and one visual center.
- Prop prompt locks the letter's material, scale, orientation, readable feature when essential, wear/state, and placement without an elaborate unrelated scene.
- Each prompt requests one standalone frame and one composition; no grid, collage, model sheet, or multiple views unless explicitly requested.

Failure checks:

- applies the same long template to all four asset types
- places the husband or interaction language inside the wife's identity reference
- clutters the clean hall with irrelevant objects or several light effects
- gives the relationship frame several actions or time beats
- produces a four-panel sheet instead of four independently usable prompts
- forces 21:9, English, or a particular image model without user request

## Case 43: Surgical Repair of a Generated Reference Image

Input:

```text
这张宋代女主参考图的脸、发髻、服装颜色、人物比例、背景和窗侧光都满意。只有右袖口错误，做成了现代宽松喇叭袖；请只修成窄口交领袍袖，不要重做其他部分。
```

Expected:

- Inspect the actual image when it is available and identify the sleeve construction as the dominant failed field.
- Output `保持不变`, `只修改`, and `禁止连带变化`.
- Preserve face, age, hair, approved garment body/color, body proportions, composition, camera, background, and source-light direction.
- Change the right cuff and only its physical dependents such as adjacent folds and wrist occlusion.
- Do not claim the repair succeeded before the revised image is generated and inspected.

Failure checks:

- rewrites the whole character prompt or redesigns the costume
- changes face, hair, color, pose, camera, background, or light
- changes the cuff without repairing directly connected folds/contact
- adds a long generic negative list unrelated to collateral drift
- reports success from the repair instruction alone

## Case 44: Actual Reference Supremacy, Cleanliness, and Physical Feasibility

Input:

```text
我原来的首帧提示词要求桌上有压纸木条，但实际生成的夫妻隔桌图里只能清楚看到和离书，没有木条；右下角还有生成平台水印。妻子坐在带扶手的椅子上，右手放在膝上。请根据实际图片写15秒图生视频提示词：她把和离书推给丈夫，然后起身离开。
```

Expected:

- Treat the actual pixels as authoritative and do not inherit the absent/unclear paperweight from the earlier image prompt.
- Flag the visible watermark before production and recommend a clean/cropped/repaired reference; do not claim that `不要水印` will reliably erase it.
- Reconstruct the start geometry: right hand travels from lap to paper, body has a reachable path, and the chair arms affect how she stands.
- Write the document contact as approach -> touch/support -> frictional push -> release -> visible endpoint; do not make the paper jump or slide together with an absent weight.
- Let her use the visible armrest or another physically supported motion to stand; preserve the clear exit path and husband/document continuity.
- Replace arbitrary centimeter precision with a visible event unless exact measurement is story-critical.

Failure checks:

- imports the paperweight from the old prompt despite its absence in the selected image
- relies only on a negative prompt to remove the embedded watermark
- makes the hand teleport from lap to document or the document move before contact
- asks her to press through the chair, table, or armrest, or gives no viable standing/exit path
- claims the reference or final video is clean/successful without a revised generation result

## Case 45: First Frame Must Not Freeze Cinematic Coverage

Input:

```text
三张实际参考图分别锁定宋代妻子身份、正厅布局，以及夫妻隔桌而坐的首帧关系。15秒无台词：妻子把和离书推过去，丈夫伸手却停住，她看他一眼后起身离开，最后留下空椅和丈夫。首帧是正面双人中景，但不要整段都保持这个景别；根据故事切换景别并选择合适运镜。
```

Expected:

- Bind the relationship image as the exact opening state only; preserve identities, room topology, axis, positions, document state, and light across later views.
- Choose a multi-shot relationship-drama structure rather than defaulting to a static one-take.
- Use motivated coverage, for example: opening `MS/MLS` relationship geography -> document/hand `CU` with match-on-action -> husband's `CU/BCU` stopped reach and reaction -> wider or moving follow shot for her stand/exit -> held aftermath on empty chair/document/husband.
- Make every cut or move reveal action, reaction, power change, or aftermath; do not add decorative angles.
- Use meaningful shot-size contrast and at least a 30-degree horizontal change when cutting around the same interaction; preserve the 180-degree axis and eyelines.
- Widen or pull back before the full-body stand/exit if needed, and give the ending 1-2 seconds to read.

Failure checks:

- treats the first-frame composition as the required framing for all 15 seconds
- labels the result `一镜到底` without a story reason or user request
- changes shots but repeats nearly identical medium framing and angle
- adds cuts or camera moves with no change in information, emotion, action readability, or aftermath
- loses identity, room geometry, screen direction, document position, or light continuity after leaving the opening view
- keeps a close framing during the stand/exit so the body action becomes cropped or physically unclear

## Case 46: Camera-Movement Library Is Selected by Story Function

Input:

```text
12秒写实悬疑：女人沿酒店走廊走向自己的房门，身后电梯突然打开，她从门牌反光里看见一个人影跟出来。不要我指定运镜，你根据剧情设计，提示词仍以中文为主。
```

Expected:

- Read the camera-movement library because movement and spatial reveal carry the suspense.
- Select only the movements that serve the route and reveal, such as a controlled `Follow Shot / OTS` for approach plus one motivated `Pan`, `Slider`, or focus/cut response for the reflected figure.
- For every selected move, state the readable start subject, physical path/direction, speed, newly revealed information, and settled endpoint.
- Keep the corridor, door, elevator, reflection, travel direction, and screen axis coherent; do not let the camera pass through walls or the character.
- Keep action and story instructions in Chinese; retain English only for useful cinematography terms and abbreviations.
- Use no more than the few movements the 12-second action can carry.

Failure checks:

- lists several of the 46 moves as alternatives instead of making a director choice
- stacks `Orbit`, `Whip Pan`, `Crash Zoom`, `Drone`, and `Handheld` for style alone
- names a movement without start, path/direction, speed, story result, or endpoint
- switches to an English prompt paragraph copied from the library
- sacrifices corridor geography, reflection logic, or reaction time for camera spectacle

## Case 47: Observable Emotion Library Without Stock Acting

Input:

```text
10秒近景：女人对母亲说“我过得很好”，先挤出一个紧张假笑；母亲把她退回来的车票放在桌上后，她的笑消失，愧疚地低下眼睛，却没有哭。表演自然克制，提示词用中文。
```

Expected:

- Use `紧张假笑` as the initial protection and `愧疚` as the triggered destination rather than mixing several unrelated emotions.
- Keep only 2-4 decisive cues in each playable phase: for example mouth smiling while eyes remain flat, a hard swallow or brief gaze drop; after the ticket lands, the smile releases, gaze lowers, and speech fails or breath changes.
- Tie the transition to the visible/sounding ticket contact and preserve the exact dialogue, listener timing, and no-cry boundary.
- Write onset, trigger, change, and held aftermath; do not display the final guilty face from the first frame.
- Keep the final performance direction in Chinese. Do not print English emotion labels, intensity tags, library analysis, or an AU/FACS dump.

Failure checks:

- copies the complete stock modules or uses every listed facial/body cue
- adds shock, terror, sobbing, flirtation, or another unrelated emotion
- makes her cry despite the explicit boundary
- describes only abstract `紧张、愧疚` without visible eyes, mouth, breath, gaze, hand, or posture evidence
- outputs the emotion library's English labels or long English acting sentences

## Case 48: Aspect-Ratio Routing Without Repeated Questions

Inputs:

```text
A：直接给我9:16竖屏提示词：女孩在电梯里发现镜中有人站在她身后。
B：继续上一段，沿用已经确认的竖屏人物和场景参考图。
C：8秒单人厨房近景，男人偷偷倒掉煎糊的鸡蛋；没有画幅要求。
D：先给宋代夫妻隔桌和离戏制作正式场景和首帧参考图；没有说明横竖屏。
```

Expected:

- A enters the vertical system directly without asking about ratio.
- B inherits the confirmed vertical ratio without asking again.
- C defaults to 16:9 horizontal and proceeds because the low-risk single-subject action does not justify a checkpoint.
- D asks once because formal scene/relationship/first-frame assets and two-person table blocking are costly to redo; combine this with any existing direction or reference-route confirmation.
- If the user delegates D, use 16:9 by default unless an actual vertical production asset or explicit vertical delivery context exists.

Failure checks:

- asks A or B to choose a ratio already given or inherited
- interrupts C with an unnecessary aspect-ratio question
- generates D's composition-controlling assets before resolving a materially consequential ratio
- creates a separate aspect-ratio question immediately after another confirmation round
- assumes a platform ratio without the user specifying its intended format

## Case 49: Vertical Two-Person Reference-First Relationship Scene

Input:

```text
9:16竖屏，宋代夫妻隔桌而坐。先做正厅场景和双人首帧参考图，图片满意后生成15秒视频：妻子推过和离书，丈夫伸手停住，她起身离开。不要把横屏画面直接裁窄。
```

Expected:

- Read the vertical adaptation and reference-first workflow; state 9:16 in composition-controlling scene/first-frame prompts.
- Recompose the hall around a central depth/action corridor, readable table/document, viable standing/exit path, and vertical source-light geometry.
- Avoid two equally small figures pushed to opposite edges; use staggered depth, height, `OTS`, diagonal relationship, or another narrow-frame solution while preserving the axis and document ownership.
- Keep face, hands, document, chair support, head/foot clearance, and exit visible where their actions occur.
- Stage 1 stops after the reference plan/prompts. After actual vertical images are supplied, the video may use motivated shot-size changes rather than freezing the first-frame composition.

Failure checks:

- writes a horizontal side-by-side composition and merely appends `9:16`
- crops out a spouse, the document, chair arms, or the exit route
- creates composition-controlling references in conflicting ratios
- gives a tight portrait first frame that cannot support pushing, standing, and leaving
- outputs the final video prompt before actual images are generated without an explicit complete-package request

## Case 50: Vertical Full-Body Action and Camera Travel

Input:

```text
12秒9:16竖屏：年轻女人从楼梯下方跑上来，在平台停住，抬头看见楼上门缝透出光，转身继续向上。要紧张但动作清楚，根据剧情选择运镜。
```

Expected:

- Use stairs, height, destination, and upper/lower frame relationships as meaningful vertical geography.
- Choose a physically plausible combination such as low `Follow Shot`, controlled `Tilt Up`, `Pedestal/Crane`, or a motivated cut; do not use vertical movement merely because the canvas is tall.
- Maintain head/foot room and the travel direction; widen or reframe before the stop/turn so the full-body mechanics remain visible.
- Keep horizontal travel short, the door-light destination readable, and the final upward direction continuous.
- Preserve action time and ending breath rather than stacking camera techniques.

Failure checks:

- keeps a tight face shot while demanding running, stopping, turning, and climbing
- loses feet, stair edges, landing, or door destination
- adds `Orbit`, long lateral tracking, drone movement, and whip pans without story function
- reverses travel direction or relocates the light/door between shots
- treats 9:16 as a suffix instead of a composition and movement constraint

## Case 51: Sustained Body-Mounted Camera and Repeated Recovery

Input:

```text
20秒、16:9、全程身体固定机位、一镜到底。快递员抱着包裹穿过走廊，两次伸手想敲门又收回；第二次听到门内自己的名字后才真正敲响。头和手可以自然动，始终看到关键动作。直接给视频提示词，不要配乐。
```

Expected:

- Accept the sustained Snorricam request without imposing a short psychological insert or a cut.
- Bind the camera to the torso, allow independent head/arm motion, and frame the hand path and supported parcel.
- Preserve visible withdrawal and a changed trigger for renewed action; clarify which hand supports the parcel.
- Background motion follows torso movement and settles with it; no independent orbit, push or zoom.

Failure checks:

- freezes the head and hands along with the torso, hides withdrawal, or loops equal gestures without motive
- drops/transfers the parcel invisibly or adds an unrelated threat/music

## Case 52: Matched Memory Cut With Intentional State Change

Input:

```text
12秒，两镜。女孩把旧网球滚到老犬脚边，球停住。保持球的位置和低机位，硬切到她记忆里的晴天球场，同一只犬年轻健康，上前叼球。不要渐变，不要解释性旁白，直接给提示词。
```

Expected:

- State the matched ball position/camera and deliberate location, light and age changes across the hard cut.
- Treat the change as the supplied memory, not present-time healing or resurrection.
- Preserve identity without freezing temporary age/state or generating extra reference assets by default.

Failure checks:

- morphs between states, treats the cut as an accidental continuity reset, or adds a supernatural rule

## Case 53: Environment-Driven Adjustment and Tone Boundary

Inputs:

```text
A. 12秒写实：服务员端着水杯穿过行驶中的列车，列车转弯，他扶住座椅恢复平衡，保住杯子，继续走。认真克制，无台词，直接给提示词。
B. 同一情节改成冷幽默：站稳后他看着仅剩一点水的杯子，停一下，说“还好，杯子没事。”直接给提示词。
```

Expected:

- A: carriage motion causes consistent body/liquid response; specify free-hand support, recovery and continued movement without inventing a crash or joke.
- B: show how water spills, retain the changed cup state, and reserve time for the pause, supplied line and understated aftermath.
- Keep no-music default and use scene sound; do not force slow motion, triumphant posing or a freeze.

Failure checks:

- cup refills or teleports, support uses an occupied hand, or environment motion has no effect on balance
- adds a comic line to A or rushes B's dialogue into an unplayable final instant

## Case 54: Direction Continuation and Reserved Approval

Run each variant with its own context:

```text
A. 直接给12秒悬疑视频提示词：夜班保安听到空电梯里传出自己的声音，按住关门键，声音却从身后响起。无配乐。
B. 同一剧情先给两个方向，等我选了再写提示词。
C. Previous exchange: assistant offered 1. 保持现实质感，不解释声音来源; 2. 加入梦境解释. User: 1，直接写12秒最终提示词。
D. 我要一个很震撼、很电影感的视频。
E. 我要一个很震撼、很电影感的视频。主角、场景和事件你决定，直接写12秒提示词。
```

Expected: A delivers one final prompt without a genre-driven checkpoint; B stops after directions; C follows option 1 without re-asking or inventing image approval; D asks only for missing story foundations; E chooses a coherent event and delivers. No camera/lens questionnaire.

Failure checks: uses suspense alone to stop A; writes B's final prompt early; loses C's choice; invents an unauthorized story for D; asks E to supply already-delegated details.

## Case 55: Agent Capabilities and Object-Specific Approval

Run each variant independently; capability fixtures are evaluator controls, not additional user requests.

```text
A. 图片我已经满意了，请按这张首帧写15秒视频提示词：妻子推过和离书，丈夫伸手停住，她起身离开。
B. 先给妻子定妆图和正厅空景的图片提示词，不要实际生成图片。
C. 请生成妻子定妆图，我看过满意后，你再写视频提示词。
D. 按刚才选定的参考图优先路径继续。
E. 请生成一张成年女子在空房间门口停步的首帧图，检查后直接继续写8秒视频提示词，不需要我中途选图。
```

Fixtures and expected behavior:

- A1: supply a readable approved image of two adults across a table, a document, armchairs and a visible exit. Inspect actual pixels, then write the prompt; do not regenerate the reference or repeat route/approval questions. Do not assume a paperweight absent from the image.
- A2: same user request, but host image viewing is unavailable. State the specific visual facts needed for reach/exit/contact; do not claim pixel inspection. Any useful provisional draft must identify its description-based, unverified status.
- B: even if a generation tool exists, output only the two image prompts; no media calls.
- C1: an authorized generation tool exists. Generate and inspect, then wait for the reserved user approval; do not write the final video prompt yet.
- C2: no generation tool exists. Supply the usable image prompt, explain actual generation remains undone, and preserve the user's later image-approval step.
- D: context confirms only the route, with no actual images or media-generation request. Supply missing Stage 1 plan/prompts; do not treat route selection as permission to generate or as image approval.
- E: authorized generation and image viewing are available. Generate, inspect, then continue the video prompt if the result supports it; do not add a user image-selection gate. A tool success alone is not a quality pass.

Failure checks: fabricates image facts, uses a named tool as a mandatory dependency, generates media for B/D, bypasses C's approval, stalls E for an invented gate, or calls prompt text a completed media edit. With real paid/external tools, run only within evaluator authorization; otherwise mark the tool branch not tested rather than claiming a simulated call succeeded.

## Case 56: Full Coverage, Stage Completion, and Hard Conflict

```text
A. 把以下故事完整改编为三条8秒视频提示词，直接交付全部。第一条：成年女儿在旧屋发现未寄出的信。第二条：她到码头，把信交给等船的父亲。第三条：父亲看完信放下船票，与女儿一起走回城里。不要新增人物或对白。
B. 同一故事只规划三段结构，等我确认再写视频提示词。
C. 15秒内保留以下12句对白，每句都必须完整说完，不能抢话、加速或拆片；每句之后还要停顿2秒。
```

For C, supply twelve distinct 10-15-character lines about a family farewell; preserve the exact same lines across runs. The twelve required pauses alone exceed the hard duration.

Expected: A provides all three prompts, causal continuity and an ending, not just a highlight or table. B supplies structure only and waits. C explains the concrete timing conflict and asks which hard constraint may change without silently deleting lines. Under an evaluator-imposed output limit for A, label the partial batch, remaining segment IDs and continuation state; do not call it complete. Repeat A with a longer prose expansion of the same three events above 3000 Chinese characters: length alone must not create a fresh approval gate.

## Case 57: Stylized 1v2 High-Intensity Fight Control

Input:

```text
30秒、16:9，高燃东方动作短片。一名成年女刀客对战两名成年男性：甲使用长柄重兵器正面纵向压制，乙使用双短兵器从侧后快速切入。第一帧直接开打，全程高压，结尾女主明确取胜；根据剧情决定是否致命，非血腥。直接给最终视频提示词。
```

Expected:

- Give all three fighters distinct combat-function signatures: weapon ownership/count, distance, attack plane, entry sector, rhythm, and recovery/re-entry behavior.
- Use one focal exchange per readable beat while assigning the non-focal attacker a purposeful state that shapes the next decision. Before one focal exchange fully resolves, preload the next threat through entry, weapon preparation, lane closure, shadow, sound, or forced eyeline so the pressure reads as 1v2 rather than alternating 1v1; do not demand simultaneous limb-heavy clutter.
- Isolate any story-critical disarm, weapon break/transfer/endpoint, incapacitation, or major environment collapse as one primary hard state change with trigger, visible process, result, and confirmation. Do not stack several unrelated hard state changes into one short phase.
- State or internally enforce the priority order: hard fighter/weapon/outcome invariants, 3-5 phase anchors, then optional move vocabulary. Do not require every named acrobatic move to appear.
- Allow more than 10 visible action changes in a 25-30s stylized fight when they remain organized inside readable phases. Do not split only because of a universal action-count threshold.
- Sustain pressure through changes in direction, height, distance, focal attacker, shot scale, and environmental consequence; keep one dominant emphasis device and a readable ending state.
- If the user explicitly chooses a fatal ending, preserve it through non-graphic defeat and aftermath. If no fatal outcome is requested, default to incapacitation rather than inventing death.
- Keep the final prompt below the 4000-character ceiling, normally within the 2200-3400 target, and simplify ornamental camera/particle language before action causality.

Failure checks:

- differentiates opponents only by names or clothing while their weapon use, attack line, and rhythm remain interchangeable
- lets one opponent wait motionless while the other completes a full exchange, or launches several unreadable contacts at once
- keeps the non-focal opponent offscreen/inactive through a long solo exchange with no entry, lane closure, shadow, sound, or other readable pressure cue
- combines a precise disarm, exact weapon landing, character fall, and large environment collapse in one short beat so the result cannot remain legible
- treats every move name as mandatory and loses fighter count, weapon ownership, geography, or recovery continuity
- mechanically splits the 30s prompt because it exceeds 10 action changes despite readable phase organization
- uses the same aerial or spinning texture repeatedly without changing the spatial problem
- silently changes a requested fatal result to non-lethal, or adds death when it was not requested
- claims prompt-text quality proves the generated video will execute every move

## Case 58: Retrospective Reversal and Dual-Meaning Montage

Input:

```text
30秒、16:9、写实科幻悬疑。失压飞船里，一名成年女宇航员意识模糊，仿佛回到家中陪女儿玩“追光点”：女儿追逐墙上移动的红点，扑向她怀里，两人贴着窗听彼此呼吸。结尾回到现实，观众才看清红点来自氧气警报，她伸手拥抱其实是在抓住破裂舱门，贴窗呼吸对应面罩漏气。不要旁白解释，不要血腥，用画面和声音让观众自己拼出真相。直接给最终视频提示词。
```

Expected:

- Use the retrospective-reversal system because the supplied ending is meant to change the meaning of earlier image and sound beats; do not add a route or direction checkpoint.
- Track objective spacecraft events, the astronaut's failing perception, and the audience's temporary home-memory belief separately. Her performance follows what she experiences, not what the audience will learn later.
- Build two or three deliberate paired beats: moving red play-light/alarm indicator, child rushing into an embrace/astronaut lunging for the damaged hatch, shared-window breathing/leaking mask or visor. Preserve useful composition, action phase, contact point, screen direction, or sound rhythm across each hard cut.
- Keep intentional differences clear: domestic warmth versus spacecraft emergency light, daughter versus hatch geometry, safe breath versus strained oxygen loss. Do not morph people into objects or treat changed states as accidental continuity errors.
- Use one compact dual-use sound motif, such as playful electronic pulses later recognized as the oxygen alarm, and breath/air texture that shifts from intimate to mechanically leaking. No explanatory voiceover or graphic bodily sound.
- Give camera stability a motivated arc, such as relatively stable domestic perception becoming subtly less stable as reality intrudes, then a locked or clearly readable final spacecraft reveal. Do not apply heavy shake throughout.
- Reserve enough final time for at least two decisive pieces of reality evidence and a held aftermath. The immediate action must complete; do not cut off at the first alarm reveal.
- Keep the final prompt within the 25-30s target/ceiling and prioritize belief control, matched action, sound, spatial clarity, and ending evidence over decorative effects.

Failure checks:

- creates a generic sentimental flashback whose actions, positions, or sounds do not correspond to the spacecraft reality
- reveals the complete spacecraft truth during the middle montage, eliminating the intended temporary audience belief
- introduces the alarm, hatch damage, or mask leak only at the ending with no earlier compatible cue
- uses particles, white flashes, dissolves, or morphing as the main transition despite the requested physical correspondences
- lets the astronaut consciously react to objective facts that her current perception has not admitted
- explains every pairing through narration, subtitles, or dialogue
- keeps the camera violently handheld from the first frame or sacrifices face, hatch, alarm, and mask readability
- adds gore, an unsupported death, another rescuer, or a new culprit
- ends immediately on the reveal without enough visual evidence or reaction time

## Case 59: Generated 1v2 Relay and Weapon-State Repair

Input:

```text
这是上一版30秒古代盐仓1女对2男打戏的实际生成结果：三个人物、盐仓空间、女主单刀、盐袋坠落、两名对手倒地和最后女主近景都很好；但前17秒经常变成甲打完再由乙上，真正夹击很少。乙原定双钩多数只看见一把，右钩被打飞钉进木柱没有出现；17-23秒同时写了缴械、钉柱、乙持剩余短钩追击、割绳、盐袋和网坠落、挡住甲，模型只保留了盐袋坠落。请按成片反馈补强或修复提示词，其他成功内容不要大改，也不要声称修改后已经生成成功。
```

Expected:

- Use generated-result surgical repair. Lock the proven identities, costumes, salt-warehouse topology/materials, female saber continuity, successful falling salt-bag payoff, defeat outcome, and final close-up unless the user asks to change them.
- Diagnose no more than three dominant failures: isolated focal exchanges that read as alternating 1v1, overloaded weapon-state control, and competition between the disarm and the environment payoff. Do not redesign the entire fight or add more moves, characters, camera tricks, or style words.
- Replace the vague demand that everyone remain active with explicit threat-handoff overlap: before the focal attacker finishes, the next attacker enters/preloads/seals a lane or applies one precise off-screen pressure cue, followed by a brief readable overlap and transfer.
- Preserve one primary hard state change per affected beat. Keep the successful salt-bag/net collapse separate from a precise disarm unless one directly causes the other and both the causal contact and final state remain readable.
- For a no-reference direct-video repair, either simplify the second opponent to one distinctive hook blade when two blades are not story-critical, or reserve a dedicated beat/reference asset for stable dual-wield and disarm continuity. Do not keep `dual wield + exact one-hand disarm + exact embed point + continued one-weapon pursuit` as a background instruction competing with the environment event.
- Write any retained disarm as trigger, visible release, weapon flight/landing, and short confirmation before the next event. If the user prioritizes the already successful environment payoff, it is acceptable to remove or relocate the disarm rather than preserving every original instruction.
- Report the revised prompt as text-checked only. A new generated-video review is required before claiming the repair worked.

Failure checks:

- removes successful environment, identity, outcome, or ending controls while trying to fix the relay problem
- keeps saying `三人持续运动` or `不要轮流攻击` without specifying how threat passes between attackers
- forces all three fighters into simultaneous contact and makes the action less readable
- adds more named techniques or camera moves instead of reducing the overloaded hard-state interval
- preserves dual wield, precise disarm, exact embedded endpoint, one-weapon continuation, major environment collapse, and another fighter's interception inside the same short beat
- claims the revised wording has solved the rendered result without reviewing a new video

## Case 60: Bridge Standoff Geography and Returning Defense

Input:

```text
写一段30秒、2.39:1写实夜景人质对峙提示词，参考图已经另行确认，直接给文本。B在桥栏内侧控制身前的C，两人背后是河面；A在桥面持枪警戒，D从A身后的警察区域赶来，群众更远。真正一镜到底，摄影机只在警察侧活动。先看B/C，再看A，D到场后形成A/D双人构图，最后回到B。D叫出熟人的名字，使B的愤怒短暂露出受伤，随后B重新用指责掩盖脆弱；不击发。夜景冷而通透，保留自然肤色。不需要重复参考人物外貌，也不要字幕和配乐。
```

Expected:

- Preserve world-space facing, captor/hostage contact and officer/crowd zones through the camera path. B's background remains railing/river; officer views may reveal the police/crowd side. Off-screen characters retain their positions. Use accessible camera movement without pretending a pan changes physical distance.
- Keep A's guard task active while D speaks; allow brief acknowledgment without turning both officers into a face-to-face conversation. Give C restrained, contact-compatible reactions rather than synchronized background acting.
- Tie B's exposed hurt and renewed defensive accusation to the name and relationship, with a small number of visible/vocal changes. Do not equate intensity with uninterrupted shouting or require this arc for every emotional scene.
- Make the night dark but readable through motivated light, retained midtones, natural skin and depth. Do not impose exact palette percentages, mandatory 65mm/aperture, scheduled focus errors, or a copied negative list.
- Fit speech, camera travel and ending into 30 seconds; report text checks separately from rendered-video verification.

Evidence scope: inspired by the user's supplied bridge-standoff prompt and reviewed video frames on 2026-09-17. Frames support attention progression, broad spatial relations, dark-background separation and changing facial performance. Exact audio overlaps, optical settings and absence of hidden cuts were not independently verified; visible subtitles/credit cannot be attributed to generation alone.

Failure checks: crowd migrates behind B; camera crosses the specified boundary; off-screen people relocate; A abandons guard merely because D speaks; every actor mirrors the same reaction; vulnerability automatically becomes a second shouting peak without motive; night detail is replaced by uniform cyan or crushed blacks; claims the new rule has passed video testing.

## Case 61: Bus-Station True One-Take Emotional Coverage Repair

Input:

```text
30秒横屏中文对白真正一镜到底，汽车站父女重逢。成片前十秒女子面部在画外，照片可见却没有压紧动作；扶垃圾桶接触不清；女子朝向让人看不出在看父亲；走近、递包、并肩离开的顺序可保留。请查看视频，区分提示词和模型问题并修复。希望照片手部特写起，后拉上移看犹豫的脸与远处父亲；叫“爸”后看父亲反应，再完整跟拍走近，近看对话，最后一起走。
```

Expected:

- Inspect available media with timestamped observations/limits; if unavailable, attribute descriptions to user. Do not claim unheard audio, exact anatomy hidden in blur, intrinsic model incapacity or guaranteed absence of cuts from sparse frames.
- Separate missing/conflicting direction from observed noncompliance. Do not assume the conversation draft equals the submitted prompt or invent responsibility percentages. Preserve successful story, appearance, setting and ending.
- Provide usable detail/reaction coverage and dwell, body/head/gaze toward father, response after call and compatible camera position.
- Distinguish focus from zoom and physical travel. Serialize detail, reveal, remote reaction, wide approach, handoff/reaction and departure; retain the entire approach. Do not lock a prime lens while ordering optical zoom.
- Give bin contacts distinct roles/support. Simplification to one lifter and a cleaner handling the lid is permitted only if exact joint lifting is not required and the change is disclosed. Do not hide all mechanics in blur.
- Record text validation separately from future media retest; new generation needs authorization.

Boundary probes:

1. `8秒固定全景，人物不走近，不要特写。` Preserve locked view and express emotion through posture/action; no forced photo, zoom, close-up or arc.
2. `两人必须同时扶桶。` Preserve shared lift with distinct upper handle/lower rim contact, grounded support and readable angle; do not substitute solo lifting.
3. `只改女子朝向，其他都满意。` Repair torso/head/gaze and necessary framing only; no new camera route, bin action, dialogue or wardrobe.
4. `只做远近移焦，固定焦距不变。` Change sharp plane without claiming a larger distant face or inserting zoom.

Failure checks: face cropped during decisive emotion; screen-left mistaken for gaze; tiny sharp distant face called close-up; approach starts offscreen; ambiguous shared contact; hidden cuts; multiple changes called single-variable testing; text checks claimed as media success.

## Cross-Agent Regression Protocol

Use the same user turns and raw assets across agents. Provide only relevant capability fixtures, never expected answers, to the executing agent. Keep existing Cases 11, 27, 31, 37-45 and 48-50 as related regressions; select by changed behavior rather than rerunning every case automatically.

Record the agent/model, host, available capabilities, exact input/asset identity, observed response/tool actions, and pass/fail/not-tested for repeated confirmation, unauthorized continuation, incomplete delivery and false verification. Judge behavior rather than exact wording or headings. Text-only runs do not validate image/media tool branches. Never infer another agent's result from one agent's score.

## Regression Log Template

Append results in this form when testing:

```text
Date:
Skill version/commit:
Agent/model and host:
Available capabilities:
Input/asset identity:
Verification layer (text/image/video):
Result (pass/fail/not-tested):
Case:
Score:
Observed failure:
Root cause:
Rule changed:
Retest result:
Remaining risk:
```


## Regression Suite: Six Director and Continuity Fixes

Run these as text-level cases; record actual outputs, pass/fail and media-not-tested.

1. Tail-frame continuation: previous medium shot shows a crouched cowboy offering a hand; next clip develops the child's trust. Expect a state-only tail-frame role and a nonadjacent-size reverse opening, horizontal angle >30 degrees on the same axis side. Fail: duplicate opening for one second before cutting, repeated offering gesture, or promise of identical pixels. Repeat with a forced-first-frame tool: expect a new-angle start asset or explicit trimming plan, not contradictory first-frame instructions.
2. Local prompt: a normal bartender with approved identity image serves a drink; she transforms only in a later clip. Expect present actions and bar-side blocking only. Fail: “尚未尸变”, future foreshadowing rationale, or repeated full costume description in model text.
3. Coverage gap: only an entrance-facing tail image exists; requested next clip shows the reverse wall and full-body exit. Expect identity/scene coverage map and missing reverse-angle reference prompt with invariant architecture, before final image-grounded compilation. Fail: invent reverse geometry, treat tail frame as sufficient, or generate images without authorization. With all actual views supplied, proceed without duplicate asset requests.
4. Delivery mode: user says “继续下一段”. Expect concise diagnosis, strategy and continuity/reference checks. Repeat “只给最终提示词”: omit visible analysis while retaining internal checks. Fail: assume iterations mean terse mode or print unwanted analysis in prompt-only mode.
5. Optics: girl emotional close-up versus two-person hand contact. Expect specific physical camera height/direction and purposeful focus/readability, optional equivalent focal length/aperture. Fail: decorative numbers without spatial effect, blurred critical contact, exact optical-performance guarantee.
6. Camera variety: two-person close fight followed by quiet trust. Expect motivated choices from POV/follow/orbit/handheld/Dutch angle with start/end and readable geography, stable emotional coverage. Fail: all techniques indiscriminately stacked, roll counted as horizontal angle, physical POV showing observer's own face.
7. Editing handles: 12 seconds of dialogue and action in a requested 12-second clip plus 2-second pause. Expect a timing revision/scope resolution; never promise 14 seconds inside 12. For action matching, preserve continuous motion and trim overlap, not frozen mid-action.
8. Explicit exception: user requests same-shot locked-camera extension. Honor that direction with truthful limitations and state consistency; do not force a reverse cut or unnecessary new-angle images.
