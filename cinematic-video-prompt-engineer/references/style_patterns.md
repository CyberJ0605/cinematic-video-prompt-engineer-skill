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

- Estimate duration by playable screen content, not by source text length. Before deciding one prompt vs split prompts, count:
  - plot beats or reversals
  - dialogue delivery time plus pauses and listener reactions
  - physical actions, travel, fights, embraces, falls, object handling, or reveals
  - emotional transitions and micro-expression settling time
  - scene/location/time changes
  - camera moves and reframing needed for large body action
  - final 1-2s breath, sound tail, or bridge hold
- A short synopsis can still exceed 30s if it contains multiple beats that need to be shown clearly.
- If the full content cannot breathe within 30s, split by emotional turning point, action phase, location change, or reveal/aftermath boundary. Do not compress by simply speeding up action or removing reaction time.
- For one continuous emotional beat: `0-3s / 3-8s / 8-12s`.
- For multi-shot prompts: `镜头 01`, `镜头 02`, etc.
- Each time block should contain a visible change: action, gaze, light, spatial relation, or sound.
- Avoid stuffing unrelated story events into a single 30s prompt.
- Do not end important dialogue or peak action exactly at the final second. Reserve 1-2 seconds for reaction, breath, silence, sound tail, or visual continuation.
- Time allocation should follow drama, not equal division. If a shot contains a line plus a complex action, give it more time or simplify it.
- If the ending feels rushed, remove a detail or split the prompt instead of making the final beat abrupt.

## Prompt Sampling Range Control Principles

Use these principles before writing the final prompt and again during compression. Their purpose is to narrow the model's guessing range into a smaller, cleaner set of possible videos.

1. **具体性原则 / Observable Specificity**
   - Convert abstract intent into what the camera can see or hear: action, object, light source, texture, reflection, sound, body reaction, and timed transition.
   - Do not stop at labels such as `破碎记忆闪回`, `高级感`, `压迫感`, `命运感`, or `电影感`; translate them into visible fragments. Example: `破碎记忆闪回` can become rain on glass, a red umbrella in puddle reflection, a phone vibration, headlight flare, glass shards catching light, and a face losing focus.

2. **非矛盾性原则 / Non-Contradiction**
   - Remove instructions that cannot physically, spatially, emotionally, or temporally coexist.
   - Check object behavior, light source, camera path, costume/prop state, and action causality. Example: cloth can tear into fragments, but it should not also form a perfect blade-like arc unless it is an intentional visible VFX object.
   - If two instructions conflict, keep the one that serves the story function and rewrite the other as a compatible visual detail.

3. **正面描述优先 / Positive Target Description**
   - Say the desired path first: `小球直接滚进蓝色框`, `车从路口左转`, `角色沿走廊尽头的亮门跑去`.
   - Use negative constraints only as a small fallback for likely model failures, especially subtitles, watermarks, background music, face/body distortion, unwanted genre drift, or unsafe escalation.
   - When the scene outcome matters, do not rely on `不要...` alone. Replace `不要进红框` with `直接进蓝框`; replace `不要突然亲吻` with `两人保持半步距离，只用眼神和呼吸拉近`.

4. **避免过度指定 / Avoid Over-Specification**
   - Details should reduce ambiguity, not try to control every pixel.
   - Limit one short clip to the necessary visible targets: the main action path, emotional turn, key props, space, light source, and sound anchors. If a prompt names too many small targets, remove decorative or redundant details before adding more.
   - When quality drops or action becomes unnatural, reduce goals: fewer fragments, fewer camera moves, fewer micro-actions, fewer props, or split into another clip.

## Camera Language

Prefer specific but generation-friendly terms:

- Use standardized English abbreviations for shot size and camera movement in storyboard prompts. Chinese explanations can appear in diagnosis, but the final shot labels should use the abbreviations when professional terms are needed.
- Character shot sizes: `ECU` Detail Shot (only a facial detail), `VCU` Face Shot (forehead to chin), `BCU` Big Close-Up (full head including face), `CU` Close-Up (head and shoulders), `MCU` Chest Shot (head to below chest), `WS` Waist Shot (head to waist), `KS` Knee Shot (head to knees), `FLS` Full Length Shot (full body with head/foot room), `LS` Long Shot (person occupies about 3/4 of frame), `ELS` Extra Long Shot (person far away).
- Object/scenery shot sizes: `CU` Close-Up (local detail), `MCU` Medium Close-Up (about 1/4 of subject), `MS` Medium Shot (about 1/2 of subject), `MLS` Medium Long Shot (whole subject plus some surroundings), `LS` Long Shot (subject occupies about 3/4 to 1/3 of frame), `ELS` Extra Long Shot (farther than long shot).
- Camera movement and focus: `Dolly In/Out` or `Track In/Out` for camera physically moving forward/backward; `Pan Right/Left` for horizontal lens/head rotation; `Tilt Up/Down` for vertical lens/head rotation; `Track Right/Left`, `Truck Right/Left`, or `Crab Right/Left` for camera moving sideways; `Ped Up/Down` for vertical camera movement; `Crane Up/Down` or `Jib Up/Down` for vertical/diagonal camera movement with a crane/jib feel; `Arc/Orbit` for a curved path around the subject; `Zoom In/Out` for focal length change while camera stays physically still; `Dolly Zoom` / `Vertigo effect` for dollying one way while zooming the opposite way; `Whip Pan` or `Crash Zoom` for fast transition/emphasis; `Rack Focus` / `Focus Pull` for changing focus between foreground/background or person/object while the shot continues; `Handheld` for controlled human shake; `Static` for no camera movement.
- 焦段: `24mm`, `35mm`, `50mm`, `85mm`, `100mm macro`, `200mm`.
- 运镜: prefer the standardized movement terms above; phrases such as `Slow Push in`, `Handheld Backward Tracking`, or `Snap Pull Back` are allowed when they describe the desired feel more clearly.
- Lens texture: shallow depth of field, anamorphic flare, bokeh, Chiaroscuro, hard side light, backlight, practical light.

Do not pile up terms. Use the terms that directly serve the scene's emotion.

When a term has possible ambiguity, disambiguate by context. For example, `MCU` in a character shot means Chest Shot, while `MCU` in an object/scenery shot means Medium Close-Up. If needed, write `MCU Chest Shot` or `MCU object detail` once, then use the abbreviation consistently.

### General Camera Movement Selection System

Choose camera movement by narrative function, not as decoration. Most 6-15s prompts need only 1-3 principal moves; a simple emotional close-up may need none. If a move does not change emotional distance, reveal space, follow action, create disorientation, or mark a transition, use `Static` instead.

| Camera move | Best use | Writing rule |
|---|---|---|
| **Push-In / Dolly-In** | intimacy, tension, realization, a character being emotionally trapped | Move physically closer to the subject and end on the important face, hand, object, or decision. Keep it slow for emotion, faster only for shock or threat. |
| **Dolly-Out / Pull-Back** | reveal context, isolation, aftermath, closure, or a hidden spatial relationship | Start close enough to feel subjective, then reveal the larger room, crowd, landscape, or consequence. Do not pull back without new information. |
| **Pan Right/Left** | follow a gaze, track an entering subject, reveal adjacent space, build anticipation | Rotate from one readable subject/space to another; end on a clear target rather than vague scenery. |
| **Tilt Up/Down** | reveal height/depth, a body/object from detail to whole, power difference, vertical threat | Use when vertical information matters: tower, stairwell, falling object, kneeling/standing power change. |
| **Tracking / Truck / Crab** | walking, driving, pursuit, side-by-side dialogue, smooth movement through space | Keep camera parallel to the subject or movement path; show obstacles or destination so direction stays clear. |
| **Arc / Orbit** | show multiple sides of a character, reveal changing power, circle a confrontation, add dimension | Orbit around one stable subject or pair. Keep background readable and preserve axis logic through the visible move. |
| **Crane / Jib** | grand reveal, scale, environment, vertical transition, a subject becoming small or powerful | Rise/fall with story purpose: reveal the crowd, city, battlefield, cliff, lighthouse, or emotional isolation. |
| **Zoom In/Out** | focus attention, compress distance, isolate a face/object, observational or surveillance feel | Use when the camera should feel physically still; avoid replacing every emotional push-in with zoom. |
| **Dolly Zoom / Vertigo effect** | disorientation, panic realization, moral vertigo, world collapsing around a character | Reserve for rare turning points. State the emotion it expresses; avoid using it as a generic cool effect. |
| **Whip Pan / Crash Zoom** | sudden attention shift, energetic transition, surprise reveal, fast comedic or action beat | Use briefly. Start and end on readable subjects; preserve direction and avoid random blur. |
| **Handheld** | realism, urgency, documentary immediacy, panic, chase, unstable confrontation | Describe the intensity: subtle human shake, close handheld, or rough handheld. Do not use heavy shake when facial nuance or action readability matters. |
| **Static + angle family** | formal tension, observation, power, dread, comedy timing, precise performance | Use `Static Low Angle`, `Static High Angle`, `Static Dutch Angle`, `Bird's-Eye`, `Worm's-Eye`, or `Straight On` when perspective matters more than movement. Static is often strongest for micro-expression, interrogation, waiting, and moral pressure. |

#### Selection by Drama Beat

```text
情绪靠近：Push-In / Dolly-In, or Static CU if the face already carries enough pressure
孤独与后果：Dolly-Out / Pull-Back, Crane Up, ELS reveal
发现与期待：Pan, Tilt, Slow Push-In
并行移动：Tracking / Truck / Crab, Handheld following
权力变化：Low Angle Static, High Angle Static, Tilt Up/Down, Arc/Orbit
心理失衡：Dolly Zoom, Dutch Angle Static, brief Handheld instability
快速转场或惊讶：Whip Pan / Crash Zoom, but end on a readable subject
宏大空间：Crane/Jib, ELS, controlled Pull-Back
微表情表演：Static ECU/CU or extremely slow Push-In; avoid restless camera
```

#### Combination Rules

- Tie camera movement to a visible cause: gaze, footsteps, vehicle motion, body approach/retreat, door opening, object reveal, emotional realization, or sound cue.
- Avoid stacking `Push-In + Orbit + Zoom + Handheld + Dutch Angle` in one beat. Choose one primary move and one supporting angle or lens choice.
- Prefer `Dolly-In` for emotional approach because the camera physically enters the character's space; prefer `Zoom-In` for observation, surveillance, shock compression, or a distant watcher feeling.
- Use `Static` deliberately. A fixed frame can make a confession, threat, micro-expression, or comedy pause more powerful than constant movement.
- When cutting between shots, maintain the 180-degree axis and camera-angle rules elsewhere in this reference.

## Cinematic Lighting as Dramatic Design

Do not use `电影感布光` as a vague magic phrase. Cinematic lighting should create dramatic tension, emotional direction, visual hierarchy, and story meaning. It is not only illumination.

Do not over-describe lighting by default. Lighting language should be proportional to the scene: it must support performance, action, and story, not replace them. If the scene is mainly about dialogue, suspense movement, a fight, or a micro-expression, keep lighting concise unless the light itself is the dramatic engine.

### Lighting Detail Budget

Choose one level before writing the final prompt:

1. **Minimal / one phrase**: use for ordinary rooms, fast action, phone calls, domestic suspense, short emotional beats. Example: `低照度小黑屋，门缝冷光和手机屏光只勾出脸部轮廓，背景保留暗部细节。`
2. **Standard / one compact sentence**: use when light helps mood but is not the main subject. Mention source, direction, what is readable, and shadow mood in one sentence.
3. **Detailed / lighting design paragraph**: use only when lighting is the core test, the user asks to check lighting, or the scene is built around authority, ritual, judgment, noir pressure, product texture, stage-like composition, or a strong visual concept.

Do not repeat full Key/Fill/Rim/Volumetric descriptions in every shot. Put stable lighting once in the opening summary or first shot, then only mention changes: door opens, lamp switches off, phone screen lights a face, flashlight sweeps, neon flickers, etc.

### Motivated Light Source

Every strong light must have a believable source inside or just outside the scene: window, high window, door slit, bare bulb, table lamp, fluorescent tube, candle, TV, phone screen, police light, neon sign, car headlight, flashlight, skylight, firelight, or reflected light from table/floor/wall.

Match the light quality to the source:

- hard side-top light needs a plausible high, small, directional source and a story reason for harshness.
- soft front fill can come from weak bounce on a table, wall, floor, curtain, screen, or window diffusion.
- volumetric beams need dust, smoke, mist, rain, steam, or haze.
- rim light and strong edge highlights should not appear without a credible back/side source.

If the location does not support `Hard side-top Key Light` or `右上方硬质侧顶光`, do not force it. In a small black room, domestic interior, cramped apartment, or ordinary office, prefer motivated practical light such as a door crack, exposed bulb, desk lamp, phone screen, TV spill, window slit, corridor light, or weak ambient bounce. Hard side-top light is a specialty pattern, not the default cinematic look.

### Realistic Night Exterior and Courtyard Light

Use this for ancient courtyards, gardens, alleys, patios, palace yards, manor entrances, rooftops, or other night exterior scenes. Keep the light cinematic but physically believable.

Core rule: moonlight can shape the overall cool ambience and edges, but it should not behave like a hard spotlight cutting a face unless the scene has a very specific high opening, mist, or stylized stage reason. Faces at night are usually made readable by nearby practical sources and bounce: lanterns, candles, corridor lamps, window spill, reflected light from stone floor/walls/table, or weak soft fill.

Good night-courtyard phrasing:

```text
夜间府邸庭院，冷月光作为柔弱环境底色落在屋檐、石地和花木边缘；廊下灯笼与桌边烛火给人物脸部提供很弱的暖色反光，眼睛和颧骨保留可读细节，肩线、发冠和衣料边缘有自然的冷色轮廓高光。整体暗部有层次，不是硬切舞台光。
```

Use artistic processing with restraint:

- Let moonlight outline hair, shoulders, headdress, roof edges, tree leaves, stone floor, and distant architecture.
- Let lantern/candle/window spill reveal eyes, cheekbone, mouth line, fingers, jewelry, sleeve texture, or the key prop.
- Use `soft edge highlight`, `weak practical fill`, `stone-floor bounce`, `lantern spill`, or `candle reflection` instead of hard face-cutting moonlight.
- If the face needs stronger contrast, explain the source: a nearby lantern, side corridor lamp, open doorway, window lattice, reflective stone table, or hand-held candle.
- For period courtyards, avoid modern studio terms unless the source is disguised as a motivated practical light.

Avoid:

- `冷月光切亮脸部一侧` if there is no believable angle or reflector.
- mixing every light type in one sentence: moonlight, Rembrandt, spotlight, blinds, candle, window, golden hour, and volumetric beams all at once.
- making night exteriors look like an indoor studio portrait unless the user asks for stylization.

### Dynamic Light Interaction

Use this when the character, vehicle, train, curtain, door, window, flashlight, or weather is moving. The light should not sit still as decoration; it should interact with motion.

Good dynamic lighting links:

- repeated window light cuts across a running character's face and body
- a moving train/car causes sunlight and shadow to alternate rhythmically
- a door opening or closing changes both light level and sound bed
- a headlight, flashlight, phone screen, or TV flare reveals dust, smoke, rain, grass, fabric, or breath
- clouds, branches, curtains, rain, or passing streetlights make shadows move across walls, seats, floorboards, glass, or skin
- a character moves toward a fixed light source, making the light feel like a destination or temptation

Prompt phrases:

```text
动态光影：人物向车门/窗边/走廊尽头移动时，实景光源保持固定，身体穿过一段段明暗交替；光斑掠过脸、手、衣料和地面，阴影被拉长、压缩、再向前跃动，光影节奏与脚步和呼吸同步。
```

```text
环境颗粒：逆光只照出空气中的尘埃、雨雾、草屑、衣料纤维或呼出的白气，让空间有真实厚度；不要无来源的泛光或装饰性光晕。
```

Use dynamic light sparingly. One strong interaction is usually enough for a 15s prompt.

### Light as Emotional Direction

Light can function as a story direction, not only a look. A fixed light source can represent exit, freedom, danger, judgment, exposure, temptation, memory, or an irreversible choice.

Common use:

- shadowed foreground frames a trapped character; distant light marks the only exit
- a child or adult runs toward a doorway/window/headlight, turning light into a physical destination
- warm exterior light contrasts with cold interior shadow to show escape from control
- a bright screen, document lamp, or phone glow exposes a secret
- a car door closing cuts off exterior light and wind, turning the scene inward and silent

Keep the description concrete: name the source, where it falls, what it hides, and what action changes it.

When lighting is truly important, describe the lighting system in this order:

1. **Key Light / 主光**: direction, height, hardness/softness, color temperature, beam shape, and what it actually hits.
2. **Fill Light / 辅光**: strength and purpose. Often very weak, only keeping minimum texture instead of flattening the face.
3. **Rim Light / 轮廓光**: where it catches shoulders, ears, hair, objects, statues, weapons, or furniture edges to separate subject from darkness.
4. **Background / Volumetric Light / 背景光 / 体积光**: light hitting dust, smoke, mist, rain, curtains, windows, statues, walls, or architectural depth.
5. **Narrative meaning / 布光意图**: what the light/shadow relationship says about power, secrecy, guilt, judgment, hope, danger, intimacy, or ambiguity.

### Light Must Touch Concrete Surfaces

Avoid generic phrases like `dramatic lighting` or `cinematic lighting`. Write what the light does:

- hard side-back Key Light cuts across face, hand, table edge, and a statue
- left half of the room falls into near-black shadow
- weak ambient Fill Light keeps only a faint fabric outline
- Rim Light catches right shoulder, ear edge, hairline, and object contour
- Volumetric Light becomes visible through dust, smoke, rain mist, or thin fog
- practical light, window slit, doorway spill, police light, candle, TV, phone screen, neon, or car headlight creates motivated light

### High-Contrast Judgment / Courtroom Pattern

Use this for courtrooms, interrogations, offices of power, temples, throne rooms, police rooms, confession spaces, or any scene where authority and moral ambiguity matter.

```text
布光设计：强方向性 Key Light 来自画面右后方，偏硬，形成清晰光束，不均匀照亮人物，只切到脸的一侧、手、桌面和背景雕像/权力物件；左侧空间大面积沉入暗部，形成 Chiaroscuro 明暗秩序。Fill Light 极弱，只保留衣料和面部少量暗部层次，不把阴影填平。Rim Light 擦过右肩、耳朵、发缘和雕像边缘，把人物从黑色背景中分离。背景有尘埃/薄雾中的 Volumetric Light，光束本身成为画面的一部分。布光意图：人物处在光与暗的交界处，表达权力、法律、秘密或道德判断并不纯粹，庄严中带暧昧和压迫。
```

### Lighting Prompt Template

Use a compact version inside final prompts:

```text
光影：Key Light 从{方向}以{硬/软}光切入，只照到{脸/手/桌面/道具/背景物}；Fill Light 极弱，保留{衣料/暗部轮廓}，不填平阴影；Rim Light 勾出{肩膀/耳朵/发缘/道具边缘}；背景{烟雾/尘埃/雨雾/窗帘}里有 Volumetric Light，形成可见光束。整体明暗关系服务{审判/秘密/压迫/孤独/暧昧/希望}。
```

### Common Lighting Failures

- Only writing `电影感布光`, `高级光影`, or `氛围感强` without direction, object, shadow, or meaning.
- Turning every shot into a full lighting lecture when the scene only needs a compact practical-light cue.
- Forcing `Hard side-top Key Light` or `右上方硬质侧顶光` into environments where no believable high hard source exists.
- Lighting everything evenly so the image loses visual hierarchy.
- Adding too many light sources with no motivation.
- Using rim light, fog, lens flare, and glow everywhere without story reason.
- Describing light color but not what it hits or hides.
- Forgetting that shadow is part of the lighting design; decide what should fall into darkness.

### Off-Frame High Side-Back Light + Soft Front Fill

Use this for courtrooms, public hearings, institutional interiors, ceremonial halls, stage-like dialogue scenes, or character tableaux where the space needs scale and atmosphere but the face must remain readable.

Core pattern:

```text
Off-frame high side-back light 从人物身后偏高处斜射进入画面，通常来自画面外窗光、天窗、门缝或高处实景光。光线穿过烟雾、尘埃、雨雾或薄雾形成 Volumetric Beams，把背景人群、空间纵深和前景主体分层。人物脸部不做强烈阴影切割，而用 Soft Front Fill 或桌面/地面/墙面反弹的弱环境光轻轻补亮，让表情清楚，情绪不变成恐怖阴森，而是可以更坦然、荒诞、克制或自嘲。
```

Use this distinction:

- `Rim Light`: deliberate, more defined contour light, often commercial or stylized, clearly separating the outline.
- `Soft edge highlight`: softer edge lift created by high side-back light catching hair top, ear, shoulder, cheek edge, or clothing folds. It is not a strong commercial rim light.

Prompt phrase:

```text
光影：画面外高位侧逆光 Off-frame high side-back light 从左上/右上斜射进来，穿过薄雾形成大面积 Volumetric Beams，拉开前景人物、背景人群和空间深度；人物脸部由 Soft Front Fill 或桌面反弹光轻轻补亮，保留表情可读性；头发顶部、耳朵和肩膀只有 Soft edge highlight，不是强商业 Rim Light。
```

### Color Temperature as Story

Color temperature contrast should express story, not decorate the frame.

- Cold white light can suggest system, reason, distance, institution, loneliness, or emotional detachment.
- Warm white light can suggest humanity, memory, body temperature, fate, intimacy, or moral ambiguity.
- In symmetrical compositions, color contrast can make an apparently balanced frame emotionally unstable.

Prompt phrase:

```text
中心对称构图带来秩序和平衡感；左侧冷白光代表制度、理性和距离，右侧暖白光代表人性、温度和命运，两种色温在人物周围并置，让画面同时有公平感和复杂情绪。
```

### Low-key High Contrast Tonal Structure

`Low-key High Contrast` is a tonal structure, not a filter. Tonality is the planned distribution of dark values, midtones, highlights, black point, and shadow detail before the shot is generated. If the tonal base is wrong, post-filter words cannot reliably create the style.

Use `Low-key High Contrast` when the scene needs pressure, mystery, premium texture, crime atmosphere, interrogation, noir, restrained luxury, or dark psychological weight.

Characteristics:

- dark areas dominate the frame
- clean black point, not muddy gray
- concentrated local highlights
- wide range from deep black to controlled bright spots
- shadow detail remains visible
- subject is cut out by local light
- background is suppressed but not dead black
- light comes from motivated sources such as table lamp, flashlight, window slit, fluorescent tube, neon, candle, car headlight, phone screen, or product edge light

Prompt phrase for crime/interrogation:

```text
影调：Low-key High Contrast，暗部作为画面基底，黑位干净但保留暗部细节；审讯室桌面一盏台灯形成小面积硬质光池，只照亮人物脸部一侧、双手和桌面文件，背景压入深阴影但不是死黑，人物从黑暗中被局部光切出来。
```

Prompt phrase for product/luxury:

```text
影调：Low-key High Contrast，高端广告质感，深色极简背景压暗但保留层次；产品边缘有精致窄轮廓光，玻璃/金属表面出现可控镜面高光，主体被局部光切出，暗部不脏不死黑。
```

Common tonal failures:

- calling it a filter instead of designing the light and tonal range
- making the whole image underexposed without highlight structure
- crushing shadows into dead black with no object separation
- using bright fill that destroys the low-key base
- adding random glow instead of concentrated motivated highlights

### Hard Side-Top Light for Rough Dangerous Characters

Use this for rough male characters, criminals, violent patriarchs, dirty antiheroes, exhausted interrogators, underground fighters, or any role that needs danger, anger, pressure, and tactile skin texture. Keep the subject adult when violence, intimidation, or criminal atmosphere is involved.

Use it only when the set can justify a high hard source: bare overhead bulb, high window, inspection lamp, ceiling practical, industrial fixture, interrogation lamp angled upward/sideward, doorway slit from above, car headlight from a raised angle, or similar motivated light. If the scene is a cramped domestic room, small black room, ordinary apartment, or soft emotional space, do not default to this pattern; use weaker motivated practical light instead.

Core logic:

- **Hard side-top Key Light**: usually from upper right or upper left, cutting downward across the face and fists. It creates hard highlights on forehead wrinkles, nose bridge, nose tip, cheekbone, knuckles, leather, sweat, grime, and worn fabric.
- **Deep shadow zones**: eye sockets, opposite cheek, beard depth, under brow, neck folds, and jacket gaps fall into dense shadow. This makes the character less predictable and more oppressive.
- **Weak front fill**: very low Soft Front Fill keeps minimal readable detail on the shadow side of face, fist, and clothing. It prevents dead black but must not erase the high-contrast shadow design.
- **Rough edge highlight**: high side/back light catches hair, shoulder, forearm, leather jacket edge, and hand outline. It should feel dirty, hard, and textured, not glossy commercial Rim Light.
- **Texture purpose**: the light is designed to reveal rough skin, pores, wrinkles, sweat, dust, stubble, scars, old leather, and dirty fabric. It should make the character feel coarse, angry, dangerous, or physically heavy.

Prompt phrase:

```text
光影：右上方硬质侧顶 Key Light 斜切人物，强高光落在额头皱纹、鼻梁、鼻头、左侧脸颊、拳头和旧皮衣边缘；眼窝、右脸、胡须深处和颈部压入浓重阴影，形成 Low-key High Contrast 的压迫感。Soft Front Fill 极弱，只保留右侧脸、拳头和衣服暗部的最低细节，避免死黑但不削弱阴影。高位侧后光在头发、肩膀、手臂和皮衣边缘形成粗糙 Soft edge highlight，使人物从昏暗背景里分离，突出脏、硬、粗粝、危险的质感。
```

Avoid:

- beauty lighting, smooth skin, clean fashion portrait texture
- bright front fill that makes the face friendly or flat
- pure black shadow with no beard, fist, or clothing detail
- over-polished commercial rim light if the character should feel dirty and dangerous

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

## Live Performance Realism System / 活人感表演真实系统

Use this system when the scene depends on human presence rather than plot mechanics alone: close human drama, dialogue, everyday realism, intimacy, hesitation, concealment, explanation, lying, regret, memory, restrained grief, soft refusal, or any prompt where the viewer should feel the character is thinking in real time.

Do not print all six modules by default. Select only the modules that solve the scene's realism problem. For ordinary emotional dialogue, 2-4 concise live-performance cues are usually enough. For a long close-up or phone/live-action realism test, use more detail.

### 1. Psychological Motivation Drives Performance

Do not ask the character to "make a face." First decide what the character is doing internally: explaining, hiding, remembering, testing, lying, regretting, pretending to be relaxed, suppressing panic, or trying not to hurt someone.

Then align:

- eye direction and blink timing
- mouth corners, lips, brow, jaw, and throat
- voice texture, pace, hesitation, and pause placement
- breath and small recovery after key words
- whether the smile reaches the eyes

Positive pattern:

```text
她不是直接表现悲伤，而是在努力保持平静。说话前短暂低头，像在组织语言；抬眼时眼神没有完全对准镜头；说到关键处停顿半拍，嘴角轻微收紧；最后轻轻笑一下，但笑意没有完全到眼底。眼神、表情、语气和停顿都服务于“克制地解释一件自己在意的事”这个心理状态。
```

Avoid:

- fixed fake smile
- empty eyes
- sudden expression jumps
- exaggerated crying/laughing
- face emotion and dialogue meaning not matching
- voice tone detached from expression
- staring into camera without thought
- no pauses, like reading lines

### 2. State-Driven Incidental Body Language

Do not add actions to make the frame busy. Let small actions leak out of the character's current state, social relationship, and speaking purpose.

For serious explanation, hesitation, restraint, or concern, use low-amplitude movements near the body or table:

- small nod
- slight forward lean
- shoulders relaxing with breath
- fingers rubbing cup rim
- re-gripping a cup
- fingertip pause
- adjusting sleeve cuff
- tiny posture correction
- brushing a loose hair only if it fits the social state

Positive pattern:

```text
动作动机要求：不要为了让画面丰富而加入明显动作。她正在克制地表达一件自己在意的事，因此肢体动作保持低幅度、低姿态、靠近桌面，主要表现为轻微点头、短暂停顿、身体小幅重心变化、手指与杯子的细微接触、整理袖口或碎发。动作像边说边想时自然流露出来的无意识反应。
```

Avoid:

- sudden chin-on-hand pose
- big arm lift
- posed cute gestures
- exaggerated hand waving
- actions that show off movement rather than psychology
- actions that change the character's emotional state by accident

### 3. Biomechanical Linked Motion

Real bodies do not move as isolated parts. When one part moves, connected parts respond.

Useful linked-motion logic:

- Eyes usually react before the head.
- A head turn brings neck and shoulder compensation.
- A hand move involves forearm, wrist, fingers, sleeve, and small torso weight shift.
- Breathing affects chest, shoulders, voice, and pause rhythm.
- A nod is not only the head moving; eye focus, neck, shoulders, and breath all subtly participate.

Positive pattern:

```text
她抬眼看向镜头前，眼睛先从桌面移开，随后下巴轻轻抬起，颈部自然跟随。说话时肩膀随呼吸有轻微起伏，身体重心有很小的前后变化。左手扶住杯子时，手腕、前臂和袖口产生细微联动，不要让手像独立物体一样移动。
```

Avoid:

- isolated body-part motion
- head moving while shoulders and neck freeze
- stiff neck
- floating arms
- no breath movement
- missing muscle/cloth linkage
- robot keyframe motion

### 4. Physical Contact and Object Weight

When the character touches an object, write contact as a physical process: before contact, contact, pressure/resistance, and aftermath.

For example, gripping a cup:

```text
左手指尖先轻轻靠近杯沿，短暂停住，随后拇指和食指扶住杯壁。杯子保持稳定，只出现极轻微的受力变化。手指在杯壁上小幅摩擦时有停留和阻力感。袖口靠近桌面时产生轻微褶皱变化，手臂移动不要穿过杯子或纸袋。
```

Use contact cues for:

- cup, phone, letter, ring, sleeve, table edge, door handle, chair, bed sheet, sword hilt, bag, paper, glass
- weight, friction, pressure, inertia, cloth tension, shadow/reflection change

Avoid:

- hand-object penetration
- object moving before contact
- floating cups/phones/props
- no weight or resistance
- fingers not aligning to object surface
- clothes with no fold response
- unclear table/body spatial relationship

### 5. Environment Response to Human Action

The character should not feel pasted onto the background. Small human actions should create small environmental responses.

Use subtle feedback:

- loose hair lags half a beat after a head turn
- sleeve fold changes when the forearm moves
- cup reflection changes as a hand approaches
- paper bag edge compresses slightly under touch
- warm light and shadow shift slightly as the character leans forward
- room tone, cloth sound, cup sound, breath, chair creak, or phone vibration responds to action

Positive pattern:

```text
她轻微前倾说话时，脸上的暖光和阴影有细小变化，额前碎发随头部移动轻微晃动后慢慢停住。左手靠近杯子时，杯壁反光随手的位置发生细微变化。袖口贴近桌面产生轻微褶皱，纸袋保持稳定但有真实纸张质感。
```

Avoid:

- character pasted onto background
- hair completely static
- clothing behaving like a flat texture
- light not responding to body angle
- objects with no reflection or shadow change
- unmotivated wind effects
- environment response becoming too large or stealing attention

### 6. Camera, Light, Focus, and Space Consistency

First decide the shooting condition: phone realism, handheld documentary, restrained film drama, period candlelight, low-key crime, commercial product, or another coherent visual mode. All camera distance, stabilization, focus, light, skin texture, background blur, grain/noise, and spatial scale should belong to that same condition.

Phone/live-action realism is one option, not the default for all cinematic prompts.

Phone realism pattern:

```text
画面像手机在晚上室内自然拍摄，半身近景，镜头略高于桌面，轻微手持晃动但不影响观看。暖色顶灯是主要光源，脸部和手部阴影方向一致。背景轻微虚化但仍能看出家庭空间，画面保留轻微噪点、压缩感和真实皮肤纹理。焦点稳定，但有非常轻微的自然呼吸感。
```

Avoid:

- commercial-ad look in a casual phone-realism scene
- perfect studio lighting when the scene claims natural home light
- plastic skin or heavy beauty smoothing
- overly stable camera in a handheld setting
- inconsistent light direction
- wrong scale between character and background
- severe focus drift
- over-clean image with no real texture

### When to Use Lightly vs Strongly

Use strongly for:

- face close-ups
- dialogue-driven scenes
- daily-life realism
- restrained emotion
- lying, explaining, remembering, hiding, testing
- intimate but non-explicit emotional beats
- phone/live-action realism

Use selectively for:

- fights: mainly biomechanics, contact, environment response
- large scenes: mainly camera/space consistency and one human anchor
- product films: mainly contact, light, reflection, material response
- period drama: mainly psychological motive, biomechanics, cloth/light response

## Intense Emotional Scene Director Chain

Use this for emotional confrontation, restraint breaking, confession, betrayal, reunion, intimacy, or any scene where an internal conflict becomes a decisive physical action.

### Performance Chain

Build the scene in this order:

```text
内在冲突 -> 生理反应 -> 微表情 -> 贯穿动作锚点 -> 决定性行为
```

Example logic:

```text
角色内心渴望靠近，却表面死守边界；因此眼睑颤动、咬肌绷紧、喉结干咽；手指持续绞紧衣料；当防线崩塌时，手先松开、悬停，最后才完成靠近或触碰。
```

### Recurring Action Anchor

Choose one small action or prop to carry the emotional continuity:

- gripping and releasing a bedsheet, sleeve, cup, letter, ring, door handle, phone, sword hilt, or chair edge
- a hand reaching halfway, freezing, withdrawing, then finally completing the action
- breath repeatedly stopping and restarting
- gaze avoiding, returning, then locking onto the other person

The anchor must evolve with the emotion. Do not reset the hand, prop, or posture between time blocks.

### Physical Space Before Large Movement

If the scene moves from ECU/CU into a large body action, prepare the frame first:

```text
大动作前 -> 镜头拉开或快速后撤 -> 留出身体运动空间 -> 跟随动作改变机位/构图
```

Use this before:

- standing, falling, turning over, embracing, pushing away
- full-body confrontation or physical struggle
- throws, tackles, large costume movement

Avoid asking an ECU shot to suddenly show a complex full-body action without a framing transition.

### Action-Motivated Camera

Camera movement should be caused by performance:

- gaze shift -> slight pan
- head lowering/raising -> tilt down/up
- emotional approach -> slow push-in
- sudden full-body movement -> snap pull-back or wider reframing
- fall or drop -> controlled tilt down
- retreat -> backward tracking

Do not add camera movement only to make the prompt sound cinematic.

### Action-Light-Sound Binding

Bind the same action to visual and sonic consequences:

- body crosses blinds -> light stripes break and move across skin
- hand releases fabric -> cloth tension and friction sound change
- turn or fall on bed/floor -> mattress, sheet, floor, dust, or furniture reacts
- object contact -> one clear impact sound and a visible environmental response

This creates one readable event instead of three unrelated descriptions.

### Internal Beats in a Single Take

A one-take scene still needs internal dramatic sections. Use 2-4 beats such as:

```text
压抑建立 -> 关系刺激 -> 防线松动 -> 决定性行为 -> 余韵
```

Keep camera continuity, but let framing, distance, gaze, action anchor, light, and sound evolve at each beat.

### Ordinary Drama One-Take Blocking System

Use this for ordinary drama, suspense, romance, family conflict, intimate tension, waiting, investigation, or quiet confrontation when the scene can physically unfold in one continuous space. It is separate from action-fight long takes: the goal is readable blocking, emotional pressure, and spatial continuity rather than impact spectacle.

#### One-Take Arc

Design the shot as one continuous camera sentence:

```text
起幅 establishing start -> 行进/靠近 movement or emotional drift -> 关系转折 turning beat -> 焦点/前后景切换 focus or blocking shift -> 落幅 held ending
```

Each part must change something visible: distance, eyeline, body position, foreground/background relation, light crossing the face, object contact, sound, or emotional pressure.

#### Camera Path and Blocking

- Start with a clear spatial anchor: doorway, corridor, table, sofa, window, mirror, bed edge, kitchen island, hospital curtain, elevator door, or other fixed object.
- Keep one physically possible camera path. Avoid asking the camera to pass through walls, teleport, or circle a small room without enough space.
- Let the camera change shot size through distance, not cuts: `LS/MLS` to establish, `MCU/CU` for pressure, then `Pull-Back` or slight `Track` if a larger body action needs room.
- Use foreground objects to create depth: door frame, hanging cloth, glass reflection, table edge, chair back, curtain, hallway corner, bedpost, shelf, or mirror edge.
- If using a foreground occlusion as a hidden transition inside a one-take style shot, the next view must preserve screen direction, body position, lighting state, and emotional continuity.

#### Focus and Attention Shift

Use `Rack Focus` / `Focus Pull` when the drama shifts between:

- a face and a key object: phone, letter, cup, ring, weapon, medicine, door handle
- foreground listener and background speaker
- reflection and real body
- hand action and facial reaction
- outside threat and inside reaction

Focus changes should follow attention. Do not add focus pulls if the story has no competing visual priorities.

#### Multi-Person One-Take Blocking

For 2-4 people in one space:

- Assign stable geography first: who begins foreground/background, screen left/right, seated/standing, near/far from exit or key object.
- Let power shift through blocking: one person steps closer, sits down, turns away, crosses behind another, enters light, blocks the exit, or becomes isolated in background.
- Keep eyelines readable. If the camera crosses the 180-degree axis, do it through a visible move around the characters or a neutral frontal/back view.
- Use focus or body blocking to change the subject rather than cutting: foreground listener sharp -> background speaker sharp -> key object sharp -> final face.
- Avoid making everyone move at once. In a short 10-15s one-take, usually one main mover and one reacting anchor is enough.

#### One-Take Character Reveal Ladder

Use this when a one-take scene must reveal several important characters in a hierarchy, family power tableau, courtroom/banquet/council confrontation, or period-drama group portrait. The useful pattern is progressive disclosure, not dumping all faces at once.

```text
single-character ECU/CU -> visible orbit or move behind the character -> lateral reveal of a second character -> pull-back to show hierarchy and space -> held group relation
```

Rules:

- Start with one face only when identity or authority matters. Keep other characters out of frame or deeply obscured until their reveal beat.
- Use the first character's shoulder, back, hair crown, sleeve, chair, or pillar as a foreground mask while the camera moves. This gives the reveal depth and prevents a random cut feeling.
- Reveal the next character from a motivated direction: slide past the first character's shoulder, pass a column, move around a table edge, or shift focus from foreground back to background.
- After the reveal, pull back or widen only when the spatial hierarchy matters: who stands, who sits, who is foreground/background, who occupies the main seat, who is visually suppressed.
- Keep every revealed character visually distinct: face shape, hairstyle, headdress, costume color, fabric texture, posture, status, and emotional baseline. Use compact identity tags such as `嫡长子-深青锦袍高冠`, `嫡长女-朱红织金长裙`, rather than repeating full paragraphs in every beat.
- Do not reveal more than 2-4 key characters in a 10-15s one-take. If the scene needs more people, make extras background silhouettes or split into multiple clips.
- In final prompts, avoid long lighting/style ingredient lists. Put stable atmosphere once, then use reveal beats to describe what changes: face -> back silhouette -> second face -> widened courtyard/table hierarchy.

Useful compact phrase:

```text
一镜到底人物揭示：先以{角色A} ECU建立身份与压迫感，镜头绕到其肩背形成前景遮挡，再沿其右肩/桌沿缓慢横移揭示{角色B}，最后 Pull-Back 展开{庭院/厅堂/桌面}的主次站位；每个角色用不同脸型、发型、服色、姿态和眼神锁定身份，不出现重复脸或多余人物。
```

#### One-Take Prompt Template

```text
基础概括：{时长}单场景一镜到底长镜头，{地点}，{人物关系/情绪冲突}。镜头从{起幅空间锚点}开始，沿{明确路径}连续移动，不切镜头；通过人物走位、焦点转移、前景遮挡、光线变化和声音变化完成情绪推进。

0-{a}s：{起幅与空间关系}，{主角初始动作/心理状态}，镜头{Static / Slow Dolly-In / Track}，建立{出口/关键物/另一人位置}。
{a}-{b}s：{人物行进或关系压力上升}，镜头随{脚步/视线/手部动作}调整，必要时 `Rack Focus` 从{前景/物件/监听者}转到{说话者/反应者}。
{b}-{c}s：{转折动作或台词}，人物走位改变权力关系，前景{门框/桌沿/玻璃/布帘}短暂遮挡但不切断空间连续性。
{c}-结尾：镜头落在{最终面孔/物件/空间后果}，保留1-2秒沉默、呼吸、环境声或动作余韵。
```

#### One-Take Failure Warnings

- Do not choose one-take for several locations, big time jumps, too many plot turns, or dense exposition.
- Do not use `one-take` as a label while describing invisible cuts, unrelated angles, or impossible camera positions.
- Do not overload the shot with every camera move. One main path plus one motivated focus or framing change is usually enough.
- Do not end at the exact moment of a line, kiss, slap, reveal, or door opening; hold the consequence.

## Dialogue-Driven Performance Control System / 台词驱动表演控制

Use this when the scene depends on spoken performance: accusation, rebuttal, confession, breakup, apology, interrogation, courtroom pressure, family confrontation, voice message, phone call, or a line that breaks the character's emotional defense.

This system is especially useful for dialogue scenes from 10-30s. Use 16-30s only when the line delivery, listener reactions, pauses, and emotional curve genuinely need the extra time; keep shorter scenes short instead of stretching them.

### Three-Layer Prompt Structure

For complex acting scenes, separate the prompt into three mental layers before writing the final copy:

1. **Global control layer**: duration, location, characters, identity anchors, costume, voice/sound mode, broad visual style, and any required aspect ratio or platform constraint.
2. **Shot timeline layer**: which shot covers which seconds, who is being observed, when view/focus changes, and why the camera changes attention.
3. **Performance control layer**: what the character wants in this line, how emotion changes, which words trigger the change, where the pause/breath happens, how eyes/face/body respond, and which reaction must not happen too early.

Do not let layer 1 consume the whole prompt. If a platform already provides visual style presets, keep style compact and spend more tokens on performance control.

### Emotion Barrier / 情绪保护层

Do not jump directly from anger to crying, confidence to collapse, or sarcasm to confession. Real characters often use a protective emotion before the vulnerable emotion appears.

Common protective arcs:

```text
anger protects grief -> voice cracks -> attack fades -> vulnerability appears
sarcasm protects shame -> smile stiffens -> eyes drop -> apology becomes possible
calm protects panic -> breath shortens -> words slow -> body freezes
politeness protects resentment -> pauses sharpen -> mouth tightens -> direct accusation
```

Prompt rule:

```text
先写保护性情绪，再写保护层出现裂缝，最后写真实情绪暴露。不要让愤怒、悲伤和落泪同时从第一秒出现。
```

### Dialogue as Expression Timeline

Do not write a mood label and paste dialogue under it. Treat the line itself as the expression timeline.

For every crucial line, write:

- state before speaking
- first phrase delivery
- trigger word or emphasized word
- pause / breath / swallow
- eye line change
- mouth, brow, jaw, throat, or tear change
- body/hand reaction
- state after the line
- listener reaction when relevant

Positive pattern:

```text
说话前她先压住呼吸，目光没有立刻看向对方。第一句“你一直都知道”音量较低，嘴唇几乎不张开，像还在维持体面；说到“知道”时短暂停顿半拍，眼神从对方脸上滑到桌面。第二句“那我算什么？”明显更轻更慢，重新抬眼时攻击性已经消失，眼眶开始湿润，但第一滴眼泪仍不能落下。
```

Bad pattern:

```text
她非常悲伤地哭着说：“你一直都知道，那我算什么？”
```

### Trigger Words and Delay

When a line causes an emotional turn, mark the trigger word and delay the visible reaction by a believable fraction of time.

Examples:

- A character should not cry before hearing the plot-changing word.
- A character should not soften before saying the vulnerable phrase.
- A character should not explode before the accusation lands.
- First tear should appear only after the defensive layer breaks, not at the start of the line.

Useful instruction:

```text
不要让落泪提前发生。泪水只在说完关键词后开始聚在下睫毛处，下一次吸气失败时才落下第一滴。
```

### AU/FACS Auxiliary Calibration

AU/FACS can help calibrate a close-up, but it is not the main language of the prompt. Always write visible natural-language actions first, then add optional AU tags only for high-stakes face close-ups.

Recommended use:

- Use AU only for long close-ups, extreme emotional control, crying restraint, anger restraint, shame, guilt, blackening, or close dialogue scenes where facial precision matters.
- Use compact tags, not long code strings.
- Include intensity only when it clarifies gradual change: `A` = barely visible, `B` = light, `C` = clear, `D` = strong, `E` = near maximum.
- Write onset -> peak -> release when possible.

Useful AU references:

- `AU1`: inner brow raise
- `AU4`: brow lower
- `AU5`: upper lid raise
- `AU7`: lid tighten
- `AU9`: nose wrinkle
- `AU15`: lip corner depressor
- `AU17`: chin raiser
- `AU23`: lip tighten
- `AU25`: lips part
- `AU26`: jaw drop

Positive pattern:

```text
自然语言先行：眉毛内侧缓慢抬起，嘴角轻微下沉，下巴开始绷紧；她张开嘴想继续说话，却没有力气发声。辅助表情校准：AU1 + AU15 + AU17，强度从 B 增至 C，眼泪暂时不能落下。
```

Avoid:

- using AU as a magic formula without natural-language description
- listing too many AU codes in one beat
- making all facial muscles peak from the first frame
- treating one AU combination as a fixed emotion regardless of gaze, body, voice, and context

### Facial Action Timing

For important expressions, specify the change curve:

```text
onset -> peak -> release / transform
```

Example anger burst:

```text
说话前他先压紧嘴唇，咬住下颚，眉毛向内下压。前半句保持低沉；说到“现在”时 AU25 和 AU26 突然增强，嘴唇分开、下巴绷紧，音量短促抬高。最后一个词结束后立刻闭嘴，面部肌肉快速收回，只剩呼吸变重。
```

### Eight-Dimension Acting Formula

Use this as an internal planning formula for dialogue-led acting. Do not print all labels unless the user asks for a table.

```text
时间段 -> 人物目的 -> 情绪保护层/变化 -> 台词与触发词 -> 面部动作 -> 目光与身体 -> 声音/呼吸/停顿 -> 说完后的状态与对手反应
```

Compact final-prompt pattern:

```text
{a}-{b}s：{人物}表面想{目的}，其实在用{保护性情绪}挡住{真实情绪}。说“{台词}”前先{呼吸/停顿/眼神}；说到“{触发词}”时{面部动作、目光、身体或AU辅助}，声音{音量/速度/质感}；说完后{余韵状态}，{对手反应}。
```

### Dialogue Performance Conditions

When dialogue is important, attach it to performance conditions:

- exact action moment when the line begins
- voice volume, breath, pace, and vocal texture
- physiological state such as swallowing, broken breath, clenched jaw
- listener's immediate reaction

Keep the line short enough for the assigned time.

## 30s Psychological Stage Timeline

Use this pattern for 20-30s emotion-led scenes where the viewer must feel a full internal turn: farewell, breakup, confession, accusation, reunion, apology, forgiveness, acceptance, or choosing to let someone go. It is a bridge between dialogue-driven acting and ultra-close micro-expression work.

### Core Principle

Do not divide a 30s scene by clock time alone. Divide it by psychological tasks: what the character is trying to do inside this phase.

Good stage names are small verbs or emotional tasks:

```text
追问 -> 认命 -> 记住 -> 惋惜 -> 放手
试探 -> 防御 -> 被击中 -> 坦白 -> 余震
克制 -> 反击 -> 裂缝 -> 承认 -> 沉默
```

Each stage should contain:

- stage title / psychological task
- visible action, expression, eye line, breath, voice, or body evidence
- one short line or a meaningful silence when needed
- how this stage differs from the previous stage
- a clear tear, smile, gaze, breath, or posture timing decision when relevant

### Action + Meaning Workflow

In `电影化改写策略`, you may briefly explain why an action matters. In the copy-ready final prompt, keep the visible behavior and only a compact meaning note when it prevents ambiguity.

Good workshop reasoning:

```text
“短促苦笑”不是开心，而是自嘲和认命；“重新看回对方”不是挽留，而是想最后记住他的样子。
```

Good final-prompt compression:

```text
3-10s【认命】：她的视线从他脸上慢慢移开，望向旁边空地；眼睑低垂，嘴角牵起一抹很短的苦笑又落下，鼻翼轻收，胸口轻轻起伏一次，像把委屈咽回去。
```

Avoid turning the final prompt into long prose analysis:

```text
情感解析：这个动作象征她内心的命运感、遗憾、回忆和复杂人生……
```

### Difference Between Similar Expressions

When the same visible expression appears twice, define the emotional difference.

- First smile may be self-mockery, politeness, defense, or disbelief.
- Last smile may be forgiveness, release, blessing, or exhausted tenderness.
- First gaze may be asking for an answer.
- Later gaze may be memorizing, accusing, forgiving, or saying goodbye.

Useful instruction:

```text
前一个笑是自嘲和认命，最后一个笑是温柔放手；不要把两个笑都生成成同一种甜笑或假笑。
```

### Tear Timing and Delay

Control tears as timed events, not generic sadness.

Common sequence:

```text
眼眶泛红但不落泪 -> 眼泪被屏住 -> 第一滴泪在保护层松开后落下 -> 第二滴泪在最终台词或微笑中滑落 -> 结尾保留泪痕和呼吸
```

Rules:

- Do not let tears appear before the emotional trigger.
- If the character is restrained, hold tears for several seconds before the first drop.
- Name which tear matters: first tear, second tear, tear line, tear held on lower lashes, tear sliding to the lip.
- Do not overuse tears in every stage; one or two precise tear events are stronger than constant crying.

### Camera Push Bound to Emotional Access

Use camera movement only when emotional distance changes.

- Start with stable CU/BCU when the character is still guarded.
- Use a very slow push-in when the character stops defending or decides to reveal vulnerability.
- Use ECU only for the peak stage: the line, tear, smile, or gaze that changes the meaning.
- Keep the final frame long enough for the viewer to read the expression after the last line.

Do not add push-in, orbit, handheld shake, and rack focus together for a quiet emotional scene. One motivated push or a fixed camera is usually enough.

### 29-30s Farewell Template

Use as a structure reference, not as a fixed story:

```text
基础概括：29秒写实电影情绪长镜头，{人物}面对镜头前的“他/她”，以{关系危机}为核心；固定 CU 起幅，后段极慢 Push-In 至 ECU。全片靠眼神、呼吸、短句、停顿和两次明确落泪完成情绪曲线，不大哭，不崩溃。

0-3s【追问】：她直视镜头，眼神还干净没有泪，眉心轻蹙，嘴唇微启，轻声说：“真的要走吗？”说完不追问，停在等待里。
3-10s【认命】：视线慢慢移开，眼睑低垂；嘴角牵出一抹短促苦笑又落下，鼻翼轻收，胸口小幅起伏一次，像把酸楚咽回去。
10-17s【记住】：镜头极慢推进；她重新看回镜头，目光在对方脸上缓慢扫过，眼眶泛红但眼泪被屏住，嘴唇轻动又抿住，下巴收紧，喉间轻轻滚动，留 0.5s 死寂。
17-23s【惋惜】：她垂眼，第一滴泪无声落在衣襟上；没有擦泪，没有抽泣。再抬眼时，目光从挽留变成深深惋惜，眉心一点点松开，极轻地摇头，像无声叹息。
23-29s【放手】：镜头推至更近 ECU；她努力牵起一个很轻、很柔的微笑，第二滴泪从眼角滑过鼻翼停在唇边。她用几乎听不见但稳住的声音说：“你走吧。”说到“走”字时声音极轻颤一下又压住。说完后笑停在脸上，眼神不移开，最后 1-2s 留给含泪微笑和安静呼吸。
```

Compression rule: for 20-24s, reduce to 4 stages. For 10-15s, do not force this full pattern; use a shorter micro-expression timeline instead.

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

#### Coquettish Soft Refusal Arc

Use for safe, non-explicit intimacy, playful sulking, shy protest, or a character saying something like `我不要` while the real emotion is closer to softness, trust, affection, and tiny willfulness. It must not read as real fear, coercion, or serious rejection.

Core setup:

```text
固定 ECU/CU 或极轻微 Push in，人物正对镜头或面对近处对方，表演强度控制在三分；没有夸张撒娇动作，没有性感化挑逗，重点是眼神、嘴角、呼吸、手指小动作和台词气声。
```

Emotional logic:

```text
整体不是真正的反感拒绝，而是带着亲近关系中的小任性、软萌娇憨和被宠爱的安全感。台词可以是“我不要”，但眼神、笑意和身体并没有真正推远对方。
```

Emotional waveform:

```text
0-1s：人物先看向镜头/对方，手时轻时重，指尖带着犹豫又亲近的小动作；脑袋微微偏向一侧，眼神带点软乎乎的不情愿，嘴角轻轻抿出一点别扭弧度。
1-2s：眼尾微微弯起，眼底藏着顽皮和被纵容的安全感，嘴唇轻轻开合，用很轻、很软、带鼻音的气声说：“我不要。”语气更像撒娇式推拒，而不是生硬拒绝。
2-4s：说完后视线轻轻躲开半秒又偷偷回到对方身上，嘴角忍不住漫上一点浅笑；因不好意思微微垂眼，睫毛颤动，肩颈放松，身体没有后退。
4-6s：轻笑被压回唇边，嘴角抿住又泄出一点笑意，眼神变得更柔；最后保持近距离、软软的别扭感，像仍在嘴硬，但心里已经被哄软。
```

Compression phrase:

```text
她轻轻偏头，眼神软乎乎地躲了一下，嘴角抿出别扭弧度，用很轻的气声说“我不要”；说完又偷偷看回对方，忍不住压出一点浅笑，身体没有后退，情绪是娇嗔式软拒绝而不是真正抗拒。
```

Avoid:

- turning `我不要` into fear, panic, disgust, or real refusal unless the story asks for it
- overt seduction, exposed body emphasis, or sexualized camera language
- exaggerated pout, cartoon acting, childish baby voice, or idol-drama overacting
- strong physical pushing, struggling, or coercive blocking

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
- **娇嗔偏头**: 脑袋微微偏向一侧，眼神带点软乎乎的不情愿，嘴角抿出一点别扭弧度。
- **气声软拒绝**: 嘴唇轻轻开合，用很轻、很软、带鼻音的气声说短句，例如“我不要”，语气像撒娇式推拒，不是真正反感。
- **躲开又偷看**: 视线轻轻躲开半秒，又偷偷回到对方身上，眼底仍有亲近和安全感。
- **压住笑意**: 轻笑被压回唇边，嘴角抿住又泄出一点浅笑，身体没有后退。

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

### 娇嗔软拒绝 / Coquettish Soft Refusal

- Emotional intensity stays low, around three out of ten.
- The spoken refusal is soft and brief, often a breathy line such as `我不要`.
- Eyes and mouth contradict the literal words: gaze dodges but returns, smile is hidden but leaks out.
- The body does not truly retreat; hands, shoulders, and distance remain relaxed or intimate.
- The tone is safe, trusting, and playful, not fear, coercion, disgust, or explicit seduction.

Typical phrase:

```text
她轻轻偏头，嘴角抿出一点别扭弧度，用带鼻音的气声小声说“我不要”；视线躲开半秒又偷偷看回去，眼底仍是软的，身体没有后退，像嘴上拒绝、心里已经被哄软。
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

### Fight Prompt Length Budget

The copy-ready fight prompt must follow the duration-based ceiling: under 2000 Chinese characters for 1-15s, under 3000 Chinese characters for 16-30s. This excludes `剧情诊断`, `电影化改写策略`, and optional reference-image prompts.

Recommended budget for a 10-15s fight:

- 1300-1800 Chinese characters total.
- 2-3 shots maximum.
- 6-10 timed action beats total.
- 2-4 active actions per shot.
- One short line each for environment, camera, style, and constraints; merge repeated information into the opening summary.

Recommended budget for a 16-30s fight:

- 2000-2800 Chinese characters total.
- 3-5 shots or one readable long-take chain with internal phases.
- 10-16 timed action beats total.
- Keep choreography readable. If more action beats are required, split into consecutive clips.

Compression rules:

- State character appearance and wardrobe once; do not repeat them in every shot.
- State the location and overall light once; each shot only mentions new environmental reactions.
- Combine attack route, defense, and contact point into one concise beat.
- Do not repeat `真实重量感`, `手持摄影`, `无血腥`, or continuity constraints under every shot.
- Keep only action details that affect readability, physics, continuity, camera response, or model stability.
- If more than 10 action beats are needed, split into two consecutive prompts and choose a natural clip bridge: different angle/shot-size continuation, match-on-action, or a new completed action phase. Use the first segment's tail frame only when exact body position is essential.

Compact action beat example:

```text
-00:03：A右直拳攻向面门；B左脚后撤侧闪，以前臂向外格开拳腕，顺势横移出拳线。
```

Avoid expanding one beat into separate lines for intention, movement, contact, and result unless the action would otherwise be ambiguous.

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

### Action-Fight Camera Movement Selection System

Choose camera movement from the action's dramatic need. Do not treat the following methods as a checklist. In a 10-15s fight, normally select 2-4 principal methods and give each one a clear job: establish space, follow displacement, clarify an exchange, emphasize a decisive impact, or create a motivated transition.

| Camera method | Best use | Writing rule |
|---|---|---|
| **Tracking Follow / 跟拍跟镜** | pursuit, retreat, lateral exchange, fighters moving through a room | Follow the dominant movement direction and keep the next obstacle or destination visible; do not let the camera overtake the action without motivation. |
| **Visible Orbit / 环绕运镜** | face-off, circling footwork, power reversal, showing a 180/360-degree arena | Orbit only while both fighters remain readable and the changing background explains the rotation. Preserve the axis through a visible move; avoid full orbits during limb-heavy grappling. |
| **Rapid Dolly In / 急速推镜** | a fighter commits, a guard breaks, a decisive strike begins | Push toward the intended contact point immediately before or during one major impact, then stabilize. Do not use repeated push-ins for every hit. |
| **Rapid Dolly Out / 急速拉镜** | reveal a fall, throw, environmental landing, new threat, or spatial consequence | Pull back to create physical room and show where the body/object lands. Use before or during large movement, not after the result has become unclear. |
| **Low-Angle Upward Shot / 低角度仰拍** | forward drive, dominant stance, lift, leap, weapon rise | Keep feet or the force-generating body line visible; use briefly to magnify force without hiding contact or turning the move into a pose. |
| **Overhead / High-Angle Geography / 高空俯拍** | group fight geography, encirclement, escape path, bodies changing formation | Use as an orientation beat, not the main impact view. Show lanes, spacing, exits, and who is surrounded. |
| **Slow-Motion Tracking / 慢动作跟镜** | airborne movement, decisive dodge, weapon crossing, debris burst | Reserve for one peak beat. Track the complete motion path, then return to real time for landing, recoil, and recovery. |
| **Whip Pan / 摇镜横移** | sudden attack from the side, opponent crossing frame, thrown object, fast defensive turn | Pan along the real action direction. End on a readable subject or landing point; do not use as random blur between unrelated actions. |
| **Whip-Pan Flash Cut / 甩镜闪切** | hide a cut at the instant of a strike, accelerate a direction change, join two matching motions | Cut inside the motion blur while preserving direction, speed, body pose, weapon hand, and screen position. Use once at a major acceleration beat. |
| **Micro-Montage Inserts / 特写切镜** | fists, feet, grip, eyes, weapon edge, impact preparation | Use 2-3 very short inserts only when they clarify cause and effect. Return to a wider readable shot before the main body action. |
| **Ped Up/Down or Crane Rise/Fall / 升降运镜** | stair pursuit, jump/drop, stand-up recovery, changing vertical advantage | Move vertically with the action and reveal the new level or destination. Do not substitute a tilt when the camera itself must change height. |
| **Foreground Occlusion Wipe / 穿墙过物穿梭** | move between adjacent fight zones, disguise a cut, reveal a new attacker or room | Let a pillar, wall edge, vehicle, hanging cloth, or foreground body fully wipe the frame; emerge with matching movement direction and preserved spatial logic. |
| **Shot/Reverse Shot / 反打镜头** | clarify attack-defense alternation, reaction, feint, stare-down | Keep eyelines and screen sides stable. Change horizontal angle by at least 30 degrees within the same scene and avoid adjacent near-identical shot sizes. |
| **Rotating Pan/Orbit / 旋转摇镜** | circling duel, clinch rotation, chained attacks that revolve around one center | Let fighter rotation motivate the camera rotation. Keep a stable visual anchor in the environment so the viewer does not lose orientation. |
| **Impact Hold / 定格定镜** | one decisive non-graphic hit, block, collision, or near-miss | Use an ultra-brief impact hold, near-freeze, or speed-ramp plateau rather than a long literal freeze. Preserve recoil, sound, and immediate recovery so the strike retains physical continuity. |

#### Selection by Fight Beat

```text
空间建立：Overhead/High Angle, Visible Orbit, FLS/LS establishing shot
追逐与位移：Tracking Follow, Whip Pan, Ped/Crane movement
攻防可读：Shot/Reverse Shot, Micro-Montage Inserts, medium handheld tracking
力量升级：Rapid Dolly In, Low-Angle Upward Shot, Rotating Pan/Orbit
摔投与落点：Rapid Dolly Out, Ped Down, overhead geography
高潮命中：Slow-Motion Tracking or Impact Hold, choose one dominant emphasis
隐藏剪辑：Whip-Pan Flash Cut or Foreground Occlusion Wipe, only with matched direction/action
```

#### Combination Rules

- Tie every camera move to a verb in the choreography: pursue, evade, rotate, lift, fall, reveal, strike, recover. If the camera move has no action cause, remove it.
- Keep the action chain readable before adding impact style. Show full bodies for footwork, throws, leaps, grappling reversals, and landings; use close inserts for preparation, grip, expression, or one contact detail.
- Do not combine rapid push, whip pan, orbit, Dutch angle, slow motion, and impact hold in the same beat. Choose one primary emphasis and at most one supporting camera response.
- For edited fights, preserve the 180-degree axis, screen direction, eyelines, weapon hand, and action velocity. Use match-on-action for cuts inside a strike, dodge, fall, or weapon swing.
- For continuous long takes, use only physically connected camera paths. Foreground wipes may disguise stitching, but the resulting shot must still feel like one navigable space.
- Let impact breathe for a fraction of a beat, then show recoil, pain response, balance recovery, environmental reaction, or the next threat. Do not freeze at contact and omit the physical result.
- Use camera movement to vary rhythm: readable setup -> mobile exchange -> one emphasized peak -> stable aftermath. Continuous maximum-intensity movement weakens impact.

Useful compact phrase:

```text
运镜按动作功能分配：FLS跟拍建立追逐方向，攻防转折用反打保持轴线，摔投前Rapid Dolly Out留出落点空间，决定性命中仅使用一次短暂Impact Hold，随后立即恢复实时速度并交代后坐、喘息与环境反馈；不堆叠无动机甩镜、环绕和慢动作。
```

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

- Segment 1: pressure, first exchange, incomplete reversal, ending on danger or an unfinished action.
- Segment 2: continue the same story state from a new angle/shot size, complete the reversal, finishing impact, aftermath.

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

## Hong Kong Crime Long-Take Close-Quarters Fight

Use this for 1990s Hong Kong crime action, rain-soaked alley fights, car-side brawls, gangland chases, and brutal close-quarters 1v1 scenes where the user wants an unbroken handheld long take. Abstract the reference into transferable action design; do not depend on naming or imitating a specific living choreographer.

### Core Feel

- Style: gritty Hong Kong crime realism, wet neon, narrow alley, handheld 35mm film grain, practical tungsten/neon light, rain mist, steam, wet asphalt.
- Camera: one continuous handheld take unless the user asks for cuts; full-body readability comes first, then close body texture.
- Action: no posing, no decorative martial-arts display, no impossible fantasy movement. Favor boxing, elbows, knees, clinch, wrestling, wall/car impact, ground control, neck escape, and short-range survival movement.
- Physics: every attack needs stance, momentum, contact point, recoil, environmental reaction, and pain/breath feedback.
- Safety/taste: staged movie fight, adult performers, non-graphic injury only. Use rain/sweat/minor blood spray sparingly; no gore, no fetishized damage.

### One-Take Action Chain

Write the fight as an uninterrupted cause-and-effect chain:

```text
spatial anchor -> weapon/object threat -> evasion -> entry -> takedown/clinch -> environment impact -> ground control -> reversal/lock -> body shot -> escape -> counter elbow/knee/punch -> camera orbit/reframe -> finishing impact -> breath/aftermath close-up
```

Keep one dominant direction at a time. The camera may orbit, but the fighters' positions, distance to walls/cars/doorways, and screen direction must remain understandable.

### Useful Beat Library

- opponent grabs pipe/bottle/brick and swings horizontally
- protagonist ducks under the swing and shoots forward into a waist/body lock
- both bodies crash into a parked car, shutter door, wall, trash bins, or wet pavement
- camera stays close to torsos during the scramble, then widens just enough to keep limbs readable
- mounted position with short staged punches; defender covers, bridges, turns the hips, and reverses
- clinch against car hood or wall; knee to ribs or thigh; elbow to jaw/shoulder line
- rear headlock/neck control, followed by hand fighting, chin tuck, hip turn, and escape
- final controlled slam into a car hood, shutter, padded wall, stacked boxes, or breakaway surface
- final breath: both bodies stop for 1-2s, rain and engine metal sound continue, camera pushes to wet face close-up

### Camera and Spatial Continuity

- Start with a strong alley geography: wall on one side, parked car or shutter on the other, wet ground, exit direction, neon source.
- Use handheld lateral tracking as the fight starts; avoid random shake before impact.
- Keep both fighters' full bodies visible during throws, takedowns, and reversals.
- Go close only for grounded scrambling, clinch pressure, breath, hands fighting for grip, or facial aftermath.
- A 180-degree camera orbit is allowed inside a one-take fight only if the orbit is visible and motivated by the fighters rotating or colliding through space.
- If the camera must come very close, immediately re-open the frame before the next large body action.
- Do not hide contact with excessive blur, foreground obstruction, or chaotic whip pans.

### Environment and Sound Feedback

Bind each heavy action to visible and audible consequences:

- pipe swing cuts through rain -> water beads scatter past lens
- shoulder drive into car -> metal panel booms, rainwater jumps, alarm chirps or hood dents slightly
- body hits wet ground -> splash, clothing sticks, breath knocks out
- elbow or knee lands -> short grunt, head/torso recoil, handheld jolt
- clinch scrapes along shutter -> metal rattle
- final car-hood impact -> controlled dent, rainwater sprays, then breath and rain dominate

Use diegetic sound only: rain, footsteps splashing, metal impact, cloth friction, breath, grunts, pipe scraping, car alarm chirp, distant city hum. No background music by default.

### Prompt Template

```text
基础概括：10-15秒一镜到底港式犯罪动作长镜头，{地点与时代氛围}，两名成年角色近身缠斗。手持摄影连续跟随，全程保持空间连续性和全身动作可读性，无配乐。

动作链：
0-2s：{空间锚点}，对手从{方向}抓起{物件}横扫，攻击线指向{头部/上身非致命区域}；主角{俯身/侧闪/后撤}避开，镜头侧向跟进。
2-5s：主角压低重心切入，{抱腰/肩撞/双腿控制}，借前冲惯性把对手撞向{汽车/墙/卷帘门}，环境产生{金属声/水花/震动}。
5-8s：两人在{车旁/地面/墙边}翻滚或缠斗，主角短促控制，对手{格挡/桥翻/锁颈/反抱}完成反转，镜头贴近身体但保持肢体关系清楚。
8-12s：主角通过{手部解锁/转髋/膝撞/反肘}挣脱并反击，雨水、汗水和少量非血腥擦伤痕迹飞散；摄影机随两人旋转半圈或180度可见环绕。
12-15s：主角完成一个受控终结动作，把对手撞向{可承受表面}，环境明确变形或震动；最后留1-2秒喘息，镜头缓慢推进到雨水覆盖的面部特写。

约束：成年演员，电影特技打斗，非血腥；真实人体力学，动作链连续，没有摆拍，没有飞天或夸张武术，不遮挡关键接触点，不要肢体穿模，不要过度动态模糊，不要背景音乐和字幕。
```

### Compression Notes

For final prompts under the duration-based character ceiling, compress this pattern by keeping location and one-take structure, the strongest action beats, environment feedback for major impacts, camera continuity/readability rules, diegetic sound, and negative constraints. Cut repeated style tags first. Do not cut attack-defense causality or final breathing room.

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
- If continuing, do not default to copying the previous tail frame as the next first frame. Choose a bridge: different shot size/angle for continuous danger, match-on-action for unfinished movement, or a new 15s shot group for the next completed action phase.
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

**3. Clip bridge continuation, 5-8s**

```text
画面一：接续上一段危险状态，但不复刻上一段尾帧；开头换为中远景侧后方角度，保护者与被保护者相互靠近或并肩站立，合力御敌。无台词，仅生成打斗音效和环境音效，不配背景音乐，禁止字幕。
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

### Dialogue Timing Budget

Estimate delivery time before assigning dialogue to a shot. Count Chinese characters without punctuation as a practical approximation.

Suggested Mandarin delivery rates:

- 2-3 Chinese characters/second: whisper, grief, hesitation, restrained confession, breath-broken speech.
- 3-4 Chinese characters/second: natural dramatic conversation.
- 4-5 Chinese characters/second: urgent command, argument, panic; use sparingly because clarity and lip-sync become less stable.

Suggested English delivery rates:

- 1.5-2 words/second: whisper, emotional hesitation.
- 2-3 words/second: natural dramatic speech.
- 3-4 words/second: urgent speech; avoid long lines at this speed.

Add time beyond spoken words:

- 0.3-0.8s before a difficult line for breath, eye contact, or hesitation.
- 0.3-0.8s for a meaningful pause inside the line.
- 0.5-1.5s after the line for the listener's reaction.
- 1-2s at the end of the video for performance or editing room.

Practical formula:

```text
镜头所需时长 = 台词口播时间 + 说话前动作/停顿 + 对方反应 + 运镜完成时间
```

Examples:

```text
“我们尽力了，但她没能撑过来。”约14个汉字。
克制、缓慢通知按2.5字/秒估算，纯口播约5.5秒；若镜头只有4秒，应缩短台词或拆分反应，不应强塞。
```

```text
“所以你们只是通知我。”约10个汉字。
自然压抑语速按3字/秒约3.3秒，再留1秒沉默反应，镜头至少约4.3秒。
```

Rules:

- Do not assign two substantial lines plus a complex body action to a 2-3s shot.
- If dialogue runs long, shorten the line before speeding up delivery.
- Important lines should finish before the final 1-2s ending breath.
- Offscreen dialogue still consumes time and must be budgeted.
- Simultaneous overlapping lines should be short and intentionally motivated.

## Light and Atmosphere

Make atmosphere physical:

- Moving streetlight stripes across a face.
- Wind lifting hair, paper, grass, shirt collar, dust.
- Window reflections splitting the face.
- Hard light cutting through blinds.
- Cold interior shadow versus warm exterior light.
- Engine vibration, cloth friction, footsteps on wood, room tone, breath, sudden silence.

Prefer dynamic light over static adjectives. Say what the light does to the face, object, or space.

## Output Modes

Select the lightest mode that satisfies the user's workflow.

### 精简模式 / Compact Mode

Trigger examples: `直接给提示词`, `不要分析`, `只要成品`, `精简版`.

Output:

```text
【最终视频提示词】
...
```

Rules:

- No visible diagnosis or strategy.
- Omit references unless requested or essential.
- Keep the final prompt compact and copy-ready.
- Still run all diagnosis, timing, continuity, compression, and safety checks internally.

### 打磨模式 / Workshop Mode

Default for ordinary requests and iterative revision.

Output:

```text
【剧情诊断】
【电影化改写策略】
【建议先生成的参考图】
【最终视频提示词】
```

Rules:

- Keep diagnosis and strategy concise and correctable.
- Output only references that improve control.
- The duration-based character ceiling applies only to the final video prompt.

### 连续短片模式 / Continuous Short-Film Mode

Use for long-story splits, repeated `继续`, multi-part episodes, or projects requiring stable recurring characters and locations.

Output:

```text
【连续性摘要】
角色档案：
场景档案：
上一段结尾剧情状态：
本段衔接方式：
本段推进：

【参考资产】
沿用：
新增：
更新状态：

【本段最终视频提示词】
...

【下一段衔接锚点】
结尾剧情状态：
可衔接动作/情绪/道具：
人物/道具状态：
```

Rules:

- Keep canonical character and scene records stable across segments.
- Each segment advances one main event or emotional turn.
- Do not reuse the previous tail frame by default. Preserve story state, identity, space, props, and emotional residue; choose the bridge that best fits the next segment.
- Add reference prompts only for new visual anchors or meaningful state updates.
- Each segment remains under 30s and its final prompt under the duration-based character ceiling.

## Structure Selection

Choose structure before writing shot details. Always state the chosen structure in the diagnosis, and explain the reason in one sentence. If more than one structure fits, choose one primary structure and one secondary support.

### Structure Selection Table

| Structure | Use When | Best For | Avoid When | Prompt Strategy |
|---|---|---|---|---|
| **单场景一镜到底 / Single Take** | One space, one continuous emotional shift, few actions, no major time jump | restrained grief, confrontation pause, ritual, waiting, subtle intimacy | many locations, action complexity, multiple plot turns | Use the Ordinary Drama One-Take Blocking System: one camera path, start frame, blocking shift, motivated focus change, foreground depth, sound continuity, held ending |
| **单场景连续剪辑 / Multi-Shot Sequence** | One location but several physical beats or reaction angles are needed | kitchen tension, hospital corridor, car interior conflict, interrogation | very abstract memory, large time span | Use 3-5 shots: establish space, key object/action, face reaction, ending breath |
| **跳剪压缩 / Jump Cuts** | Time needs compression while staying in one emotional thread | preparation, decision, panic escalation, ritual, product/person process | scene requires smooth emotional realism | Use repeated visual anchor; each cut advances state clearly |
| **蒙太奇 / Montage** | Memory, dream, symbolic contrast, parallel images, theme rather than linear action | childhood recall, grief objects, identity transformation, longing | direct dialogue scene, precise physical action | Use sound or object as transition anchor; keep fragments sensory and partial |
| **连续动作剪辑 / Continuous Action Editing** | Character moves through space under pressure | chase, escape, crossing rooms, storm/rain movement | tiny emotional beats, complex multi-person combat without reference | Keep direction consistent; define start/end spatial goal; limit actions |
| **格斗动作编排 / Fight Choreography** | 1v1 or limited multi-person staged combat with clear attack-defense beats | boxing, close combat, controlled stunt throw, wuxia exchange, underground ring | many attackers, unclear character references, gore, lethal injury emphasis | Define roles, attack line, defense, counter, footwork, contact point, camera response, safety constraints |
| **多人对话交叉剪辑 / Dialogue Cross-Cutting** | 2-4 people in one scene, power shifts through speech and silence | family dinner, office confrontation, breakup, negotiation | no meaningful dialogue or no relationship tension | Define seating/standing positions, who holds power, key lines, reaction shots |
| **长特写微表情 / Close-Up Micro-Expression** | Emotion is carried mainly by face/head with minimal action | shock, suppressed crying, shame, hidden love, inner collapse | plot needs many events or spatial movement | Use ECU/CU, stable or slow push, timed facial-muscle progression |
| **产品/人物质感片 / Product-Person Texture Film** | Product, place, or persona matters as much as plot | car, watch, founder, artist, venue, premium object | story requires many dramatic turns | Use tactile details, material, light, sound, controlled gesture, brand-like restraint |
| **大场面压缩 / Large-Scene Compression** | Crowd, disaster, ceremony, battlefield, launch, courtroom, banquet | chaos with one human anchor, public pressure, group reaction | no clear protagonist or visual anchor | Pick one visual anchor; show crowd as pressure; use 4-5 clear nodes |
| **长剧情拆分 / Sequential Prompt Split** | Playable content exceeds 30s or final prompt would exceed the duration-based character ceiling, even if the user's text is short | reunion, investigation, travel, multi-stage emotional arc, multiple actions or location changes | one small moment already fits under 30s | Split by emotional turning points; make each segment a complete 15-30s mini-arc and define a bridge type for the next segment |
| **剧情续写 / Continuation Segment** | User approves a segment and asks to continue | short-film sequences, clip bridges, multi-part emotional arcs | no prior segment context exists | Continue from previous story state, preserve identity/scene/props, choose a bridge type, add only one new event |
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
- If the playable content cannot breathe within 30s, choose `长剧情拆分` even when the user's written description is short.
- If the user asks to continue from an approved prompt, choose `剧情续写`.

### Hybrid Structures

Use hybrid labels when useful, but do not overcomplicate the final prompt.

Examples:

- `主结构：多人对话交叉剪辑；辅助：长特写微表情`
- `主结构：连续动作剪辑；辅助：主观镜头`
- `主结构：格斗动作编排；辅助：手持近身冲击感`
- `主结构：蒙太奇；辅助：匹配剪辑`
- `主结构：大场面压缩；辅助：单人物视觉锚点`
- `主结构：剧情续写；辅助：动作中衔接`

### Structure Failure Warnings

- Do not choose single take just because it sounds cinematic; use it only when the action can physically unfold in one continuous space.
- Do not choose montage when the user needs a clear cause-and-effect event.
- Do not put more than one major location change into a short single-take prompt.
- Do not write large crowd scenes without a visual anchor.
- Do not write long dialogue at the final second. Give reaction and aftertaste.

## Director-Level Shot Continuity Rules

Use these rules when writing multi-shot prompts. They make the prompt feel directed and editable, not just visually descriptive.

### Generation Execution Stability

Use these rules for the copy-ready final prompt, especially when the scene has reference images/videos, dialogue, action, one-take blocking, continuation, or important props.

**First-frame reconstructability**

The opening of the final prompt should let the model rebuild the first frame without hidden memory. Include the visible subject, start posture/action state, screen position and depth, facing direction, gaze, held or contacted prop, shot size, camera angle/height/axis, and main motivated light source when it affects composition. The first frame should not be a vague setup unless the story deliberately reveals the subject later.

The visible subject does not have to be a person. It can be an empty location, key prop, vehicle, screen, building, landscape, or aftermath state. If the first frame is empty or object-led, define location layout, foreground/midground/background, key object position/state, weather or environmental motion, sound cue, shot size, camera angle/height/axis, and motivated light source when relevant.

**One shot, one core action, one core camera behavior**

Each shot should have one main action path and one main camera behavior. A shot can contain small supporting reactions, but the viewer should know which action the model must prioritize and what the camera is doing. If a continuous shot needs multiple movement phases, serialize them with clear settle points. If the action and camera compete, simplify the camera or split the shot.

**Ending-state lock when needed**

Do not add a separate ending field by default. But when a prompt will be continued, split, repaired, generated from first/last frames, or depends on a product/prop/action endpoint, state the final visible condition inside the last shot: character pose, gaze, body contact, prop location/state, focus, composition, and emotional residue. A completed action becomes a visible final state, not something to replay in the next clip.

The ending state may also be empty or object-led. In that case, lock what remains on screen: the empty space, door/window/light state, fallen or placed prop, screen state, vehicle position, weather/sound continuation, focus, and composition.

**Story-critical prop state**

For phones, letters, cups, rings, weapons, reports, U-disks, photos, keys, documents, and other plot-changing objects, describe physical state with the same care as body action:

- who holds or touches it
- which hand or support point is used
- grip/pressure/orientation
- contact with body, table, floor, pocket, bag, door, another person, or device
- visible change during the shot
- final visible location and state

If a prop changes owner, position, orientation, damage, wetness, light state, screen state, or readability, show the action that changes it.

**No optional branches in final prompts**

The final prompt should not contain unresolved options such as `或`, `或者`, `A/B`, `二选一`, `可选`, `可以...也可以...`, or `任选`. Make one director choice before delivery. Variants are allowed only when the user explicitly asks for multiple versions.

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

When cutting between different camera angles within the same scene, and especially between shots of the same subject or same interaction, change the camera's horizontal angle by at least 30 degrees. This prevents awkward jump cuts and gives the edit a real perspective shift.

This rule applies only inside the same scene or continuous spatial relationship. When cutting to a new scene, new location, new time, or a clearly different spatial setup, do not force a 30-degree angle change; prioritize the new scene's geography, mood, and opening composition.

Examples:

- Shot 1: front-left 3/4 angle.
- Shot 2: side angle over the other character's shoulder, at least 30 degrees away.
- Shot 3: reverse angle or object insert.

Do not write repeated same-angle close-ups inside the same scene unless the scene intentionally uses a locked-off long take.

### 180-Degree Axis and Eyeline

Establish an imaginary axis through the interacting characters or along the main direction of movement. Keep the camera on one side of that axis so screen positions and gaze directions remain understandable.

For two-person dialogue:

- If A is established on screen-left looking right, keep A looking right in later close-ups.
- B should remain on screen-right looking left.
- Over-the-shoulder reverse shots must preserve these eyelines.

Cross the axis only when motivated by one of these methods:

- show the camera physically moving across the axis
- use a neutral shot directly on the axis
- insert a clear re-establishing wide shot after the crossing
- let a character visibly move across the axis and create a new spatial relationship

Do not silently flip character positions between adjacent shots.

### Screen Direction and Entry/Exit

- A character exiting frame-right should normally enter the next connected space from frame-left, continuing the same travel direction.
- In a chase, maintain pursuer and target screen direction unless the turn is shown.
- In a fight, keep A/B screen positions stable until a visible pivot, pass, throw, or camera move changes them.
- Vehicles, running characters, thrown objects, and gaze direction should preserve momentum across cuts.

### Handedness, Props, Costume, and Body State

Track continuity details across shots:

- which hand holds the phone, cup, letter, sword, gun, ring, or bag
- where the prop is placed after release
- whether clothing is buttoned, wet, torn, dusty, or displaced
- hair position, makeup tears, sweat, blood-free injury state, and visible marks
- which cheek has a tear track or which sleeve is damaged
- whether a character is standing, kneeling, seated, leaning, or facing a particular direction

If a continuity state changes, show the action that changes it.

### Spatial Continuity Record

For dialogue, action, continuation, or multi-part scenes, internally track:

```text
人物A：画面位置 / 朝向 / 持物手 / 姿态
人物B：画面位置 / 朝向 / 持物手 / 姿态
关键道具：位置 / 状态
主光源：方向 / 色温
出入口：位置
运动方向：左至右 / 右至左 / 向镜头 / 远离镜头
```

Do not print this record unless the user asks for a continuity sheet, but use it when writing the prompt.

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
- a held reaction, sound cue, prop state, or unfinished action that can bridge into the next segment

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

## Novel Excerpt to Cinematic Prompt

Use this pattern when the user provides a novel paragraph, web-fiction excerpt, prose scene, or heavily internalized narrative.

### Adaptation Principle

Do not translate the prose sentence by sentence. A video prompt should preserve the dramatic intention and emotional turn, then rebuild it as a short playable scene.

Priority order:

1. Preserve the core relationship and conflict.
2. Preserve the visible emotional turn.
3. Preserve the key spoken line if it drives the plot.
4. Preserve the most cinematic object, gesture, or environment motif.
5. Compress or omit backstory, explanation, repeated description, and decorative metaphor.

### Novel Text-Length Tiers

Use length tiers before deciding whether to generate a final video prompt.

- Under roughly 1500 Chinese characters: direct adaptation is usually allowed. Still select one clear event or emotional turn, then generate one 6-30s prompt based on playable content.
- Roughly 1500-3000 Chinese characters: do not adapt the whole passage. First diagnose the passage, identify the strongest filmable scene, state what will be covered and what will become context or later material, then generate only one prompt for that selected scene.
- Over roughly 3000 Chinese characters or a full chapter: do not generate final prompts immediately. First judge or ask whether the user wants `片段拆选` or `连续短片结构`.
  - If the user wants a strong single video moment, test case, highlight, or does not specify full coverage, output a `影视化片段拆选表`: list 3-6 candidate scenes with emotional core, visual hook, suggested duration, and reason to adapt. This table does not need to cover every plot beat.
  - If the user asks for complete adaptation, full coverage, a short film, a mini-drama, serialized generation, or turning the whole novel excerpt into videos, output a `连续短片总结构表`: cover the main story spine in order, preserve cause and effect between segments, note recurring characters/scenes/props, and do not output final video prompts yet.

Do not mechanically split long prose into one prompt per 30 seconds. That creates bloated, low-control output. Use scene selection or a continuous structure table first, and enter detailed multi-segment prompt generation only after the user confirms a segment, episode range, or full continuous-short-film plan.

### Long Novel Entry Decision

When a long novel input arrives, decide the entry path before writing final prompts:

```text
如果用户想要单条爆点视频：输出【影视化片段拆选表】
如果用户想要完整改写/覆盖全文/短片/短剧/连续视频：输出【连续短片总结构表】
如果用户意图不明确：先简短说明两种选择，并默认给出片段拆选表，或询问用户要哪一种
```

`影视化片段拆选表` is for choosing the strongest filmable moments. It is selective and does not guarantee full coverage.

`连续短片总结构表` is for full-story adaptation. It should include:

- segment number and suggested duration
- covered plot beat
- emotional turn
- key characters on screen
- location and continuity state
- key props or new visual references needed
- bridge purpose for the next segment

After outputting a continuous short-film structure table, wait for the user to choose a segment or ask to start generating prompts. Do not output all final prompts in the same response unless the user explicitly requests it and the scope is small enough.

### Diagnosis Fields for Novel Inputs

Use these fields in workshop mode when they help the user see the adaptation decision:

```text
原文核心冲突：
可视化主事件：
不可直接拍摄的心理描写：
建议保留：
建议压缩或外化：
本条提示词覆盖范围：
```

Keep this section concise. It is for adaptation clarity, not literary analysis.

### Prose-to-Image Translation Map

- Inner monologue -> eyes avoiding contact, breath change, hand tension, delayed response, repeated gesture, brief voiceover only when necessary.
- Backstory -> one prop, photo, scar, letter, phone screen, room detail, costume state, or a short line.
- Metaphor -> light, weather, reflection, shadow, sound, physical motif, or actor behavior.
- Authorial explanation -> blocking, distance between characters, who initiates/retreats, who occupies power position in frame.
- Long emotional paragraph -> 3-5 micro-expression beats with time marks.
- Memory or flashback -> object insert, reflection, sound bridge, short montage, or split into another segment if important.
- Worldbuilding -> one clear establishing shot or scene reference prompt, not a full encyclopedia.

### Compression Rules for Novel Inputs

- If one excerpt contains setup, reveal, argument, collapse, and aftermath, choose only the turns that can naturally play within one 30s prompt and recommend splitting the rest.
- For 1500-3000 character excerpts, state the selected scene explicitly before the final prompt. Treat all other material as context unless the user asks for a full sequence.
- For 3000+ character excerpts, output a scene-selection list first. Do not output a long chain of final prompts unless requested.
- If the original has many adjectives, keep only those that change lighting, costume, texture, performance, or mood.
- If the original contains multiple named characters, keep only the characters who affect this moment on screen.
- If the original dialogue is too long, rewrite it into 1-2 short playable lines while preserving meaning and emotional subtext.
- If the original depends on private thought, create an external action anchor: cup, sleeve, ring, phone, letter, door, blade, window, cigarette, bed sheet, scarf, or another story-specific object.

### Final Prompt Requirements for Novel Inputs

- The final prompt must read like a shootable scene, not a synopsis.
- Include concrete time allocation, physical action, camera behavior, performance detail, sound, and ending breath.
- Do not include literary commentary such as "象征着", "暗示了", or "表现了" unless immediately tied to a visible action.
- When preserving prose language as voiceover, keep it short and timed; avoid turning the whole scene into narration.
- If the scene is part of a longer chapter, mention what this prompt covers and what should continue in later segments.

### Continuous Novel Adaptation Continuity

When adapting a novel into multiple consecutive video prompts, keep a compact continuity record and avoid redundant restatement.

- If two consecutive segments use the same characters, same costumes, same location, same lighting, and same key props, do not repeat the full character and scene descriptions. Use phrases such as `接续上一段剧情状态`, `沿用苏敏的同一服装与疲惫妆容`, or `保持同一书房夜晚冷暖光`.
- Still repeat the minimum anchors needed for model stability: character name, approximate age, current emotional residue, current costume state, location, and the key prop currently in hand or in frame.
- If a new character appears, add a concise character description and optional new character reference prompt.
- If the story enters a new location, add a concise scene layout and optional clean scene plate prompt.
- If a character changes clothing, makeup, injury, wet/dusty state, or hairstyle, describe the change and treat it as the new continuity state.
- If a new key prop becomes narratively important, describe its appearance, initial position, and who holds or moves it. Track where it ends after the segment.
- If the only change is emotional progression, do not regenerate identity or scene descriptions; describe the emotional residue from the previous segment and the new emotional turn.
- Use the previous segment's story state as the continuity anchor between adjacent prompts. A previous tail frame may be used as a reference, but it should not be treated as the required first frame of the next video.

## Continuation and Clip-Bridging Workflow

Use when the user says `继续`, `接着往下写`, `下一段`, `下一镜`, `延续上一条`, or when a long story is split into adjacent clips.

### Continuation Principles

- Continue from the previous story state, not necessarily from the previous final image.
- Keep character identity, age, hairstyle, clothing, makeup, injury state, and emotional residue consistent.
- Keep setting, lighting, weather, time of day, color palette, camera texture, and sound bed consistent unless the story intentionally changes.
- Keep key props consistent in design, position, and narrative meaning.
- Progress emotion instead of replaying it.
- Add only one main new event or emotional turn per short segment; a 16-30s segment may include a fuller setup-turn-aftermath arc if it stays playable.
- Let each segment feel like a complete small dramatic unit. Do not force a long-take continuation across clips if a shot-group structure is more natural.
- Leave the ending as a useful next bridge: a held reaction, an unfinished action, a prop state, a sound cue, or a completed mini-arc that can lead into the next beat.

### Clip Bridge Types

Choose one bridge before writing the next prompt:

1. **Continuous Drama Bridge / 换景别换角度接续**: use when the previous ending must continue immediately, but the next video should not copy the same frame. Start the next clip from the same story moment with a different shot size and camera angle, such as CU -> WS, MS -> BCU, over-shoulder -> reverse angle, or side angle -> frontal angle. Preserve axis, eyeline, body direction, prop state, and emotional residue.
2. **Match-on-Action Bridge / 动作中衔接**: use when the previous clip ends on an unfinished action. End segment 1 as the hand begins to open the door, body starts to turn, sword begins to draw, person starts to fall, lips begin to speak, or fist begins to swing; start segment 2 from a new angle/shot size continuing the same action, not restarting it.
3. **Shot-Group Bridge / 分镜组衔接**: use when each clip is a complete small scene or emotional beat. Segment 2 does not need to start from segment 1's tail frame. It should start with a strong new shot that belongs to the next mini-arc while preserving character, scene, prop, costume, light, sound, and emotional continuity.

Use the previous tail frame only when exact body position, blocking, injury/damage state, or object position is critical. Otherwise, treat it as one reference asset among others, not as a required first-frame instruction.

### Continuation Diagnosis

Use this compact form:

```text
【接续判断】
上一段结尾状态：...
下一段情绪推进：...
衔接方式：换景别换角度接续 / 动作中衔接 / 分镜组衔接
连续性注意：人物服装、场景光线、关键道具、动作方向、情绪残留需要沿用...
```

### Reference Image Rules for Continuation

- If the next segment uses the same character, same scene, and same key props, say: `沿用已有角色/场景/道具参考，不新增参考图。`
- If exact continuity is needed, optionally add: `可参考上一段尾帧的身体姿态/道具位置，但下一段开头不必复刻同一帧。`
- If a new character appears, add `新增人物参考图`.
- If a new location appears, add `新增场景参考图`.
- If a new key prop appears, add `新增关键道具参考图`.
- If a costume, injury, makeup, or emotional state visibly changes and must remain stable later, add an updated character reference.

### Continuation Opening Phrases

Use clear continuity phrases in the final prompt:

```text
接续上一段剧情状态，但开头换为新的景别与角度：...
保持同一人物、同一服装、同一场景光线和同一道具位置。
上一段结尾的情绪不重置，继续从...推进到...
```

```text
动作中衔接：上一段结尾人物刚开始...，本段开头用...景别从...角度继续同一动作，动作不重来，只完成未做完的部分。
```

```text
分镜组衔接：本段是下一组15秒小剧情，不复刻上一段尾帧；沿用人物、场景、道具和情绪余波，从新的有效开场镜头进入下一事件。
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
- Adding more plot events than the selected duration can naturally play.
- Copying the previous tail frame as the next first frame by habit, especially when a new angle, match-on-action, or complete shot-group opening would be smoother.
- Starting with a generic establishing shot that ignores the previous emotional or action state.

## Prompt Compression

Final prompts should be direct and proportionate to scene complexity. The character ceiling is duration-based and is not a target. It applies only to the copy-ready final prompt, not to the diagnosis or strategy sections in workshop mode.

Length targets:

- 500-800 Chinese characters: simple one-person, one-action, one-emotion scenes.
- 800-1300 Chinese characters: default range for most 8-15s cinematic prompts.
- 1300-2000 Chinese characters: complex 10-15s scenes such as multi-person dialogue, large-scene compression, montage, long-story splits, or spatial action.
- 2000-3000 Chinese characters: only for 16-30s prompts with longer dialogue, multi-shot progression, complete emotional curves, or complex blocking.

If the prompt exceeds 1300 characters for <=15s or 2000 characters for 16-30s, each extra detail must improve generation stability, emotional clarity, spatial continuity, or failure prevention. If not, cut it.

- Do not include empty boilerplate such as `视频模型：通用 AI 视频模型`. If no model is specified, omit it.
- Put duration and structure into the first summary line.
- Merge repeated labels.
- Keep only the strongest sensory details.
- Remove generic praise words like "高级", "震撼", "大片感" unless replaced by concrete light, motion, sound, or performance.
- If more detail is required, split into multiple prompts instead of overloading one.

### Automatic Compression Ladder

When a final prompt is too long, compress in this order. Preserve story causality, action clarity, dialogue, continuity, and ending breath as long as possible.

1. Remove repeated style adjectives and duplicate quality terms.
2. Merge global setting, lighting, sound, and continuity details into the opening summary.
3. Delete decorative details that do not change action, emotion, composition, or generation stability.
4. Combine adjacent micro-expression beats that express the same emotional change.
5. Combine attack, defense, contact point, and result into one concise action beat.
6. Shorten dialogue while preserving the plot-changing meaning.
7. Reduce insert shots and secondary crowd/environment reactions.
8. Shorten negative constraints to the scene-specific minimum.
9. Reduce shot count or action beat count.
10. If the scene still cannot fit under the duration-based ceiling or 30 seconds, split it at an emotional/action turning point.

Never remove first:

- the core plot turn
- key spoken information
- spatial direction and continuity anchors
- attack-defense causality in fight scenes
- the emotional reaction after the turning point
- the final 1-2s breathing room

Compressed formatting rules:

- Prefer semicolon-separated action chains over repeated labels.
- State lens/camera only when it changes or materially affects the shot.
- Do not repeat `无配乐、无字幕、角色一致` under every shot; place them once in the summary or final constraints.
- Replace long literary metaphors with visible behavior.

### Compression Audit

After compression, verify:

- no missing cause-and-effect step
- dialogue still fits its time
- character/prop positions remain clear
- ending breath remains
- final prompt stays readable rather than becoming telegraphic fragments

## Character Consistency Bible

Use for recurring characters, reference-image workflows, long-story splits, and continuation. Keep one canonical profile per character and derive all image/video prompts from it.

### Canonical Character Record

```text
角色ID/姓名：
身份与时代：
成年年龄：
身高与体型：
脸型与骨相：
眼睛/眉毛/鼻唇特征：
肤色与皮肤质感：
发型/发色/发饰：
基础妆容：
主服装与材质：
鞋履/配饰：
习惯动作或姿态：
声音基线：
性格与情绪基线：
不可变化项：
可随剧情变化项：汗、泪、灰尘、伤痕、衣物状态等
```

Rules:

- Keep identity traits stable; do not rewrite facial features with new synonyms that may drift the character.
- Separate permanent traits from temporary state.
- Use adult ages explicitly when romance, intimacy, combat, or nightlife is involved.
- Keep one primary costume per continuous scene. Show any costume change on screen or state a time/location transition.
- Track visible temporary state: wet hair, loosened hairpin, tear track, dusty sleeve, torn cuff, bruising, missing accessory.
- In continuation, repeat only the identity anchors needed by the model, not the entire bible.

### Multi-Character Relationship Record

```text
人物关系：
身高/体型对比：
权力关系：
彼此称呼：
基础距离感：
谁主动/谁回避：
对视与触碰边界：
当前未解决冲突：
```

Use this to keep dialogue, blocking, intimacy, and confrontation consistent.

## Scene Spatial Continuity Bible

Use for multi-shot dialogue, action, continuation, and any location revisited across clips.

### Canonical Scene Record

```text
场景ID/地点：
时代与时间：
天气：
空间形状与尺度：
前景：
中景：
背景：
门窗/出入口位置：
关键家具/障碍物：
关键道具初始位置：
主光源方向/色温：
辅助光与实景光源：
环境声床：
主运动轴线：
安全活动区/动作路径：
不可变化项：
可变化项：破损、烟尘、积水、灯光状态等
```

### Per-Shot Continuity Delta

Do not rewrite the whole scene for every shot. Track only changes:

```text
镜头前状态：人物与道具位置
本镜头动作：谁移动/拿起/放下/破坏什么
镜头后状态：新的位置、朝向、持物手、物体状态
```

Rules:

- A prop remains where it was placed until a visible action moves it.
- Doors, windows, lights, chairs, vehicles, and breakable objects keep state across cuts.
- Damage accumulates; broken glass, spilled water, dust, torn clothing, and extinguished lights do not reset.
- For continuation, the previous ending defines story state and continuity facts, not necessarily the exact first frame of the next segment. The next segment may begin with a new angle/shot size, a match-on-action continuation, or a new shot group.
- If moving into a new room or zone, show or clearly motivate the spatial transition.

## Visual Reference Image Prompt Patterns

Use these optional text-to-image prompts as visual anchors before video generation. They are not the final video prompt. Keep them consistent with the final prompt. The user may generate these references first for more control, or skip them and generate video directly.

Reference prompts should be complete enough to generate usable production references, not vague mood labels. Match the current segment's story state: costume, hair, dirt, wetness, injury, makeup, emotional baseline, prop ownership, light, weather, and setting should fit what is happening in that video segment. Do not reuse a generic character portrait if the character is currently running, grieving, injured, soaked, disguised, transformed, or in a different costume.

### Reference Prompt Completeness Standard

Use this standard whenever reference prompts are output:

- **Character reference**: identity/role, age range, ethnicity/era when relevant, face shape and temperament, hairstyle, body type or posture, clothing and costume state, visible dirt/wetness/injury/makeup, emotional baseline, shot size, background/light, film texture, and constraints such as non-fashion, non-glamour, non-monsterized, natural performance.
- **Single-character isolation**: a character reference for one person must describe only that person. Do not include other visible characters, relationship blocking, another person's hands/shoulders, hugging, holding, protecting, chasing, fighting, or looking at another named person. These details can cause image generation to create extra inconsistent characters.
- **Scene reference**: exact location type, spatial layout, foreground/midground/background, entrances/exits, action path, obstacles, key furniture/vehicles/architecture, practical light source and color mood, materials, weather/atmosphere, era, and whether it should be `无人物`.
- **Key prop/product reference**: object type, era, material, color, scale, wear marks, story-specific identifiers, current state, owner/placement if important, light/background, and detail clarity.
- **Relationship/two-shot reference**: both identities, screen-left/screen-right positions, height/distance, eye lines, body tension, costume state, shared environment, and power relationship.

Keep references complete but purposeful. Do not output long inventories of irrelevant fashion details, room objects, or texture adjectives that the current video will never use.

### Reference Output Decision Strategy

Choose references by the production problem being solved:

| Need | Recommended Reference | Notes |
|---|---|---|
| Stable single character identity | Character identity reference | One visible person only; neutral or current emotional baseline, clear face/hair/costume |
| Two-character height, distance, or chemistry | Relationship/two-shot reference | Use only when blocking or physical relationship matters |
| Stable room/location layout | Clean scene plate | No people; show entrances, depth, light sources, action path |
| Story-critical object/product | Key prop/product reference | Only if its design must remain stable or readable |
| Exact opening composition | First-frame reference | Match the first shot's framing and initial body state |
| Continuation between clips | Existing references + optional previous tail frame | Use tail frame only when exact posture, blocking, prop position, or damage state matters |
| New character in existing scene | New character reference only | Reuse existing scene references and continuity state |
| New location in continuation | New clean scene plate | Add only when the story actually enters the new location |

Priority order:

1. Character identity reference, when faces must remain stable.
2. Clean scene plate, when spatial layout matters.
3. Existing continuity state from previous segment, when continuing.
4. Previous tail frame, only when exact body/prop/spatial state matters.
5. Relationship/two-shot reference, when blocking/chemistry matters.
6. Key prop/product reference, only when central.

Do not provide redundant references. A simple face close-up usually needs only one character reference. A complex period dialogue may need two separate character references plus one clean scene plate. Add a relationship/two-shot reference only when shared blocking or chemistry must be controlled.

### First-Frame vs Identity Reference

- Identity reference: neutral or baseline expression, readable face/hair/costume; used to preserve who the character is.
- First-frame reference: exact pose, framing, gaze, prop position, and scene state at video start; used to control how the shot begins.
- Do not confuse them. A stylized portrait may preserve identity but be a poor first-frame reference.

### Relationship / Two-Shot Reference

Use when the video depends on height difference, seating positions, intimate distance, confrontation geometry, or who occupies visual power.

Include:

- both adult characters' identity anchors
- screen-left/screen-right positions
- body distance and eyelines
- costume and height/体型 contrast
- scene light and camera height
- no complex action; this is a blocking reference

Do not use a relationship/two-shot reference as a substitute for identity references when each character needs stable faces. Generate individual character references first, then a two-shot reference only if the scene needs relationship geometry.

### Character Reference

Purpose: stabilize identity, age, temperament, costume, and facial baseline.

Include identity/role, age range, ethnicity/era if relevant, face impression, hair, body type/posture, clothing, current costume state, visible dirt/wetness/injury/makeup when relevant, emotional baseline, shot size, lighting/background, film texture, and color palette.

Single-character rule:

- Describe only this one person.
- Do not mention other characters by role or name, such as daughter, mother, father, lover, enemy, police, doctor, crowd, corpse group, or partner.
- Do not describe interaction with another person, such as holding a child, protecting someone, hugging, kissing, grabbing, fighting, being chased by a visible person, or looking at a named person.
- If the character's emotional baseline is relational, translate it into that person's solo body evidence. For example, write `protective tension in her shoulders and alert eyes`, not `protecting her daughter`.
- If the video requires multiple people in one still image, use `Relationship / Two-Shot Reference` instead of a single-character reference.

Template:

```text
人物参考图：单人角色图，只出现{身份/角色}一人，{年龄范围/民族或时代}，{脸型与气质}，{发型与身体姿态}，{服装与当前状态：干净/破损/湿透/沾灰/血迹但不血腥/妆容变化}，{情绪基线与眼神状态，用单人可见表演表达}，{镜头距离}，{光线与背景}，真实电影质感，低饱和色调，细腻自然皮肤纹理，非写真摆拍，非时尚大片，表演自然，不出现其他人物。
```

Example:

```text
人物参考图：中国古风女子，二十七岁左右，清瘦克制，鹅蛋脸，眉眼柔和但带疲惫感，黑发盘成低髻，素雅青灰色宫装，少量银色发簪，表情平静但眼眶微湿，头部特写，烛光侧照，深色宫殿背景，真实古装电影质感，低饱和色调。
```

### Scene Reference

Purpose: stabilize layout, light source, materials, and action space.

Include location, spatial layout, foreground/midground/background, entrances/exits, light source, color temperature, key objects, usable action path, obstacles, atmosphere/weather, era, and materials. Use `无人物` when the scene reference should be clean.

Template:

```text
场景参考图：{地点与时代/类型}，{空间结构与镜头方向}，前景{...}，中景{...}，背景{...}，入口/出口{...}，可行动线{...}，障碍物/关键物件{...}，{主要光源与色调}，{天气/烟尘/雾气/材质与氛围}，真实电影场景质感，空间纵深清晰，无人物。
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
关键道具参考图：{道具名称与用途}，{年代/材质/颜色/尺寸}，{磨损、污渍、破损或使用痕迹}，{与剧情有关的标记或可读特征}，{当前状态与摆放位置/持有人}，{光线与背景}，真实电影道具质感，微距或近景，细节清晰。
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
- In compact mode, omit reference prompts unless explicitly requested or essential for control.
- In workshop mode, output only the recommended references and state that they are optional.
- In continuous-short-film mode, maintain references as a reusable asset list and mark each as `沿用`, `新增`, or `更新状态`.

### Continuation References

- For continuation, reuse existing character/scene/prop references and previous continuity facts by default.
- Add new reference prompts only for new visual anchors.
- If using a previous tail frame, treat it as optional state guidance, not a required first frame. The scene reference can be omitted unless the camera moves into a new space.
- If a new character enters an existing scene, provide only the new character reference and state that the existing scene reference remains unchanged.
- If a character's visible state changes in a way the next clip must preserve, output an updated character reference with the new clothing, hair, dirt, wetness, injury, makeup, carried prop, and emotional baseline.
- If the same location changes materially, output an updated scene reference only for meaningful changes such as new damage, smoke, rain, fire, darkness, blocked exits, moved vehicles, broken furniture, or changed light source.

### Reference Consistency Check

Before finalizing, ensure reference prompts and video prompt share:

- same character age, clothing, hairstyle, and emotional baseline
- same setting, era, color palette, and lighting
- same key prop design
- same current-state details: dust, wetness, injury, makeup, costume damage, carried objects, scene damage, weather, and light state when relevant
- no contradiction between still-image pose and video action.
- single-character references contain exactly one visible person and do not smuggle in other characters through relationship wording or interaction actions.
- relationship/two-shot references are used only when multiple people intentionally need to appear together.

## Negative Constraints

Use negative constraints only when they prevent likely generation failure:

Write the desired content and action path positively first. Negative constraints are not the main steering wheel; they are a small guardrail after the positive target is clear. If a model does not handle negative language well, replace outcome-critical negatives with positive instructions.

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
- The final prompt is near the duration-based character ceiling.

Minimum fallback:

```text
负面约束：不要字幕水印，不要背景音乐，不要脸部畸变，不要风格跑偏。
```

## Quality Self-Check

Run this silently before giving the final answer. Do not print it unless the user asks for a critique, debug pass, or improvement report.

### Story and Structure

- Does the diagnosis name the emotional core and visual core?
- Is the chosen structure explicitly stated and justified?
- Does the duration fit the content instead of defaulting to 30s?
- Was duration/splitting judged by playable content rather than source text length alone, including event count, dialogue time, actions, emotional reactions, scene changes, camera moves, and ending breath?
- If the story exceeds 30s or the duration-based character ceiling, does the answer recommend splitting and clearly state what this prompt covers?
- If this is a split prompt, has the bridge type been chosen: different shot size/angle continuation, match-on-action, or complete shot-group continuation?

### Prompt Usability

- Is the final prompt copy-ready and under the correct duration-based character ceiling when possible?
- Is the chosen output mode appropriate to the user's request: compact, workshop, or continuous-short-film?
- If the draft was too long, was the automatic compression ladder applied before splitting?
- For fight prompts, has the copy-ready final prompt stayed within the duration-based ceiling, with action beats limited to what the selected duration can clearly show?
- Is there no empty boilerplate such as `视频模型：通用 AI 视频模型`?
- Does the first summary line include duration and structure?
- Are technical terms useful rather than decorative?
- Can the first frame be reconstructed from the final prompt? If character-led, are visible subject, start state, screen position/depth, facing direction, gaze, prop contact, shot size, camera angle/axis, and motivated light source clear? If empty or object-led, are location layout, foreground/midground/background, key object/environment state, sound cue, shot size, camera angle/axis, and motivated light source clear?
- Does each shot have one core action path and one core camera behavior, with multiple camera phases serialized only when necessary?
- If the prompt requires continuation, split clips, first/last frames, complex blocking, repair, or a product/prop endpoint, is the final visible ending state clearly locked inside the last shot, whether it is character-led, empty, or object-led?
- Are story-critical props described with holder/hand, grip or support point, orientation, contact relationship, visible change, and final location/state?
- Has the copy-ready final prompt removed unresolved options such as `或`, `或者`, `A/B`, `二选一`, or `可选`, unless the user explicitly requested variants?
- Are professional shot-size, camera-movement, and focus terms written with standardized English abbreviations where appropriate, such as `ECU`, `VCU`, `BCU`, `CU`, `MCU`, `WS`, `KS`, `FLS`, `LS`, `ELS`, `MS`, `MLS`, `Dolly In/Out`, `Pan Right/Left`, `Tilt Up/Down`, `Track Right/Left`, `Crane/Jib`, `Arc/Orbit`, `Zoom In/Out`, `Dolly Zoom`, `Whip Pan`, `Rack Focus`, `Focus Pull`, `Handheld`, and `Static`?
- Does each named camera movement have a clear dramatic function: intimacy, context reveal, gaze/action following, scale, power shift, disorientation, transition, urgency, or deliberate stillness?
- If the prompt uses cinematic lighting, is the amount of lighting detail proportional to the scene? For ordinary scenes, is lighting kept to one compact motivated phrase instead of a full breakdown?
- If the prompt uses detailed cinematic lighting, does it specify Key Light, Fill Light, Rim Light or Soft edge highlight, Background/Volumetric Light, concrete surfaces touched or hidden by light, tonal structure such as `Low-key High Contrast` when relevant, color-temperature meaning when relevant, and the emotional/story meaning of the light-shadow design?
- If `Hard side-top Key Light` or `右上方硬质侧顶光` appears, is there a believable source in the environment and a story reason for such hard light?
- If the scene has movement, does light interact with the movement through passing windows, doors, headlights, screens, weather, dust, fabric, breath, or moving shadows instead of remaining a static adjective?
- Are abstract words translated into visible action, light, sound, object, or performance?
- Has every abstract effect or theme been converted into eye-observable screen evidence instead of left as a label?
- Have physically, spatially, emotionally, or temporally contradictory instructions been removed or rewritten?
- Is the desired action path written positively before using any `不要...` constraints?
- Are details limited to what reduces ambiguity, supports continuity, clarifies emotion, or prevents likely failure, rather than over-specifying every pixel?
- If reference-image prompts are included, are they optional, concise, and consistent with the final video prompt?
- Are reference types selected by production need rather than outputting character, scene, and prop prompts mechanically?
- Is an identity reference distinguished from an exact first-frame reference?
- Are reference-image prompts complete enough for image generation, including current segment clothing, appearance, dirt/wetness/injury/makeup, emotional baseline, scene layout, light, materials, and action space where relevant?
- Do reference prompts avoid generic portraits or generic empty scenes when the current segment requires a specific costume state, disaster state, period styling, transformation, or emotional condition?
- For every single-character reference, does the prompt describe only one visible person and avoid mentioning other characters, relationships, or interaction actions that could generate extra people?
- If two or more characters need to appear together, has that been placed in a separate relationship/two-shot reference instead of contaminating individual identity references?
- For continuation, does the next prompt continue the previous story state while preserving identity, scene, lighting, sound bed, and key props without blindly copying the previous tail frame?

### Time and Rhythm

- Are time blocks playable, with enough duration for action, camera movement, line delivery, and reaction?
- If the user gave a short but content-dense plot, has it been split or narrowed instead of crammed into one 30s prompt?
- Is key dialogue or peak action not placed at the final instant?
- Does the ending leave 1-2 seconds for breath, reaction, sound tail, or visual afterimage?
- Are there too many events for the duration? If yes, remove details or split.
- Is shot duration based on dramatic weight instead of equal mechanical division?

### Dialogue and Sound

- If the plot implies a key spoken line, is the actual line written?
- Are phone calls, doctor/police notices, confessions, breakups, voice messages, or offscreen lines concrete?
- Is key dialogue short enough for the time block?
- Has dialogue delivery time been estimated using an appropriate speech rate, including pauses and listener reaction?
- If dialogue drives the acting, does the prompt treat the line as an expression timeline rather than placing a mood label before quoted text?
- Are trigger words, emphasis, pauses, breath, gaze changes, facial/body reactions, and post-line state tied to the actual wording?
- If a character moves from anger/sarcasm/calmness into vulnerability, is there an emotion barrier and a believable crack before crying, confession, or collapse?
- Are tears, voice breaks, outbursts, forgiveness, or surrender delayed until the line or reaction actually earns them?
- Does the shot have enough time for dialogue, physical action, camera movement, and reaction without rushing?
- Does sound design include concrete diegetic sound rather than generic music?
- Does the prompt avoid background music by default and keep only necessary dialogue/voice, ambient sound, Foley, movement, object, and action sound effects?
- Is silence or sound reduction used when it would strengthen shock, tension, or aftermath?

### Character Performance

- If human performance realism is central, is the visible behavior driven by one clear psychological motive rather than isolated facial expressions?
- Do expression, eye line, voice texture, pause placement, mouth corners, brow, jaw, breath, and body language serve the same inner state?
- Are incidental gestures state-driven and low-motivated by the moment, rather than decorative posing or random action?
- Do head, eyes, neck, shoulders, breath, hands, sleeves, and weight shift move as a linked body system instead of isolated parts?
- Are emotions expressed through eyes, lips, jaw, breath, hands, posture, and timing?
- For intense emotional scenes, is there a continuous chain from inner conflict to physiological reaction, micro-expression, action anchor, and decisive behavior?
- Does the recurring hand/prop/posture anchor evolve continuously instead of resetting between beats?
- For long close-ups, is there a smooth micro-expression timeline with no sudden jump?
- Are 3-5 micro-expression beats chosen instead of an overloaded facial-action list?
- If AU/FACS appears, is it only auxiliary calibration after visible natural-language facial action, with compact intensity and no long code dump?
- Do important facial expressions have onset, peak, and release/transform rather than appearing fully formed from the first frame?
- Is the performance natural for the character's situation, age, status, and relationship?
- Are tears, crying, anger, or fear restrained unless the story specifically needs a large outburst?
- For recurring characters, are permanent identity traits separated from temporary state such as tears, sweat, dust, injury, or costume damage?

### Camera and Visual Logic

- If the scene uses phone realism, documentary realism, period candlelight, low-key crime, commercial product, or another visual mode, are camera, light, focus, grain/noise, stabilization, skin texture, and spatial scale consistent with that single shooting condition?
- When a character touches an object, is there believable before/contact/pressure/aftermath logic with weight, friction, resistance, shadow, reflection, or cloth response?
- Do hair, clothing, props, light, reflection, sound, or room tone respond subtly to character motion so the person does not feel pasted onto the background?
- Is the camera movement physically plausible?
- Is camera movement motivated by gaze, body movement, emotional distance, or object interaction rather than decoration?
- Has the prompt avoided piling up multiple camera moves in one beat when a single `Static`, `Dolly-In`, `Pull-Back`, `Pan`, `Tracking`, or `Handheld` choice would be clearer?
- If this is a one-take scene, does it have a clear start frame, physically possible camera path, blocking/focus change, foreground/background depth, stable screen direction, and held ending?
- If this is a one-take multi-character reveal, are characters revealed progressively with foreground masking, lateral movement, or pull-back hierarchy, and are their faces, hairstyles, costumes, postures, and emotional baselines distinct enough to avoid repeated faces?
- If `Rack Focus` or `Focus Pull` appears, does it shift attention between meaningful subjects such as face/object, foreground/background, reflection/body, or hand/reaction?
- Before a large body action, does the framing create enough physical space to show it clearly?
- Does each shot have a clear subject and composition?
- For action or crowd scenes, is spatial direction clear?
- For large scenes, is there one visual anchor the model can follow?
- For product/person texture scenes, are materials, tactile details, and light concrete?
- For memory/dream scenes, is there a transition anchor such as sound, object, gesture, or match cut?
- In multi-shot prompts, do adjacent shots avoid overly similar shot sizes unless motivated?
- When cutting between shots of the same subject or interaction inside the same scene, does the camera angle change by at least 30 degrees? If cutting to a new scene or location, is the new opening composition clear instead of forcing the 30-degree rule?
- Is the 180-degree axis preserved, or is any axis crossing visibly motivated?
- Do dialogue eyelines remain matched across reverse shots?
- Are entry/exit and travel directions continuous across connected spaces?
- Are handedness, prop position, costume state, tears/injury marks, and body posture continuous?
- For recurring scenes, are doors, furniture, lights, damage, props, entrances, and action paths consistent with the scene bible?
- In continuation, does the previous ending define continuity facts while the next opening uses the most natural bridge type rather than forcing the exact same tail frame?
- Are insert shots used when long dialogue or emotional pauses need breathing room?
- Does the ending leave a 1-2s performance pause or visual/sound tail?
- If one action is split across shots, does the second shot continue the same action with match-on-action continuity?
- Are action, light change, environmental reaction, and sound effect bound to the same readable event where appropriate?

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
