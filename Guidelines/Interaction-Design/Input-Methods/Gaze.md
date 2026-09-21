<table>
<tr>
<th>

<img src="https://raw.githubusercontent.com/theorchestrator/eac-ux-guidelines/main/uploads/9ffa5835d60764111f03716acdb78806/Yes.PNG" alt="" width="88" height="88">Do's
</th>
<th>

<img src="https://raw.githubusercontent.com/theorchestrator/eac-ux-guidelines/main/uploads/d414000014132194ace6f369fde11cc7/No.PNG" alt="No.PNG" width="83" height="83">Don'ts
</th>
</tr>
<tr>
<td>
<ul>
<li>Provide subtle feedback to confirm gaze interaction without distraction.</li>
<li>Combine gaze with other inputs (e.g., gesture or voice) for better control.</li>
<li>Use sufficiently large targets to reduce strain and improve accuracy.</li>
</ul>
</td>
<td>
<ul>
<li>Force unnatural or repetitive eye/head movements through poor layout.</li>
<li>Attach UI elements directly to gaze in a distracting way.</li>
<li>Make feedback too immediate or flickery due to natural eye movement.</li>
</ul>
</td>
</tr>
</table>

Gaze is an interaction method that allows users to engage with an application without relying on voice or hand input. It is particularly useful in situations where hands-free interaction is required or when other input methods are limited. There are two primary types of gaze interaction: head-gaze and eye-gaze. Head-gaze uses the orientation of the user’s head to determine what they are pointing at, typically through a raycast originating from the centre of the head. In contrast, eye-gaze enables more precise interaction by tracking exactly where the user is looking. Both approaches offer distinct advantages and limitations. The choice between them depends on the context of the application, the required level of precision, and the overall interaction design.

<img src="https://raw.githubusercontent.com/theorchestrator/eac-ux-guidelines/main/uploads/016d45314b3a28fda1ee6dcb26a9b213/image.png" alt="image.png" width="900" height="398">\[34\]

* **Favour Appropriate Feedback:** Feedback is especially important for gaze interactions since users need to know that it is active and functioning correctly. This feedback should remain subtle to avoid interrupting the user’s workflow or causing unnecessary stress. Techniques such as gentle highlighting or slight scaling of targets can provide confirmation without being distracting.
* **Favour Combination with Other Inputs:** Gaze is most effective when combined with other input methods. For example, users can use gaze to select a target and confirm actions through gestures, voice commands, or controller input. This reduces the risk of accidental activation, supports multitasking, and gives users greater control over their interactions.
* **Choose Appropriately Sized Targets:** Targets that are too small can lead to eye strain and increase user fatigue, as they require greater focus and precision. Larger targets help reduce errors caused by natural eye jitter and make interactions more comfortable and accessible.
* **Avoid Enforcing Unnatural Eye or Head Movements:** Interfaces should not require exaggerated or unnatural movements to interact with elements. Poor placement of targets may force users to repeatedly move their eyes or head in uncomfortable ways, which can lead to fatigue and reduced usability.
* **Avoid Attaching UI Directly to Eye Gaze:** Since eye movements are rapid and constant, attaching UI elements (such as cursors) directly to gaze can feel overwhelming and distracting. It can also obstruct important visual information in the environment, making interactions more difficult.
* **Favour Delayed Visual Feedback:** Introducing a slight delay before displaying gaze-based feedback can help prevent flickering caused by natural eye or head movement. This delay should be carefully balanced so that feedback still feels responsive and does not appear unresponsive or lagging.

These guidelines have been taken and summarised from the Microsoft Mixed Reality Guidelines \[[34](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]