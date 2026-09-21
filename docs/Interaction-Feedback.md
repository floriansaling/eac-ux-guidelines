<table>
<tr>
<th>

<img src="/eac-ux-guidelines/uploads/9ffa5835d60764111f03716acdb78806/Yes.PNG" alt="" width="88" height="88">Do's
</th>
<th>

<img src="/eac-ux-guidelines/uploads/d414000014132194ace6f369fde11cc7/No.PNG" alt="No.PNG" width="83" height="83">Don'ts
</th>
</tr>
<tr>
<td>
<ul>
<li>Use clear, consistent feedback patterns so users know what to expect</li>
<li>Provide feedback for every user action, including delayed or loading responses</li>
<li>Combine visual, auditory, and haptic cues to improve clarity and immersion</li>
<li>Use haptic feedback to reinforce actions without demanding visual attention</li>
<li>Choose colours thoughtfully and pair them with other feedback modalities</li>
</ul>
</td>
<td>
<ul>
<li>Rely on a single sensory channel for critical feedback</li>
<li>Overwhelm users with too many or overly intense feedback signals</li>
<li>Use inconsistent or ambiguous feedback that can confuse user actions</li>
<li>Allow 2D markers or visual cues to blend into the environment and go unnoticed</li>
</ul>
</td>
</tr>
</table>

Interaction feedback refers to the information users receive in response to their actions within a virtual environment. In VR, feedback can be delivered through multiple sensory channels to increase immersion, guide users through tasks, and communicate performance or progress. Clear feedback also strengthens a user’s sense of autonomy, as it reduces reliance on external guidance or supervision. Common feedback modalities include visual, auditory, haptic, and olfactory outputs. While research suggests that olfactory feedback (smell) can significantly enhance immersion and memory retention, it is not always feasible to implement. Therefore, the following guidelines focus on visual, auditory, and haptic feedback, while olfactory feedback is recommended where possible. \[[41, 46, 47, 56](References.md)\]

* **Favour Feedback for Every Action:** Users should always receive confirmation that an action has been registered. Feedback can range from subtle cues, such as a button highlight on hover, to explicit text-based confirmations. This is especially important for actions that involve delays or loading times. In such cases, users need clear reassurance that their input was successful and that they should wait. Loading indicators, progress symbols, or short messages can help prevent repeated inputs or confusion.
* **Avoid Inconsistencies:** Feedback should follow consistent patterns within an application and, where possible, align with patterns used in other applications. Consistency helps users build expectations and reduces confusion, making interactions feel more intuitive and reliable. Inconsistent feedback can lead to uncertainty and increase the likelihood of user errors. \[[12, 47](References.md)\]
* **Favour Clear and Unambiguous Feedback:** Feedback that is too subtle, delayed, or unclear can lead to confusion, frustration, or incorrect actions. Users should immediately understand which interaction triggered the feedback and what it means for their next step. Clear cause-and-effect relationships help users build trust in the system and reduce errors.
* **Avoid Overwhelming Users:** Effective feedback informs without overwhelming. Using too many feedback signals at once, engaging too many senses, or relying on overly intense cues can cause discomfort or confusion. Feedback should be precise, purposeful, and easy to interpret so users know exactly how and when to respond. \[[47](References.md)\]
* **Favour Haptic Feedback:** Haptic feedback, such as controller vibration, adds a physical layer to interaction and can significantly enhance immersion. Studies show that haptic-only feedback can create a stronger sense of presence than visual-only feedback. Used thoughtfully, haptics help reinforce actions and confirmations without demanding additional visual attention. \[[16, 22, 56](References.md)\]
* **Favour Auditory Feedback When Appropriate:** Research suggests that auditory cues, especially binaural sound, can be more effective than visual feedback alone and can reduce search time. However, audio feedback may not always be perceivable due to environmental noise or accessibility constraints (see [Accessibility](Accessibility.md)). For this reason, auditory feedback should be paired with visual or haptic cues to ensure it is reliably perceived. \[[6](References.md)\]
* **Favour Multimodal Feedback:** Multimodal feedback can make an application more accessible (see [Accessibility](Accessibility.md)) and reduce issues such as Super Soldier Syndrome (see [Super Soldier Syndrome](Super-Soldier-Syndrome.md)). Having only colour-coded feedback can make it difficult for people with colourblindness and can cause confusion when using predefined colours, e.g., astronauts assign fixed meanings to colours such as red, yellow, and green. Additionally, studies have shown that multimodal feedback can improve performance, reduce cognitive load and increase user immersion. Even though specific sensory modalities excel at specific tasks or situations, such as haptics for precision or visuals for spatial awareness, the strongest results consistently come from combining multiple sensory outputs. \[[11, 12, 22, 41, 47, 48, 56](References.md)\]
* **Be Conscious About Colour Choices:** Colour coding can be an effective feedback tool when it is paired with other visual, audio or haptic cues. Colours should contrast clearly with the background to remain noticeable, but not so strongly that they cause discomfort or visual fatigue (see [Colours](Colours.md) and [Visual Fatigue](Visual-Fatigue.md)). It is also important to consider the contextual meaning of colours. Colours with strong predefined associations, e.g. red for warnings or errors, should only be used when they align with the intended message. Thoughtful colour choices help ensure feedback is clear, comfortable, and contextually appropriate. \[[47](References.md)\]
* **Favour Billboarding with 2D Markers:** 2D elements can seem off-putting and can often be missed in a 3D environment. Billboarding could be a solution to make 2D markers, such as arrows or icons, more fitting and noticeable. Billboarding means rotating a 2D image towards the user so it always faces them. This makes them easier to spot from any direction and prevents them from being mistaken for part of the environment, such as wall textures or decorative elements.

  <img src="/eac-ux-guidelines/uploads/ed91d460607ea530ca008b3234d7e279/Screenshot_2026-01-30_143801.png" alt="Screenshot 2026-01-30 143801.png" width="295" height="180"><img src="/eac-ux-guidelines/uploads/b7be4dbefcda582f082415b56f551ef6/Screenshot_2026-01-30_143850.png" alt="Screenshot 2026-01-30 143850.png" width="350" height="177">

  <img src="/eac-ux-guidelines/uploads/d2eb74e8029383685924932ca2f128e3/Haptic_Feedback.PNG" alt="Haptic Feedback.PNG" width="202" height="276">