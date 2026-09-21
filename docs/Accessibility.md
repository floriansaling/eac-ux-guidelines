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
<li>Design for all users, including left-handed, colourblind, or mobility-limited individuals</li>
<li>Offer flexible movement and seating options to accommodate varying physical abilities</li>
<li>Use multimodal communication (visual, auditory, haptic) for key information</li>
<li>Provide adjustable difficulty levels and allow reversibility of actions</li>
<li>Make accessibility features visible, easy to activate, and explain them during onboarding</li>
</ul>
</td>
<td>
<ul>
<li>Assume all users have the same abilities or environmental conditions</li>
<li>Rely solely on audio, colour, or precise physical actions to convey information</li>
<li>Place critical objects or instructions out of reach or only in peripheral zones</li>
<li>Force users into one interaction style (e.g., only standing, only right-handed)</li>
<li>Overlook temporary or situational disabilities (e.g., holding items, noisy environments)</li>
</ul>
</td>
</tr>
</table>

### Why it is important:

* **Reach a Wider Audience:** Assuming every user has the same abilities can unintentionally exclude large groups of people. Understanding and applying accessible design practices ensures that more people can use and enjoy the application.
* **Improve the Experience for Everyone:** Accessibility features often help far more people than the groups they were originally designed for. Many everyday tools have started as design inventions for people with disabilities (e.g. audio books, electric toothbrushes, curb cuts, dark mode, and more). \[[27](References.md)\]
* **Positive Public Perception:** Because accessibility is still not standard in most applications, especially in XR, applications that actively consider accessibility stand out and gain more attention. People also become more curious and invested in applications that see them and accommodate their needs.
* **Disability is a Spectrum:** Disability is not defined by someone's health condition but by a mismatch between a person and their environment. Not every disability is the same, and people have different needs and preferences. Even small changes can make an application more accessible, and bigger changes might help more people than initially intended. Especially when looking at permanent, temporary and situational disabilities, it becomes clear that the people who can benefit from accessibility features are more than initially expected. \[[5, 16, 18](References.md)\]
* **Permanent, Temporary and Situational Disabilities:** There are five different categories of disabilities: motor skills (touch), vision, hearing, speech, and cognition. People with **permanent disabilities** are permanently affected by disabilities that fall into one or more of these categories, such as people who are blind, deaf or missing an arm. There are also people who are not permanently affected by a disability but can benefit from the same accessibility accommodations, such as people with temporary or situational disabilities. **Temporary disabilities** are conditions such as a broken arm, an eye or ear infection, which can make people temporarily dependent on a more accessible environment. There are also situations which cause people to experience **situational disabilities** suddenly. For example, loud and noisy environments such as fairs can make it hard to hear audio guidance or concentrate on the application; a heavy accent can cause trouble with voice recognition; and holding something can make using two controllers difficult. Everyone experiences some form of disability at times, so it’s important to design with this in mind. \[[5, 18, 19](References.md)\]

  <img src="/eac-ux-guidelines/uploads/fffd0dea5a0efad25121b67308debe97/image.png" alt="image.png" width="879" height="494">\[[19](References.md)\]

### General Guidance:

* **Accommodate Left-Handedness:** Around 10% of the population is left-handed, so it is essential to design an application that makes it comfortable and natural to use, regardless of the user's dominant hand. Especially simulations, such as training applications that rely on replicating a known environment in virtual reality and where interactions are important, can cause frustration, discomfort, and mistakes by making users complete tasks with their less dominant hand. To accommodate left-handed people, both the left and right controllers could have the same functions when interacting with objects, e.g., grabbing, or the user can switch the controller mapping via a settings menu or with an instructor's help. \[[1, 32, 33](References.md)\]
* **Accommodate Colour Blindness:** Studies have shown that about one in every 12th men is colourblind. This rate increases even more in countries that have a higher Caucasian population, e.g. in Sweden, around 10-11% of the male population is colourblind. To accommodate people with colour blindness, applications should avoid relying solely on red and green, or blue and yellow, colour combinations to highlight important changes, e.g., green light for active features and red light for inactive features. Pair colours with alternative cues, such as shapes, icons, sounds, or haptics, to ensure everyone can recognise changes. \[[48, 52](References.md)\]
* **Consider Limited Mobility:** XR environments are often highly immersive and interactive. People actively move and interact within the application's virtual world. However, not everyone can turn or bend so easily. Reaching down to grab a virtual item from the ground can be a difficult challenge for some. Additionally, the real-world environment sometimes restricts the user's movement, even when they can bend down to pick something up. Places like fairs often have only a small area for users to test the application, and users need to be careful in their movements to avoid injury, e.g., hitting their head on a table when picking up an item. Possible solutions would be to make objects more reachable by making them bigger, avoiding placing them in hard-to-reach places or allow users to interact from a distance using raycasts or similar tools. \[[3, 16](References.md)\]
* **Offer a Seating Option:** Some XR applications are designed with the assumption that the user is standing, which is not always possible. Some users feel more comfortable using the application while sitting, especially if the duration of the application is longer than just a few minutes. Additionally, studies have shown that sitting down in a VR application can help with motion sickness (see [Motion Sickness](Motion-Sickness.md)). Thus, the user should be able to have the same experience with the application whether sitting down or standing up; i.e., they should be able to move around freely, with visuals and animations of the environment adjusting accordingly, and virtual objects should be easily reachable. \[[3, 9, 53](References.md)\]
* **Reduce Dependence on Audio:** Adding sounds and music to an application can make it more immersive and enjoyable. However, most applications run in environments where it is difficult to focus on their audio. Fairs and the ISS often have noisy backgrounds, where sounds can get lost. Other applications that a trainer or supervisor accompanies should also minimise the sound options, since they can make it difficult for the user to hear instructions. Hence, if sound is used, audio instructions should be paired with text so it is not an issue if the user misses something, and smaller sounds should be accompanied by visual or haptic feedback, e.g. an icon appears, or the controller vibrates in addition to a notification sound.
* **Favour Multimodal Communication:** If a virtual object or action only relies on one of the user's senses, there is a chance the user might miss it, e.g. a silent visual that is placed in the peripheral zone of the user or controller vibration when a task is done. Using multiple senses, e.g. visual, auditory, and haptic, helps make interactions clearer and more accessible to everyone. \[[16](References.md)\]
* **Offer Different Difficulty Levels:** Especially for shorter applications, it is beneficial to offer different difficulty levels to avoid overwhelming users. Some users struggle with learning new things in a short amount of time, some are not in the mindset to take on difficult tasks in that moment, and some are new to XR and even simpler interactions can be quite overwhelming. Making the entire application easier to accommodate these users is not always the best solution, since it could bore more experienced users. A selection of tasks with varying difficulties, or minor setting changes to make the application better fit the user, can create a more enjoyable experience.
* **Allow Reversibility of Actions:** Mistakes are a natural part of interaction, especially in XR where precision can be affected by hand tremors, accidental input, or rushed decisions. Users should be able to undo or redo actions, especially when those actions have a significant impact on the course of the application. \[[16](References.md)\]
* **Make Users Aware of Accessibility Features:** Users might not be aware that there are features that can accommodate their needs and preferences, especially if they are new to XR. Accessibility features or settings should be mentioned in the onboarding or via an instructor in person, so that the user can get the full potential out of the application. If possible, check in with users during the experience, for example, offering a seat if someone seems motion sick or suggesting an easier mode if they appear overwhelmed.

  <img src="/eac-ux-guidelines/uploads/01860000978d4a79ec7d762ee0271431/Screenshot_2026-01-16_110342.png" alt="Screenshot 2026-01-16 110342.png" width="320" height="330"><img src="/eac-ux-guidelines/uploads/d7ddfe9009ec6a397c39b9f68fc3d915/Chair.png" alt="Chair.png" width="208" height="292">