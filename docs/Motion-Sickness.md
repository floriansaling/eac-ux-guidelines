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

* Align virtual movement with the user’s physical movement to reduce conflict between vision and body.
* Keep movement smooth and consistent; use teleportation or controller-based rotations to minimize head strain.
* Provide seating options and let users control their movement and rotation.
* Subtly restrict field of view during movement to reduce peripheral motion.
* Create a comfortable environment and encourage short breaks.
</td>
<td>

* Include sudden accelerations, fast zooms, rapid falls, or unnatural rotations.
* Force pinned GUIs on the camera view without adjustments.
* Over-restrict FOV or make users turn their heads excessively.
* Expose new users to prolonged VR sessions without mitigation.
</td>
</tr>
</table>

Motion sickness, often referred to as cybersickness in virtual environments, is a condition that affects about one-third of users in immersive virtual environments. Common symptoms of virtual-induced motion sickness include nausea, fatigue, disorientation, headache, excessive sweating, dry mouth, vertigo, and difficulty with hand-eye coordination. One of the leading explanations for its cause is the mismatch between the user’s physical movement and the visual motion presented in VR. When the body senses one thing but the eyes report another, the brain interprets the conflict as discomfort. New users are particularly susceptible, and a negative first experience can make them hesitant to return to VR. Because of this, designing applications with feature that mitigate motion sickness in mind is essential for both user safety and long-term engagement. The Simulator Sickness Questionnaire can be used to asses the user comfort level of the application (see [User Comfort Questionnaires](User-Comfort-Questionnaires.md)) \[[9, 42, 51, 53](References.md)\]

* **Align Virtual Body Movement With Physical Movement:** The closer the virtual body’s movement and rotation matches the user’s actual physical motion, the lower the risk of motion sickness. Especially in combination with camera effects, such as waveform motions, fast zoom effects, rapid falls and sudden flips, can cause discomfort to the user. Rotations around the z-axis, which are often aligned with head movements, cause less intense motion sickness than rotations around the x and y axes. \[[9, 31, 33, 42, 53](References.md)\]
* **Favour Consistent Movement Speed:** Sudden movement stops, fast accelerations, or irregular shifts in speed can trigger motion sickness. Keeping movement smooth and consistent helps the user anticipate motion and feel more stable within the environment. \[[9, 11, 31, 53](References.md)\]
* **Favour Minimal Head Movement:** Excessive or rapid head movement can cause motion sickness and neck strain. To better accommodate the user, controller-based rotations (see [Mapping](Mapping.md)) or full body rotations while standing or sitting in a swivel chair are recommended. \[[51](References.md)\]
* **Favour Teleportation Methods:** Teleportation is a movement technique that allows users to jump from one location to another (see [Controller Mapping](Mapping.md)). Studies have shown that this is the best controller-based movement option in VR to reduce the effects of motion sickness. \[[7, 9, 33, 42](References.md)\]
* **Favour User Autonomy:** Users tend to feel less motion sick when they have clear control over how they move and rotate. Drifts, unwanted rotations, or sudden, unplanned teleportations can cause disorientation and increase the likelihood of motion sickness. \[[9, 32](References.md)\]
* **Favour Restricted Field of View during Movement:** Narrowing the field of view, e.g., through a vignette effect, can help reduce discomfort during movement or rotation by limiting peripheral motion. However, an overly restricted FOV can reduce immersion and encourage users to move their heads more, which may worsen symptoms. A balanced, adjustable approach works best. \[[7, 9](References.md)\]
* **Avoid Pinned GUI to Camera:** A GUI, such as a menu attached to the user’s camera view, can increase feelings of motion sickness, especially during movement or rotation. Introducing a slight delay in their motion or attaching the interface to in-world objects or the user’s arm can reduce this effect (see [Billboard Interfaces](Graphical-User-Interface.md)). \[[4, 32](References.md)\]
* **Provide Seating Option:** Studies have shown that sitting while being in a VR environment can mitigate motion sickness symptoms. Applications should therefore support seated play, including controller-based turning, reach-adjusted object placement, and comfortable interaction distances. This not only helps reduce symptoms but also improves accessibility (see [Accessibility](Accessibility.md)). \[[3, 9, 42, 53](References.md)\]
* **New Users Are More Susceptible:** Users with more VR experience have reported fewer motion sickness symptoms than new users. Studies suggest that repeated exposure can help reduce motion sickness symptoms over time. Theories also suggest that becoming accustomed to a VR environment with a high likelihood of inducing motion sickness can help astronauts prepare for motion sickness in microgravity. Although users can benefit from building tolerance to motion sickness over time, more susceptible users should still be able to enjoy VR and not be exposed to symptoms any more than necessary. One solution would be to add features that can mitigate the feeling of motion sickness, such as limiting unnatural rotations, restricting the field of vision, offering seating options, creating a comfortable environment and more, which the user or a supervisor can turn on or off so that the user can slowly ease into the application. \[[9, 32](References.md)\]
* **Create a Comfortable Environment:** Users should be aware of whether an application is more likely to induce motion sickness and of methods that can help mitigate symptoms, e.g., sitting down or chewing gum. They should feel comfortable asking for breaks, and supervisors should regularly check in to ensure the user is doing well. Small environmental adjustments, e.g. providing airflow from a nearby fan, can also help alleviate symptoms and make the overall experience more pleasant. \[[9](References.md)\]

  <img src="/eac-ux-guidelines/uploads/7ebf0d28833c3f2d5c655b496153335f/Disoriented.PNG" alt="Disoriented.PNG" width="261" height="279">