# Reference Prompt Content Module

Read only when writing or planning reference-image prompts. Paths are relative to the skill root. The main-file route/stage rules and reference_first_video_workflow.md govern actual-image authority.

## Visual Reference Image Prompts

Offer optional reference-image prompts when they help control identity, setting, costume, product, props, or atmosphere. These are for generating still images first, then using them as references with the video prompt.

For route selection, staged delivery, reference authority, static-information deduplication, and image-to-video compilation, read `references/reference_first_video_workflow.md`. The rules below define reference content; that file defines how references and video text divide control.

- Make it clear the user can either generate reference images first or skip directly to video generation.
- Do not output a complete reference set and a complete self-contained video prompt together by default. Keep the current turn scoped to the chosen production path and stage.
- Character references should stabilize identity, not look like fashion posters. Read `Reference Image Prompt Compiler` in `references/reference_first_video_workflow.md` for the character information budget. Identity/role, age range, era, facial impression, body type/posture, hair, clothing/state, dirt/wetness/injury/makeup, emotional baseline, framing and non-stylization are candidate fields, not a completeness checklist. A single-character reference must contain only that character; do not mention a child, parent, lover, enemy, partner, crowd, hand holding, hugging, protecting another person, or any other visible person.
- For principal/recurring character assets, read `character_card_prompts.md`: directly combine the text-designed identity/costume with its four-view layout; no prior portrait is required. One identity may appear in isolated panels, never as several story characters. Supporting roles, simple face-only tasks and existing satisfactory assets retain the smaller appropriate form. This card is a foundation asset and does not bypass confirmation before dependent relationship/first-frame images.
- Scene references should define usable video space with content-matched photography and light, not just inventory a room. Read `Scene photography and lighting execution` in `reference_first_video_workflow.md` alongside the scene information budget: select useful depth, visual emphasis, source-related light/shadow and material/color relationships while keeping entrances, action paths and planned performance zones readable. Use `无人物` for a clean plate; lighting a future action area does not add actors or a first-frame composition.
- When the same location needs reverse views or topology-sensitive coverage, read `Scene multi-view prevention` in `reference_first_video_workflow.md` before drafting new angles. Use only needed views; a layout sketch and numbered contact sheet are optional planning aids, not default assets.
- Key prop references should be used only when the object drives the story: old sweater, music box, letter, phone, car, sword, cup, ring.
- Choose the smallest reference set that covers required identity, space, contact and planned views. 1-2 images for simple scenes and 2-3 for some complex scenes are planning estimates, not caps. Add a distinct necessary asset when coverage requires it, reuse existing assets, and do not multiply redundant references. Distinguish the series asset library from images active in one generation; an actual tool input limit calls for compatible shot/asset batching, not silently dropping required evidence.
- Keep all references consistent with the final video prompt.
- Apply `Visual Style Integration` in `references/style_patterns.md` to the requested image asset: integrate only relevant visual qualities with its light/texture description, preserve identity and topology readability, and share the chosen look across related assets. This is not permission to add image types, change approved design, or restyle an actual selected reference.
- Initial delivery defaults to the needed identity, unpeopled scene and key prop references. Select relationship/two-shot or first/tail/action-frame references only when needed, after the actual constituent foundations are confirmed under `Foundation and combination-image dependencies` in `reference_first_video_workflow.md`. Do not output every type by default or hide a relationship inside a single-character identity image. Changed foundations require checking affected combinations before reuse.
- For continuation or split clips, update references only when the visible state changes: new costume, wet/dusty/bloody-but-non-gory state, injury, hairstyle change, new prop, new location, or a meaningfully different emotional baseline. Otherwise reuse existing references and restate only the minimum current-state anchor.

Recommended counts:

- Emotional close-up: character reference only.
- Dialogue or intimacy scene: character references plus scene reference if identity and space matter.
- Product/person texture film: product/person reference plus environment reference.
- Period drama: character/costume reference plus scene reference.
- Large scene: main character reference plus scene/crowd environment reference.
- Object-led memory scene: key prop reference plus scene reference.

