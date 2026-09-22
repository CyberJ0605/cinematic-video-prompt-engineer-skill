# Continuity, Reference Coverage, and Director Delivery Contract

Read this reference for continuation, multi-shot reference-driven prompts, and repairs involving cuts, geometry or coverage. It takes precedence over older examples that conflate a previous tail frame with a required opening composition.

## 1. Tail-frame state is not an opening-frame command

Default: a previous tail frame controls story state (identity, costume, physical layout, contact, handedness, prop state, action phase and emotional residue), not the next clip's exact composition. Start a continuation with a motivated new angle and clearly differentiated shot size. Never default to “原样接续尾帧”, “准确首帧” or one second of duplicated composition before the new angle. A same-shot extension is an explicit user choice, not a synonym for “继续”. Preserve real object locations while allowing their screen coordinates to change with camera perspective.

Distinguish reference input from first-frame input. If the tool supports ordinary image references, assign the tail frame state-only authority. If it forces an input image to be the first frame, a text instruction cannot reliably make that first frame a different angle: prepare a compatible new-angle opening image, or explicitly plan to trim the generated opening and cut at the new view. Do not promise seamless pixels. Inspect actual media before claiming a join works.

### Cut audit (including the boundary between clips)

- Default to nonadjacent shot sizes: avoid 全景→中景, 中景→近景, 近景→特写 and 特写→大特写. Prefer 全景→近景, 中景→特写, 特写→全景. Continuous reframing inside one shot is not a cut. If the user imposes a strict rule, do not silently grant an exception. Otherwise an exception needs a concrete editorial reason.
- For a same-scene cut on the same subject/interaction, specify a horizontal camera change greater than 30 degrees, while preserving the 180-degree axis and eyelines. A Dutch roll, vertical height change or focal-length change alone does not satisfy this. A new location needs readable geography, not a fabricated relative angle.
- Use environment, object or listener inserts only when they carry information, a reaction, elapsed time or a sound bridge. Do not hide a physically impossible reset with an insert.
- Budget 1–2 seconds after the last key line or completed performance beat for reaction, breath, sound decay or continued movement. Include it in total duration. For match-on-action, use flowing action handles/overlap for editing instead of freezing halfway; trim overlap so the action is not repeated on screen.
- Match-on-action specifies previous action phase, next phase, contact, direction, active hand, prop ownership and cut point. Use differentiated sizes/angles; do not restart a completed gesture.

## 2. Keep model instructions local and visible

Keep plot diagnosis and directorial rationale outside the copy-ready prompt. Inside it describe this clip's visible actions, performance, camera, sound, reference roles and necessary continuity facts. Omit future events, backstory, thematic commentary and “铺垫下一段”. A normal character reference needs no “还没有尸变”; write the required reaction and position. Replace “开始信任” alone with observable gaze, breath and voluntary contact. Do not repeat static identity and costume already supplied by references. Preserve story-critical present facts such as a removed poster or an occupied hand. Negative constraints target demonstrated or likely physical failures only, not an inventory of unrelated plot events.

## 3. Shot-first reference coverage

Design the shots before deciding the reference set. Map each important shot to available, inspected visual evidence:

| Reference role | Authority |
|---|---|
| Previous tail frame | Current story/action/prop state, not default framing |
| Main character identity/full-body | Face, hair, proportions, clothing and recurring accessories |
| Scene angle | Architecture, openings, furniture, paths and occlusion from that camera |
| Relationship/action keyframe | Critical contact, relative scale and body positions |
| Key prop/animal | Design, scale, tack or other story-critical state |

One tail frame does not prove an unseen reverse wall or hidden passage. Check each new angle, close-up and full-body action for coverage. Reuse approved references; do not generate every category automatically. If a missing view creates material geometry/identity risk, first deliver a reference-image prompt specifying its source images and roles, camera location/height/direction/shot size, fixed layout and current-state changes. Preserve world geometry, do not redesign a set to fit a shot. Say which planned shots depend on it. Inspect and reconcile the actual new image before final image-grounded compilation. Prompt-only requests do not authorize media generation; authorized generation proceeds without an extra approval unless the user reserved it. If the user explicitly asks for a full text package before assets exist, label dependent video text provisional.

Assign image numbers by actual upload order and put narrow roles inside the final prompt. Conflicting earlier states do not override the latest confirmed state. A character sheet controls identity, not its pose or background. New-angle images must agree with existing doors, partitions, routes and lighting; unknown geometry is not verified evidence.

## 4. Delivery sections remain visible

Unless the user explicitly requests prompt-only output, include concise 【剧情诊断】 and 【电影化改写策略】 in creation and continuation answers. Continuation uses a local diagnosis, not a repeat of the entire plot. Then include 【接续与参考图检查】 when applicable, missing reference prompts when needed, and the final prompt only at the authorized/asset-ready stage. A small repair may use one sentence per diagnosis/strategy section. Do not infer prompt-only mode from repeated iterations. In explicit prompt-only mode, run these checks internally without printing the sections.

## 5. Camera geometry before numeric decoration

Specify important camera positions relative to fixed landmarks, view direction, height, subject angle and movement path. For critical cuts describe horizontal angle change and axis side. Do not overload every shot with every field.

Use full-frame-equivalent focal length when perspective/subject distance matters; pair it with framing and desired spatial effect. Use aperture or a range only when depth of field serves evidence, performance or focus transfer; specify exactly which face/contact/background must be readable. Treat numeric lens/aperture values as visual intent, not guaranteed optical simulation. Do not put a critical gun hit, hand contact or route in blur merely to get a cinematic look. Skip gratuitous numeric settings for simple shots. Example: “85mm等效视角，f/2.8浅景深效果，双眼清晰，身后麻袋虚化但可辨；机位与人物眼睛等高”.

## 6. Choose camera language by dramatic purpose

Read camera_movement_prompt_library.md when a move materially carries the scene. One primary camera behavior per shot, with clear start/path/end and sufficient time.

- Character POV: identify whose eyes, physical eye height, gaze target and movement; distinguish optical POV from an over-shoulder view. Do not show the observer's face in their own optical POV without a visible mirror.
- Follow/orbit: name fixed landmarks, orbit direction/extent, start/end and axis handling; it must reveal an opponent, decision or spatial relation, not circle decoratively.
- Natural handheld: small irregular body/footstep-driven motion, readable faces and contact; avoid generic violent shake masking action.
- Dutch angle: a bounded roll motivated by destabilization; state when it begins or settles. Roll is not a 30-degree horizontal camera relocation.
- Stable coverage: keep emotionally important faces still enough to read. A transition from handheld conflict to stable connection is useful when motivated. No obligation to use POV, orbit, handheld and Dutch angle in every clip.

## Final delivery gate

Before delivering, check: local diagnosis and strategy present unless explicitly omitted; tail-frame role separated from first-frame binding; first cut and internal cuts audited; critical shots covered by inspected references or clearly marked pending; current visible instructions without future plot leakage; readable camera geometry and purposeful lens/depth choices; moves physically grounded; actions fit real time; final 1–2 seconds are usable editorial space. Resolve conflicts by simplifying camera/decorative detail before sacrificing physical causality, performance or continuity. Passing this gate is text validation, not proof of generated-media continuity.
