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

* Keep controller mappings simple and easy to learn
* Use intuitive, real-world–inspired interactions where possible
* Stay consistent within the application and across similar XR experiences
* Support multiple movement and rotation options to suit different users
* Allow left- and right-handed use or remapping of controls
</td>
<td>

* Overload users with complex or frequently changing button mappings
* Rely on a single movement or rotation method that may cause discomfort
* Assume all users have the same experience level or physical abilities
</td>
</tr>
</table>

Mapping, or controller/button mapping, refers to the assignment of buttons to various functions. While multiple applications have different functions and can thus differ in their mapping, some functions are present in a majority of applications. These functions are _Movement_, _Rotate_, _Grab_ and _Select_.

#### Example Controller Mapping:

<img src="/eac-ux-guidelines/uploads/3c7b8117d68c07f1a3b9d491947a3645/image.png" alt="image.png" width="721" height="373">

### General Guidelines

* **Keep It Simple:** Too many varied or complex controls can overwhelm or frustrate users, especially those with little VR experience. \[[50](References.md)\]
* **Keep It Intuitive:** Too abstract controls can increase the cognitive load of the user. More intuitive controls also make it easier and quicker for users to learn them. \[[50](References.md)\]
* **Be Consistent:** Avoid switching the controls too much within the same application, and try to keep the same mapping across similar applications. \[[44, 50](References.md)\]

### Movement

Movement in VR can be achieved through various methods, depending on factors such as the limitations of the current virtual environment, the user's VR experience, and more. The most common movement techniques are _Steering, Teleportation_, and _Climbing_.

<img src="/eac-ux-guidelines/uploads/edd7049205863a72f31664bf25af6d80/Screenshot_2026-01-16_144736.png" alt="Screenshot 2026-01-16 144736.png" width="456" height="375">

* **Steering**:
  * **Description:** With the steering technique, the user moves the joystick in the direction they want to move. Depending on the gravity level and the environment of the virtual character, the user will either **walk or fly** towards the direction they are steering. \[[7](References.md)\]
  * **Good for Exploration:** This movement method is especially useful for exploration since the user can take their time and explore everything in their preferred distance without missing anything during their movement. \[[7](References.md)\]
  * **More Intuitive:** Most users find the steering movement technique more intuitive since it resembles movement in other, less immersive virtual environments, such as video games. The onboarding for this method is also quite simple, which makes it easier for new users. \[[7](References.md)\]
  * **Can Induce Motion Sickness**: Studies have shown that this movement can cause motion sickness in users. This is most likely due to the fact that the movement of the virtual character does not align with the movement of the user, who is most likely standing still during application use (see [Motion Sickness](Motion-Sickness.md)). \[[7](References.md)\]
* **Teleportation:**

  <img src="/eac-ux-guidelines/uploads/e00f824d8eecfa33dd9ad48ba7872d01/Screenshot_2026-01-16_104806.png" alt="Screenshot 2026-01-16 104806.png" width="900" height="507">
  * **Description:** The teleportation movement technique allows users to jump from one location to another. This is often done by either using the joystick to point to the location the user wants to jump to, pressing a button and pointing the controller in the desired direction, or a combination of both. Once teleportation is activated, the user usually sees a circle at the desired end position and an arc connecting the circle and the virtual character to indicate the jump. Once the controls are released, the user jumps towards the circle.
  * **Can Reduce Motion Sickness:** Various studies have shown that users feel less motion sick with the teleportation method, especially compared to the steering method. \[[7, 42](References.md)\]
  * **Makes Movement Quicker:** Users can move quickly from point A to point B. This is especially useful when the environment is vast. \[[7](References.md)\]
  * **Can Cause Disorientation:** Due to the jumping, user can often find themself suddenly in a new location, seeing it from a new perspective. This could cause disorientation and confusion, especially for users who are new to VR. \[[7, 42](References.md)\]
  * **Not Intuitive:** The concept of teleportation and its controls are usually not very intuitive, especially for new users. Users can feel overwhelmed by the movement, and it can often lead to accidental teleportation, which can confuse the user. In cases where the application duration is short and/or the user is a bit overwhelmed with the controls, it is good to have an additional movement option to teleportation, e.g. steering. In these cases, teleportation can be activated through another button or via a trainer/supervisor (see [Outside Manipulation](Outside-Manipulation.md)).
* **Climbing:**

  <img src="/eac-ux-guidelines/uploads/43c5156020f5ee422337381298da3927/Screenshot_2026-01-16_104854.png" alt="Screenshot 2026-01-16 104854.png" width="900" height="507">
  * **Definition:** Climbing is a movement method where users use their hands to move their virtual body. Users can grab fixed objects in their environment, such as handles, and push their virtual body towards their desired position. This movement technique is usually used in simulations in microgravity environments.
  * **Suitable for Training:** This method is effective for training users to move in microgravity environments, such as the International Space Station (ISS) or Extravehicular Activities (EVAs), since the movement is similar to real-world movement in these environments.
  * **Can Cause Muscle Fatigue:** To move in these environments, users have to hold their arms up for extended periods of time. Plan breaks so the user can rest their arms for a bit and regularly check in to make sure they are not straining themselves too much.
  * **Can Cause Motion Sickness:** The combination of movement and floating in microgravity creates a dissonance between the user's virtual and real-world movement. This could induce motion sickness (see [Motion Sickness](Motion-Sickness.md)).

### Rotation

There are also various rotation methods in VR. Users often can rotate their heads in VR as a way to rotate. However, this can lead to neck strain, so an additional control-based option for rotation is recommended. One of these options is discrete rotation via the joystick.

* **Discrete Rotation**
  * **Description:** Discrete rotation allows the user, via the joystick, to rotate their field of view by a fixed rotation. Users often prefer this rotation method to other techniques with head movements (e.g. resetting) due to its simplicity and limited head movement. \[[7](References.md)\]
  * **Use Appropriate Rotation Steps:** Studies recommend a rotation of **22.5 degrees**. Any larger rotation can induce motion sickness. \[[7](References.md)\]
  * **Field of View Reduction Recommended:** Studies have shown that using a reduced field of view during rotation can help reduce motion sickness. \[[7](References.md)\]
  * **Different Rotation in Microgravity Simulation:** Controller-based rotations are usually not possible in simulations that aim to represent interactions and movements in microgravity environments realistically. In those simulations, users can usually rotate by grabbing a handle or a fixed object with two hands and pushing their body towards the desired rotation. Be aware that this rotation can cause motion sickness, as the virtual body movement does not align with the user's real body movement.

### Grab and Select

Grab and select are important functions that are nearly always needed in any application. With grab, the user can grab items in their environment and interact with them. The select options allow users to interact with GUIs such as menus.

<img src="/eac-ux-guidelines/uploads/3a88bfc3f609707210683cd1228a8257/Screenshot_2026-01-16_150343.png" alt="Screenshot 2026-01-16 150343.png" width="531" height="344">

* **Choose Appropriate Mapping:** The controller mapping for the grab and select options may vary from application to application, depending on the environment, use case, user, and other factors. Some applications use the **trigger button for selecting items and the grip button to grab objects.** However, when throwing objects, it might be easier to use the trigger button to grab them. Additionally, new users often confuse the trigger and the grip button, so some applications use the same functions for both buttons to make it easier for the user. \[[28, 44](References.md)\]
* **Accommodate Left-Hand User:** Grabbing and selecting are often actions we do with our dominant hand in the real world. To make virtual applications more immersive and comfortable for users, users should be able to interact with objects with either their left or right hand. This can be done by mapping the same functions to both controllers, or by allowing users, either directly or via an instructor or supervisor, to map the controls to their preferred configuration. This could also help other users who cannot use their right hand as a dominant hand (see [Accessibility](Accessibility.md)).
* **Be Aware of Mistakes:** It is easy to accidentally select or grab the wrong thing, especially when selecting an item via raycasting. Most people have a slight tremor in their hands, which can make selecting small items such as buttons difficult. Also, when pressing a button, the hand slightly moves, i.e. the Heisenberg effect, which can lead to further mistakes. \[[50, 55](References.md)\]

### Menu

A button for a menu or similar is another important feature that should be part of the controller mapping. Users should have constant, easy access to a menu or similar GUI that provides options such as closing the application and instructions for interacting with objects in VR.

* **Easy and Intuitive Access:** Users should know where and how to access the menu. The menu button should be easy to find and consistent across all applications to enable easy, intuitive access. \[[44](References.md)\]
* **Be Aware Of Steam Link Overwrite:** The menu button on the left controller is a good option for the menu button for the user. However, when using Steam Link, this menu button will always open the Steam Link Menu unless it is manually changed on the headset. Developers should be aware of that when choosing a menu button.