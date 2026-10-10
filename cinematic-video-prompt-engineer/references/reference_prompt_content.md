# Reference Prompt Content Module

Read only when writing or planning reference-image prompts. Paths are relative to the skill root. The main-file route/stage rules and reference_first_video_workflow.md govern actual-image authority.

## Visual Reference Image Prompts

Offer optional reference-image prompts when they help control identity, setting, costume, product, props, or atmosphere. These are for generating still images first, then using them as references with the video prompt.

For route selection, staged delivery, reference authority, static-information deduplication, and image-to-video compilation, read `references/reference_first_video_workflow.md`. The rules below define reference content; that file defines how references and video text divide control.

- Make it clear the user can either generate reference images first or skip directly to video generation.
- Do not output a complete reference set and a complete self-contained video prompt together by default. Keep the current turn scoped to the chosen production path and stage.
- Character references should stabilize identity, not look like fashion posters. Treat identity/role, age range, era, facial impression, body type/posture, hair, clothing/costume state, dirt/wetness/injury/makeup, emotional baseline, framing, light/background, and non-stylization as a candidate field menu, not a completeness checklist. Select 4-6 recurring identity/costume anchors plus one emotional baseline; add a field only when the current production state genuinely depends on it. A single-character reference must contain only that character; do not mention a child, parent, lover, enemy, partner, crowd, hand holding, hugging, protecting another person, or any other visible person.
- Scene references should define usable video space with 4-6 topology/light anchors: select only the location relationships, foreground/midground/background, entrances/exits, action path, obstacles, source light, materials, era, palette, atmosphere, or action area that affect later blocking and continuity. These are candidate fields, not a checklist. Use `无人物` if the scene reference should be clean.
- Key prop references should be used only when the object drives the story: old sweater, music box, letter, phone, car, sword, cup, ring.
- Choose the smallest reference set that covers required identity, space, contact and planned views. 1-2 images for simple scenes and 2-3 for some complex scenes are planning estimates, not caps. Add a distinct necessary asset when coverage requires it, reuse existing assets, and do not multiply redundant references. Distinguish the series asset library from images active in one generation; an actual tool input limit calls for compatible shot/asset batching, not silently dropping required evidence.
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

