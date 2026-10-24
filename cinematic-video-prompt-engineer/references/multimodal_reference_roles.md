# Multimodal Reference Roles

Read only when supplied video/audio guides new generation or mixed media need role separation. This extends existing reference authority, not video editing, extension, storyboarding or blockout workflows. Image-specific controls remain in `reference_first_video_workflow.md`; explicit user bindings, stage boundaries and evidence limits remain in the main skill.

## Assign only needed authority

- Images control the assigned identity, costume, prop, space, look or boundary state, not every visible attribute.
- Video may provide action, camera path, rhythm, scene or sound. Select the requested dimensions; motion reference does not automatically import its performers, costumes, setting, effects, music or dialogue. If the observed action/order already supplies the desired motion, bind it concisely rather than re-choreographing the same sequence in conflicting text. Specify necessary story deltas and readable endpoints.
- Audio may provide voice identity, spoken content, delivery/accent, ambience, effects or music. Bind it to the named speaker or sound source and only the requested dimensions. A voice reference does not automatically supply its words or background music. Supplied script controls words unless the user requests reuse of the recording's speech. Resolve a material conflict instead of silently merging alternatives; preserve intended overlap and offscreen speech.

Keep supplied identifiers and user-selected mappings stable. Different speaking/visible roles need unambiguous bindings; several views of one entity remain one entity. Do not infer hidden identity, relationships or motives from appearance, filename or upload order. Inspect accessible media; distinguish sampled visual states from verified motion, and listened audio from an available audio track. Preserve explicit bindings for inaccessible media, but do not invent observations or claim verified compilation; use the main skill's dependency/provisional-draft handling.

## Activate per scene

Distinguish the reusable library from this scene's inputs. Activate only materials needed for its roles; do not add unused candidates to an already sufficient user mapping. Recommend omitting irrelevant uploads where practical. If a still-supplied asset poses likely contamination, name its narrow exclusion briefly; do not append an exhaustive unused-material list or claim text exclusions guarantee isolation. Scope bindings per shot only when authority changes.

Merge necessary role statements into the existing reference binding or scene summary, within the current prompt budget; no mandatory table or extra heading. Do not repeat static descriptions or force reference images for a video/audio-only task. No new media call or dependency on another skill is introduced.

Example, assuming inspected and selected assets:

```text
图片1锁定女主身份与服装；图片2锁定走廊布局。视频1只参考闪避步法与动作衔接，不继承人物、场景和声音；摄影机按本段分镜执行。音频1只提供女主音色，台词使用本段中文原文，不采用录音里的配乐。
```
