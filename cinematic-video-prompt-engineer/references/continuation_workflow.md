# Continuation Delivery Module

Read for continued segments and multi-clip work. Paths are relative to the skill root. The main-file scope/approval rules and continuity contract govern this retained workflow.

## Continuation Workflow

Use this when the user says `继续`, `接着往下写`, `延续上一条`, `下一段`, `下一镜`, `用上一条尾帧继续`, `第一条满意，写第二条`, or gives a follow-up after approving the previous prompt.

Continuation is not a new unrelated prompt. It must preserve continuity and move the story forward.

Default continuation format; include the reference-assets block only when the chosen path or a new/updated visual anchor needs it:

```text
【剧情诊断】
本段可见变化与时长风险：

【电影化改写策略】
表演、切点与摄影选择：

【接续判断】
上一段结尾状态：
下一段情绪推进：
连续性注意：

【参考资产状态】
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
- Each new 15s continuation should add only one main event or emotional turn; a 16-30s segment may include a fuller setup-turn-aftermath arc if it stays playable.
- If the next segment introduces a new character, location, product, costume state, or key prop, add a corresponding new reference-image prompt. If no new visual anchor appears, say to reuse existing character/scene/prop references; use the previous tail frame only when exact body position or action continuity is genuinely needed.
- In continuous-short-film mode, maintain an internal character bible and scene continuity sheet with an anchor budget: keep 4-6 stable identity anchors for the main character, 3-5 for an important supporting character, 4-6 spatial/light anchors for each recurring scene, and 1-2 group-level anchors for background people. Track temporary story state separately, including held/placed props, missing accessories, wetness/injury, body position, travel direction, voice condition, and emotional residue. Causally necessary state overrides the numeric budget. Repeat only the anchors visible or relevant in the current shot; when the prompt becomes crowded, remove decorative identity detail before action causality, spatial direction, prop state, key dialogue, or the ending reaction. Print compact bible/sheet versions only when they help the user generate multiple segments consistently.
- If the user provides a new direction for the continuation, follow it. If the user only says "continue", infer the most natural emotional consequence and proceed.
- Keep the next final prompt under the normal length targets and 30s maximum.

