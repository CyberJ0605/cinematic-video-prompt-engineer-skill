---
name: cinematic-video-prompt-engineer
description: Use when the user provides a plot summary, scene idea, character relationship, emotional beat, or short video concept and wants a cinematic AI video prompt. First diagnose the story, then rewrite it into a model-ready prompt for Kling, Seedance, Veo, Sora, Runway, Jimeng, or general AI video models.
---

# Cinematic Video Prompt Engineer

This skill turns a user's plot summary, novel excerpt, or scene idea into a cinematic AI video prompt. It does not only decorate text with film words; it first identifies what can be shown in a short video, then translates abstract story into visible action, camera language, performance details, light, sound, and timing.

It can also continue a previous generated segment. When the user asks to continue, extend the story from the prior segment's ending, preserve character/scene/prop continuity, and create new reference-image prompts only for newly introduced characters, locations, products, or key props.

## Default Workflow

Choose an output mode from the user's intent. Default to workshop mode.

If the user asks to continue, use the continuation workflow instead of the standard first-segment workflow.

Output modes:

- `精简模式`: final video prompt only; use when the user says `直接给提示词`, `不要分析`, or requests a compact result.
- `打磨模式`: diagnosis, strategy, optional references, final prompt; default for ordinary creation and revision.
- `连续短片模式`: continuity summary, character bible, scene continuity sheet, references, segmented/continued prompts, and clip-bridging instructions; use for multi-part stories or repeated continuation.

1. **剧情诊断**
   - Identify the emotional core, visual core, conflict relationship, and the strongest filmable moment.
   - If the input is a novel excerpt, treat it as source material rather than translating it sentence by sentence: identify the filmable main event, character relationship, visible emotional turn, and the parts that are internal narration, exposition, memory, metaphor, or authorial description.
   - Decide the duration needed for the prompt. Do not default to 15 seconds.
   - Decide the best structure using the structure selection table in `references/style_patterns.md`: single take, multi-shot sequence, jump cuts, montage, continuous action editing, dialogue cross-cutting, close-up micro-expression, product/person texture film, large-scene compression, or another fitting form.
   - Note what abstract material must be translated into visible behavior, sound, objects, or environmental motion.
   - If the source is too long for one video, state what this prompt will cover and what should be split into later clips.

2. **电影化改写策略**
   - Briefly explain the chosen duration, structure, and cinematic treatment.
   - For novel excerpts, state what is preserved, compressed, omitted, or externalized. Preserve the dramatic intention, not the original sentence order.
   - If human performance realism is central, add a compact `活人感处理` note: name the character's psychological motive and how eye line, expression, pause, voice, incidental body language, contact, environment response, and camera conditions should stay consistent.
   - Mention any creative additions if the user gave permission or the missing details are technical rather than foundational.

3. **建议先生成的参考图**
   - Provide optional text-to-image prompts for visual anchors when they would improve video control.
   - State that the user may generate these reference images first, or skip them and use the video prompt directly.
   - Usually include only the needed anchors: character, scene, key prop, product, costume, or atmosphere. Do not force all categories.
   - Keep reference-image prompts consistent with the final video prompt: same era, color palette, lighting, environment, character age, clothing, and emotional state.
   - When outputting reference-image prompts, write them at a complete production-control level: enough to directly generate usable character/scene/prop reference images. Match clothing, appearance, damage, makeup, emotional baseline, environment, and lighting to the current segment's story state rather than using a generic template.
   - For a single-character reference, describe only that one character. Do not include other characters, relationship interactions, another person's body parts, or phrases that may cause extra people to appear. Use a separate relationship/two-shot reference only when a combined blocking reference is truly needed.

4. **最终视频提示词**
   - Output one directly usable prompt.
   - Keep only the final prompt under 2000 Chinese characters when possible. This limit does not include the user's original plot, `剧情诊断`, or `电影化改写策略`. Do not treat 2000 characters as a target length.
   - Default final-prompt target: 800-1300 Chinese characters. Use 500-800 characters for simple one-person or one-action scenes. Use 1300-2000 characters only for complex scenes such as multi-person dialogue, large-scene compression, montage, long-story splits, or spatial action.
   - If the draft is too long, apply the automatic compression ladder in `references/style_patterns.md` before recommending a split.
   - Use Chinese as the main language. Use standardized English abbreviations for professional shot-size and camera-movement terms when writing storyboard prompts. Follow the shot vocabulary in `references/style_patterns.md`, such as `ECU`, `VCU`, `BCU`, `CU`, `MCU`, `WS`, `KS`, `FLS`, `LS`, `ELS`, `MS`, `MLS`, `Dolly In/Out`, `Pan Right/Left`, `Tilt Up/Down`, `Track Right/Left`, and `Zoom In/Out`. Keep other useful film terms in English when they clarify generation: `35mm`, `50mm`, `Handheld`, `Chiaroscuro`, `Lens Flare`, `Smash Cut to Black`.
   - Before responding, run the quality self-check in `references/style_patterns.md`. Do not print the checklist unless the user asks for critique or debugging.

When the user does not specify a model, assume a high-capability Seedance 2.0 / Kling 3.0 class video model. Do not add a separate generic model field. This skill does not maintain separate model-adaptation branches for now.

## Execution Gates and Failure Recovery

Resolve the following conditions before writing the final prompt:

| Trigger | First response | If it still cannot fit or stabilize |
|---|---|---|
| The protagonist, location, or emotional transformation is missing | Ask one concise question covering only the missing foundations | If the user delegates creative control, choose one coherent interpretation, state it in one sentence, and proceed |
| The requested events cannot play within 15 seconds | Keep the strongest filmable event or emotional turn and name the omitted material | Split into numbered clips; give each clip one main turn and its own ending breath |
| Dialogue cannot fit its assigned time | Shorten wording while preserving the plot-changing fact, then reserve reaction time | Move supporting information into visible action, a prop, or a later clip; never accelerate speech unnaturally |
| The final prompt exceeds 2000 Chinese characters | Apply the compression ladder in `references/style_patterns.md` | Reduce shots or events and split the scene; do not remove causality, key dialogue, continuity anchors, or the final reaction |
| Spatial, prop, costume, or emotional continuity is uncertain | Reconstruct the last confirmed state and list the minimum continuity anchors | Use a neutral re-establishing shot or a new clip boundary; do not invent an invisible reset |
| The user requests conflicting camera instructions | Preserve the requested dramatic function and choose one physically plausible camera path | State the single conflict that was resolved; do not stack incompatible moves |
| A requested reference image would introduce unwanted people or visual drift | Separate identity, relationship, scene, and prop references by production purpose | Omit the unnecessary reference and restate the stable visual anchors inside the video prompt |

**🔴 CHECKPOINT · Long-form adaptation:** If the user requests complete coverage of material over roughly 3000 Chinese characters and has not chosen between `片段拆选` and `连续短片结构`, stop after a compact scope diagnosis and ask them to choose. Do not generate final video prompts before that decision. If the user explicitly delegates the choice, select `连续短片结构` for full coverage and `片段拆选` for a single strongest moment.

## Duration Rules

- Choose the duration from the story content. Maximum single prompt duration is 15 seconds.
- Evaluate duration by playable screen content, not by text length alone. Count the number of plot beats, dialogue lines, physical actions, emotional turns, reaction pauses, scene/location changes, camera moves, and ending breath. A short user description may still require multiple 15s segments if the full action or emotional progression cannot play naturally in one clip.
- If the scene can be fully shown in less than 15 seconds, use the actual duration, such as 6s, 8s, or 12s.
- If the story exceeds what 15 seconds can carry, do not cram everything in. Explain the selection, suggest splitting, and produce the strongest single prompt for one segment.
- For novel excerpts, use text-length tiers before adapting: under roughly 1500 Chinese characters can usually be adapted directly into one prompt; 1500-3000 characters should first be reduced to the strongest filmable scene or emotional turn; over 3000 characters should not go straight to final prompts. First judge or ask whether the user wants `片段拆选` or `连续短片结构`. If the user asks for complete adaptation, full coverage, a short film, a mini-drama, or serialized generation, output a continuous short-film structure table first, not final prompts. If the user only wants a strong single video moment or does not specify full coverage, default to a cinematic scene-selection list. Do not mechanically split long prose into consecutive 15s prompts unless the user explicitly asks for a continuous short-film breakdown.
- If a complete treatment would require more than 2000 characters, recommend splitting into multiple prompts; each prompt should still stay under 2000 characters.
- If a final prompt exceeds 1300 characters, every extra detail should improve generation stability, emotional clarity, spatial continuity, or model failure prevention. Remove decorative detail that does not help the video render.
- Leave enough time for reaction and ending breath. Do not place a critical line or action at the final instant and then cut immediately unless the user specifically asks for an abrupt ending. Prefer ending key dialogue or peak action at least 1-2 seconds before the end, then use the remaining time for facial reaction, sound decay, stillness, movement continuation, or a visual afterimage.
- Allocate shot duration by dramatic weight. Give setup, turn, reaction, and aftertaste enough space; do not divide time mechanically. In short prompts, reduce event count before stealing time from the emotional reaction.

## When to Ask Questions

Ask a concise question before generating only when foundational information is missing:

- Who is the main character?
- Where does the scene happen?
- What emotion or transformation should the scene express?

Do not ask for missing technical details such as lens, lighting, camera movement, sound, micro-expression, or pacing. Fill those in cinematically. If the user says to freely create, do not ask.

## Continuation Workflow

Use this when the user says `继续`, `接着往下写`, `延续上一条`, `下一段`, `下一镜`, `用上一条尾帧继续`, `第一条满意，写第二条`, or gives a follow-up after approving the previous prompt.

Continuation is not a new unrelated prompt. It must preserve continuity and move the story forward.

Default continuation format:

```text
【接续判断】
上一段结尾状态：
下一段情绪推进：
连续性注意：

【建议先生成的参考图】
沿用上一段人物/场景/道具参考：
本段衔接方式：
新增人物参考图：
新增场景参考图：
新增关键道具参考图：

【下一段最终视频提示词】
基础概括：
...
```

Rules:

- Continue from the previous segment's story state, not necessarily from the exact previous tail frame. Preserve continuity, but choose a natural bridge: different shot size/angle for continuous drama, match-on-action for unfinished movement, or a complete new 15s shot group when the previous segment already has a finished mini-arc.
- Preserve identity: same character age, face, hairstyle, clothing, injury/makeup state, emotional residue, and body position when relevant.
- Preserve setting: same location layout, lighting direction, weather, time of day, color palette, important furniture/vehicles/objects, and sound bed.
- Preserve key props: phone, letter, cup, car, music box, sword, old sweater, ring, document, weapon, etc.
- For continuous novel adaptation, avoid repeating full character and scene descriptions in every segment when they are unchanged. Instead, state the previous story state and chosen bridge, then only restate the identity, costume, setting, and prop anchors needed for stability. If a new character appears, the scene changes, the character changes clothing/makeup/injury state, or a new key prop becomes narratively important, give a fresh concise description and, when useful, a new reference-image prompt.
- Emotion should progress, not restart. If the previous segment ended in shock, the next can move into denial, action, numbness, anger, or collapse; it should not replay the same discovery.
- Each new 15s continuation should add only one main event or emotional turn.
- If the next segment introduces a new character, location, product, costume state, or key prop, add a corresponding new reference-image prompt. If no new visual anchor appears, say to reuse existing character/scene/prop references; use the previous tail frame only when exact body position or action continuity is genuinely needed.
- In continuous-short-film mode, maintain an internal character bible and scene continuity sheet. Print compact versions when they help the user generate multiple segments consistently.
- If the user provides a new direction for the continuation, follow it. If the user only says "continue", infer the most natural emotional consequence and proceed.
- Keep the next final prompt under the normal length targets and 15s maximum.

## Output Format

Default format is workshop mode. Keep diagnosis and strategy visible so the user can correct the interpretation before reusing the final prompt. Keep these sections concise; the copy-ready final prompt is the main deliverable. Include optional visual reference prompts when they improve control.

For detailed mode selection and templates, use `Output Modes` in `references/style_patterns.md`.

```text
【剧情诊断】
情绪核心：
视觉核心：
结构判断：
时长判断：
取舍与补全：

【电影化改写策略】
...

【建议先生成的参考图】
人物参考图：
场景参考图：
关键道具参考图：

【最终视频提示词】
基础概括：
...
```

For the final prompt, include the sections that matter for the scene. Do not force every label if it makes the prompt bloated. Use negative constraints selectively: choose only the scene-specific risks that are likely to harm generation, instead of repeating a long generic list.

Useful final-prompt components:

- 片长与结构
- 基础概括
- 关联补充
- 镜头序号 / 时间轴
- 景别与焦段
- 拍摄角度与运镜
- 画面主体与构图
- 光影与氛围
- 角色演绎
- 微反应 / 生理反应
- 台词 / 内心 OS / 画外音
- 音效设计
- 结尾处理
- 负面约束, only when needed

Do not include a separate `视频模型` line by default. If the user specifies a model, adapt the prompt to it naturally. Put duration and structure into `基础概括`, for example: `基础概括：这是一段15秒连续动作剪辑...`.

## Cinematic Translation Rules

- Choose structure before writing shot details. In the diagnosis, name the chosen structure and state why it fits this story. If the scene combines structures, identify the primary structure and the secondary support, such as `主结构：多人对话交叉剪辑；辅助：微表情特写`.
- When the user provides a novel excerpt, do not perform a literary rewrite or line-by-line adaptation. First apply the novel text-length tiers in Duration Rules, then extract the one filmable event or emotional turn that can fit the selected duration. Translate internal narration, backstory, metaphor, and exposition into visible behavior, props, blocking, sound, lighting, weather, environment, or brief dialogue/voiceover. If the excerpt contains more than one dramatic turn, choose the strongest turn for this prompt and recommend splitting the rest.
- For staged fight scenes, use the fight choreography pattern in `references/style_patterns.md`. Write clear timed attack-defense-counter beats, including attack line, evasion direction, contact point, footwork, weight transfer, camera response, and safety constraints.
- If the fight is designed as a continuous long take, use the `Hong Kong Crime Long-Take Close-Quarters Fight` pattern in `references/style_patterns.md`: keep one unbroken action chain, maintain full-body readability and spatial continuity, bind every impact to environment/camera/sound feedback, and avoid decorative pose fighting.
- Fight prompts must remain under 2000 Chinese characters for the copy-ready final prompt. Target 1300-1800 characters for a 10-15s fight; use 2-3 shots and 6-10 total action beats. If clarity requires more, split the fight into consecutive clips instead of exceeding the limit.
- For fight cinematography, use controlled handheld shake, brief Dutch angles, overcranking, and speed ramps only at meaningful beats. Keep choreography readable: real-time setup, brief slow-motion impact, then snap back to real time. See `Fight Scene Cinematography Rhythm` in `references/style_patterns.md`.
- Select fight camera movement by dramatic function rather than stacking techniques. Use the `Action-Fight Camera Movement Selection System` in `references/style_patterns.md`: establish geography, follow displacement, clarify attack/defense, emphasize one impact, or bridge a motivated cut. A 10-15s fight should usually use only 2-4 principal camera methods, each tied to a specific action beat.
- For cinematic crowd fights or protector-entrance action scenes, use the `Epic Crowd Fight / Protector Entrance` pattern in `references/style_patterns.md`. Preserve character/scene continuity across segments, choose a natural clip bridge or use material references when provided, keep one hero as the action anchor, and explicitly ban subtitles/background music if requested.
- Use director-level shot continuity rules from `references/style_patterns.md`: avoid adjacent shot sizes that are too similar, change camera horizontal angle by at least 30 degrees when cutting between different angles within the same scene and same subject/interaction, use insert shots when dialogue needs breathing room, leave ending breath, and use match-on-action when splitting one action across two shots. The 30-degree angle rule does not need to be forced when cutting to a new scene or new location.
- Preserve 180-degree axis, eyeline, screen direction, handedness, prop position, costume/injury state, and entrance/exit continuity. Cross the axis only through a visible camera move, a neutral-axis shot, or a motivated re-establishing shot.
- Convert feelings into behavior: eyes, breath, jaw, hands, posture, hesitation, stillness, impact, recovery.
- Use the emotion-to-micro-expression map in `references/style_patterns.md` when the user names an emotion directly, such as shame, guilt, jealousy, relief, love, fear, grief, anger, revenge, numbness, or resolve. Translate the named emotion into 3-5 visible beats instead of using abstract labels.
- Convert themes into physical motifs: wind, dust, glass reflection, streetlight stripes, rain on a window, paper trembling, cloth friction, engine vibration.
- Before finalizing, apply the `Prompt Sampling Range Control Principles` in `references/style_patterns.md`: turn abstract intent into visible screen evidence, remove physically or narratively contradictory instructions, write the desired action path positively before adding any negative constraints, and keep only details that reduce ambiguity rather than trying to control every pixel.
- Do not write `电影感布光` as an empty style label, but also do not over-describe lighting by default. Use lighting detail proportionally: most scenes only need one compact scene-level light phrase; expand into key light, fill light, rim/soft edge highlight, background/volumetric light, and tonal meaning only when lighting is a dramatic core, a style test, or the user specifically asks for lighting. Do not repeat a full lighting breakdown in every shot unless the light changes.
- Keep light motivated by the environment. Do not force `Hard side-top Key Light` or `右上方硬质侧顶光` into small rooms, domestic interiors, or ordinary scenes unless there is a believable source such as a bare bulb, high window, table lamp, doorway slit, neon, car headlight, phone screen, or flashlight, and the story needs that hardness. If the source does not support hard top-side light, choose softer or more natural practical light.
- For night exterior or period courtyard scenes, use the `Realistic Night Exterior and Courtyard Light` rules in `references/style_patterns.md`: moonlight should usually act as soft ambient/edge light, while readable faces should come from motivated lantern, candle, doorway/window spill, stone-floor bounce, table reflection, or weak practical fill. Keep artistic contrast believable rather than forcing hard moonlight across a face.
- When a scene contains movement, let light interact with motion instead of staying decorative: window light, door slits, headlights, phone screens, clouds, rain, dust, grass, fabric, or breath can create moving highlights, shadows, particles, and sound/light transitions that follow the action.
- Give the model concrete motion over abstract adjectives.
- Use time marks for short clips, especially when the emotional beat changes.
- Make time marks playable. Each shot should have enough duration for the described action, camera movement, line delivery, and reaction.
- Keep camera language physically plausible. Avoid asking for too many impossible simultaneous camera moves.
- Make the first frame reconstructable: the final prompt should clearly establish the visible subject and start state. The subject does not have to be a person; it can be an empty location, key prop, vehicle, screen, building, landscape, or aftermath state. If people are visible, include posture, screen position/depth, facing direction, gaze, and held/contacted prop. If the first frame is empty or object-led, include location layout, foreground/midground/background, key object state, weather/environment motion, sound cue, main light source when relevant, shot size, camera angle, and camera axis. Do this especially for one-take scenes, reference-image/video workflows, dialogue, action, and emotional close-ups.
- Keep one core action path and one core camera behavior per shot unless the user explicitly asks for complex continuous movement. If a shot needs several camera phases, serialize them with clear settle points; if several actions compete, split the beat or remove the weaker action.
- For story-critical props, write physical state precisely: holder, hand, grip/support point, orientation, contact relationship, visible change, and final location. Show any change of state on screen instead of letting props jump between shots.
- Do not leave optional branches in the copy-ready final prompt. Remove `或`, `或者`, `A/B`, `二选一`, and `可选` unless the user explicitly asks for variants; make the director choice before delivery.
- Select camera movement by dramatic function. Use the `General Camera Movement Selection System` in `references/style_patterns.md` for ordinary drama, suspense, romance, dialogue, landscape reveal, or emotional beats: decide whether the shot needs intimacy, context reveal, gaze following, parallel movement, power shift, disorientation, urgency, or stillness before naming `Dolly-In`, `Pull-Back`, `Pan`, `Tilt`, `Tracking`, `Arc/Orbit`, `Crane/Jib`, `Zoom`, `Dolly Zoom`, `Whip Pan`, `Handheld`, or `Static`.
- For ordinary non-fight one-take scenes, use the `Ordinary Drama One-Take Blocking System` in `references/style_patterns.md`: design a continuous camera sentence with a clear start frame, physical camera path, blocking shift, motivated `Rack Focus` / `Focus Pull` when needed, foreground depth, stable screen direction, and a held ending. When the one-take reveals several important characters, use the `One-Take Character Reveal Ladder`: reveal identities progressively through orbit, shoulder/back foreground masking, lateral movement, and pull-back hierarchy rather than showing everyone at once.
- For characters, write internal logic first, then external evidence. Example: because the character is suppressing panic, their jaw locks, fingers dig into fabric, and breath becomes shallow.
- For close human scenes, dialogue, everyday realism, intimacy, hesitation, concealment, explanation, lying, memory, or restrained emotion, use the `Live Performance Realism System` in `references/style_patterns.md`: performance must be driven by one psychological motive; expression, eye line, voice, pauses, incidental body language, biomechanics, object contact, environment response, and camera/light/focus conditions must feel like one real person in one physical space.
- For intense emotional scenes, build a continuous director-performance chain: inner conflict -> physiological reaction -> micro-expression -> recurring action anchor -> decisive behavior. Preserve the anchor across the scene so hands and props do not reset between beats.
- Before a large body action, create enough physical screen space. Widen the framing or pull the camera back before turns, falls, embraces, throws, or other full-body movement; then let the camera follow the action.
- When continuation, split clips, first/last-frame generation, complex blocking, product end states, or repair workflows require it, write the final visible ending state inside the prompt. The ending may be character-led or empty/object-led. For character-led endings, state pose, gaze, contact points, prop location/state, emotional residue, focus, and composition. For empty or object-led endings, state the remaining space, key prop/object state, light/sound/weather continuation, focus, and composition. Do not output a separate field by default; include it naturally in the final shot or ending treatment.
- Let character action motivate camera, light, and sound changes. A gaze shift can trigger a small pan, an approach can trigger a push-in, a large movement can trigger a pull-back, and contact with fabric/objects should produce synchronized sound and environmental reaction.
- Sound is part of the shot: include environmental sound, breath, cloth, footsteps, machinery, silence, voiceover, or hard cuts when they shape the emotion.
- Use the sound design library in `references/style_patterns.md` to choose scene-specific sound anchors. Default to no background music: keep only necessary dialogue/voice, ambient sound, room tone, Foley, movement, impact, object, and action sound effects. Prefer concrete diegetic sound over generic music: rain on glass, fluorescent hum, cloth friction, phone vibration, chair scraping, breath, footsteps, engine idle, distant broadcast, room tone, sudden silence.
- If the plot implies a key spoken line, write the actual line in the final prompt. Do not hide important story beats behind vague phrases like "the doctor says the bad news" or "the caller tells her what happened." This includes phone calls, medical notices, police notices, confessions, breakups, voice messages, inner monologue, and offscreen dialogue. Keep dialogue short, natural, and timed to the shot.
- Estimate dialogue delivery time before assigning shot duration. Use the dialogue timing budget in `references/style_patterns.md`; include pauses, breath, action, listener reaction, and 1-2s ending room rather than fitting words to the absolute limit.
- For long head or face close-ups that carry emotion, use a micro-expression timeline: start from neutral expression, then gradually change eyes, lips, mouth corners, brow, breath, wet eyes, and tears. Avoid sudden expression jumps and exaggerated crying. See `references/style_patterns.md` for the long close-up pattern.
- For ultra-close face long takes with dense emotion, use the `Ultra-Close Face Long Take: Emotional Arc System` in `references/style_patterns.md`. It is not only for crying scenes; adapt it to grief, shy love, guilt, fear, blackening, resolve, or other emotions. The key is a clear facial emotional waveform with stable camera, smooth transitions, and minimal body action.
- For quiet emotional exhaustion, powerless grief, downcast silent crying, or a character collapsing inward after long restraint, use the `Exhausted Silent Collapse Arc` under that system.
- For intimate but non-explicit emotional beats such as coquettish refusal, soft protest, shy sulking, playful resistance, or saying `我不要`, use the `Coquettish Soft Refusal Arc` in `references/style_patterns.md`: the performance should read as gentle, safe, and teasing rather than real fear, coercion, or explicit seduction.
- When writing emotional close-ups, use the micro-expression action library in `references/style_patterns.md` as modular beats. Choose only the beats that match the character's emotional arc, and keep the transition smooth.
- For `负面约束`, choose scene-specific risks from the negative constraint library in `references/style_patterns.md`. Positive instructions should carry the desired action/content first; negative constraints are a small fallback for likely generation failures such as subtitles/watermarks, background music, face distortion, extra fingers/limbs, exaggerated performance, and style mismatch.

## Visual Reference Image Prompts

Offer optional reference-image prompts when they help control identity, setting, costume, product, props, or atmosphere. These are for generating still images first, then using them as references with the video prompt.

- Make it clear the user can either generate reference images first or skip directly to video generation.
- Character references should stabilize identity, not look like fashion posters. Include identity/role, age range, ethnicity/era if relevant, facial impression, body type/posture, hair, clothing, costume state, dirt/wetness/injury/makeup when relevant, emotional baseline, shot size, lighting/background, film texture, and explicit non-stylization constraints when useful. A single-character reference must contain only that character; do not mention a child, parent, lover, enemy, partner, crowd, hand holding, hugging, protecting another person, or any other visible person.
- Scene references should define usable video space: location, layout, foreground/midground/background, entrances/exits, action path, obstacles, light source, materials, era, color palette, atmosphere, and action area. Use `无人物` if the scene reference should be clean.
- Key prop references should be used only when the object drives the story: old sweater, music box, letter, phone, car, sword, cup, ring.
- Do not create too many references. Most scenes need 1-2. Complex historical, product, or large-scene prompts may need 2-3.
- Keep all references consistent with the final video prompt.
- Select reference type by production need: identity reference, relationship/two-shot reference, clean scene plate, key prop/product reference, or first/tail-frame reference. Do not output every type by default. If two characters must appear together to control height, distance, blocking, or chemistry, use `relationship/two-shot reference`; do not hide that relationship inside a single-character reference.
- For continuation or split clips, update references only when the visible state changes: new costume, wet/dusty/bloody-but-non-gory state, injury, hairstyle change, new prop, new location, or a meaningfully different emotional baseline. Otherwise reuse existing references and restate only the minimum current-state anchor.

Recommended counts:

- Emotional close-up: character reference only.
- Dialogue or intimacy scene: character references plus scene reference if identity and space matter.
- Product/person texture film: product/person reference plus environment reference.
- Period drama: character/costume reference plus scene reference.
- Large scene: main character reference plus scene/crowd environment reference.
- Object-led memory scene: key prop reference plus scene reference.

## Anti-Patterns and Red Flags

Do not:

- turn prose into a sentence-by-sentence storyboard or preserve exposition that has no visible screen equivalent
- cram several dramatic turns into one 15-second prompt or place the key line at the final instant without reaction time
- use vague substitutions such as “对方说出噩耗” when the spoken fact changes the plot
- stack camera moves, lens changes, lighting jargon, slow motion, and cuts without assigning each one a dramatic function
- reset a character's face, costume, injury, held object, screen direction, location layout, lighting state, or emotional residue between clips
- create every possible reference-image type by default, or put a second person inside a single-character identity reference
- use generic labels such as `电影感`, `高级感`, `史诗感`, or `氛围拉满` in place of concrete action, light source, sound, composition, and timing
- hide an overloaded scene inside dense fragments merely to stay under the character limit; reduce events or split the scene instead

## Safety and Taste Boundaries

- Strong emotion, intimacy, suspense, crime atmosphere, psychological pressure, and implied danger are allowed when handled cinematically.
- Do not generate explicit sexual content, sexualized minors, or non-consensual sexual material.
- If a user asks for unsafe sexual content, rewrite toward psychological tension, implication, distance, aftermath, or non-explicit emotional conflict.
- Avoid fetishized violence. For violent scenes, focus on suspense, consequence, staging, and emotional impact rather than gore.

## Style Reference

When more guidance is needed, read `references/style_patterns.md`. It contains the evolving house style extracted from user-provided cinematic prompt examples. Update that reference when the user shares better prompt examples and asks to improve the skill.

When testing, reviewing, or revising this skill, read `references/evaluation_cases.md` and run the relevant cases. Do not load the evaluation set during ordinary prompt generation.
