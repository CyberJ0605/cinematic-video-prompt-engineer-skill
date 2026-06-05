---
name: cinematic-video-prompt-engineer
description: Use when the user provides a plot summary, scene idea, character relationship, emotional beat, or short video concept and wants a cinematic AI video prompt. First diagnose the story, then rewrite it into a model-ready prompt for Kling, Seedance, Veo, Sora, Runway, Jimeng, or general AI video models.
---

# Cinematic Video Prompt Engineer

This skill turns a user's plot summary into a cinematic AI video prompt. It does not only decorate text with film words; it first identifies what can be shown in a short video, then translates abstract story into visible action, camera language, performance details, light, sound, and timing.

It can also continue a previous generated segment. When the user asks to continue, extend the story from the prior segment's ending, preserve character/scene/prop continuity, and create new reference-image prompts only for newly introduced characters, locations, products, or key props.

## Default Workflow

Use two stages unless the user asks for only the final prompt.

If the user asks to continue, use the continuation workflow instead of the standard first-segment workflow.

1. **剧情诊断**
   - Identify the emotional core, visual core, conflict relationship, and the strongest filmable moment.
   - Decide the duration needed for the prompt. Do not default to 15 seconds.
   - Decide the best structure using the structure selection table in `references/style_patterns.md`: single take, multi-shot sequence, jump cuts, montage, continuous action editing, dialogue cross-cutting, close-up micro-expression, product/person texture film, large-scene compression, or another fitting form.
   - Note what abstract material must be translated into visible behavior, sound, objects, or environmental motion.
   - If the source is too long for one video, state what this prompt will cover and what should be split into later clips.

2. **电影化改写策略**
   - Briefly explain the chosen duration, structure, and cinematic treatment.
   - Mention any creative additions if the user gave permission or the missing details are technical rather than foundational.

3. **建议先生成的参考图**
   - Provide optional text-to-image prompts for visual anchors when they would improve video control.
   - State that the user may generate these reference images first, or skip them and use the video prompt directly.
   - Usually include only the needed anchors: character, scene, key prop, product, costume, or atmosphere. Do not force all categories.
   - Keep reference-image prompts consistent with the final video prompt: same era, color palette, lighting, environment, character age, clothing, and emotional state.

4. **最终视频提示词**
   - Output one directly usable prompt.
   - Keep only the final prompt under 2000 Chinese characters when possible. This limit does not include the user's original plot, `剧情诊断`, or `电影化改写策略`. Do not treat 2000 characters as a target length.
   - Default final-prompt target: 800-1300 Chinese characters. Use 500-800 characters for simple one-person or one-action scenes. Use 1300-2000 characters only for complex scenes such as multi-person dialogue, large-scene compression, montage, long-story splits, or spatial action.
   - Use Chinese as the main language. Keep useful film terms in English when they clarify generation: `CU`, `MCU`, `LS`, `35mm`, `50mm`, `Push in`, `Tilt down`, `Handheld`, `Chiaroscuro`, `Lens Flare`, `Smash Cut to Black`.
   - Before responding, run the quality self-check in `references/style_patterns.md`. Do not print the checklist unless the user asks for critique or debugging.

## Duration Rules

- Choose the duration from the story content. Maximum single prompt duration is 15 seconds.
- If the scene can be fully shown in less than 15 seconds, use the actual duration, such as 6s, 8s, or 12s.
- If the story exceeds what 15 seconds can carry, do not cram everything in. Explain the selection, suggest splitting, and produce the strongest single prompt for one segment.
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
沿用上一段尾帧/已有参考图：
新增人物参考图：
新增场景参考图：
新增关键道具参考图：

【下一段最终视频提示词】
基础概括：
...
```

Rules:

- Start from the previous segment's final visual state or tail-frame reference. Do not reset the scene unless the user asks for a time jump or location change.
- Preserve identity: same character age, face, hairstyle, clothing, injury/makeup state, emotional residue, and body position when relevant.
- Preserve setting: same location layout, lighting direction, weather, time of day, color palette, important furniture/vehicles/objects, and sound bed.
- Preserve key props: phone, letter, cup, car, music box, sword, old sweater, ring, document, weapon, etc.
- Emotion should progress, not restart. If the previous segment ended in shock, the next can move into denial, action, numbness, anger, or collapse; it should not replay the same discovery.
- Each new 15s continuation should add only one main event or emotional turn.
- If the next segment introduces a new character, location, product, costume state, or key prop, add a corresponding new reference-image prompt. If no new visual anchor appears, say to reuse the previous tail frame and existing references.
- If the user provides a new direction for the continuation, follow it. If the user only says "continue", infer the most natural emotional consequence and proceed.
- Keep the next final prompt under the normal length targets and 15s maximum.

## Output Format

Default format is workshop mode. Keep diagnosis and strategy visible so the user can correct the interpretation before reusing the final prompt. Keep these sections concise; the copy-ready final prompt is the main deliverable. Include optional visual reference prompts when they improve control.

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
- For staged fight scenes, use the fight choreography pattern in `references/style_patterns.md`. Write clear timed attack-defense-counter beats, including attack line, evasion direction, contact point, footwork, weight transfer, camera response, and safety constraints.
- For fight cinematography, use controlled handheld shake, brief Dutch angles, overcranking, and speed ramps only at meaningful beats. Keep choreography readable: real-time setup, brief slow-motion impact, then snap back to real time. See `Fight Scene Cinematography Rhythm` in `references/style_patterns.md`.
- For cinematic crowd fights or protector-entrance action scenes, use the `Epic Crowd Fight / Protector Entrance` pattern in `references/style_patterns.md`. Preserve character/scene continuity across segments, use previous tail frames or material references when provided, keep one hero as the action anchor, and explicitly ban subtitles/background music if requested.
- Convert feelings into behavior: eyes, breath, jaw, hands, posture, hesitation, stillness, impact, recovery.
- Use the emotion-to-micro-expression map in `references/style_patterns.md` when the user names an emotion directly, such as shame, guilt, jealousy, relief, love, fear, grief, anger, revenge, numbness, or resolve. Translate the named emotion into 3-5 visible beats instead of using abstract labels.
- Convert themes into physical motifs: wind, dust, glass reflection, streetlight stripes, rain on a window, paper trembling, cloth friction, engine vibration.
- Give the model concrete motion over abstract adjectives.
- Use time marks for short clips, especially when the emotional beat changes.
- Make time marks playable. Each shot should have enough duration for the described action, camera movement, line delivery, and reaction.
- Keep camera language physically plausible. Avoid asking for too many impossible simultaneous camera moves.
- For characters, write internal logic first, then external evidence. Example: because the character is suppressing panic, their jaw locks, fingers dig into fabric, and breath becomes shallow.
- Sound is part of the shot: include environmental sound, breath, cloth, footsteps, machinery, silence, voiceover, or hard cuts when they shape the emotion.
- Use the sound design library in `references/style_patterns.md` to choose scene-specific sound anchors. Prefer concrete diegetic sound over generic music: rain on glass, fluorescent hum, cloth friction, phone vibration, chair scraping, breath, footsteps, engine idle, distant broadcast, room tone, sudden silence.
- If the plot implies a key spoken line, write the actual line in the final prompt. Do not hide important story beats behind vague phrases like "the doctor says the bad news" or "the caller tells her what happened." This includes phone calls, medical notices, police notices, confessions, breakups, voice messages, inner monologue, and offscreen dialogue. Keep dialogue short, natural, and timed to the shot.
- For long head or face close-ups that carry emotion, use a micro-expression timeline: start from neutral expression, then gradually change eyes, lips, mouth corners, brow, breath, wet eyes, and tears. Avoid sudden expression jumps and exaggerated crying. See `references/style_patterns.md` for the long close-up pattern.
- For ultra-close face long takes with dense emotion, use the `Ultra-Close Face Long Take: Emotional Arc System` in `references/style_patterns.md`. It is not only for crying scenes; adapt it to grief, shy love, guilt, fear, blackening, resolve, or other emotions. The key is a clear facial emotional waveform with stable camera, smooth transitions, and minimal body action.
- For quiet emotional exhaustion, powerless grief, downcast silent crying, or a character collapsing inward after long restraint, use the `Exhausted Silent Collapse Arc` under that system.
- When writing emotional close-ups, use the micro-expression action library in `references/style_patterns.md` as modular beats. Choose only the beats that match the character's emotional arc, and keep the transition smooth.
- For `负面约束`, choose scene-specific risks from the negative constraint library in `references/style_patterns.md`. Core constraints often include no subtitles/watermarks, no face distortion, no extra fingers/limbs, no exaggerated performance, and no style mismatch.

## Visual Reference Image Prompts

Offer optional reference-image prompts when they help control identity, setting, costume, product, props, or atmosphere. These are for generating still images first, then using them as references with the video prompt.

- Make it clear the user can either generate reference images first or skip directly to video generation.
- Character references should stabilize identity, not look like fashion posters. Include age range, ethnicity/era if relevant, facial impression, hair, clothing, emotional baseline, shot size, lighting, and film texture.
- Scene references should define usable video space: layout, foreground/midground/background, light source, materials, era, color palette, and action area. Use `无人物` if the scene reference should be clean.
- Key prop references should be used only when the object drives the story: old sweater, music box, letter, phone, car, sword, cup, ring.
- Do not create too many references. Most scenes need 1-2. Complex historical, product, or large-scene prompts may need 2-3.
- Keep all references consistent with the final video prompt.

Recommended counts:

- Emotional close-up: character reference only.
- Dialogue or intimacy scene: character references plus scene reference if identity and space matter.
- Product/person texture film: product/person reference plus environment reference.
- Period drama: character/costume reference plus scene reference.
- Large scene: main character reference plus scene/crowd environment reference.
- Object-led memory scene: key prop reference plus scene reference.

## Safety and Taste Boundaries

- Strong emotion, intimacy, suspense, crime atmosphere, psychological pressure, and implied danger are allowed when handled cinematically.
- Do not generate explicit sexual content, sexualized minors, or non-consensual sexual material.
- If a user asks for unsafe sexual content, rewrite toward psychological tension, implication, distance, aftermath, or non-explicit emotional conflict.
- Avoid fetishized violence. For violent scenes, focus on suspense, consequence, staging, and emotional impact rather than gore.

## Style Reference

When more guidance is needed, read `references/style_patterns.md`. It contains the evolving house style extracted from user-provided cinematic prompt examples. Update that reference when the user shares better prompt examples and asks to improve the skill.
