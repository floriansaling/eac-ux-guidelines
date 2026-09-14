---
title: Billboard Interfaces
---
<table>
<tr>
<th>

![](https://raw.githubusercontent.com/theorchestrator/eac-ux-guidelines/main/uploads/9ffa5835d60764111f03716acdb78806/Yes.PNG){width="88" height="88"}Do's
</th>
<th>

![No.PNG](uploads/d414000014132194ace6f369fde11cc7/No.PNG){width="83" height="83"}Don'ts
</th>
</tr>
<tr>
<td>

* Keep interfaces simple, symmetrical, and visually clear
* Place important UI elements in the comfortable viewing zone
* Use consistent visual or auditory feedback to show what is interactable
* Choose readable sizes, spacing, and a limited colour palette
</td>
<td>

* Overload the user with text, clutter, or floating UI elements
* Pin GUI elements rigidly to the user’s camera view
</td>
</tr>
</table>

Good GUI design can make an application easier, more comfortable, and more enjoyable to use. Research shows that a few simple choices can have a big impact on readability and user comfort.

#### Visual appearance:

* **Favour Rounded Corners:** Users tend to prefer shapes with rounded corners, which can make interfaces feel more approachable and visually pleasant. \[[38](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]
* **Simple and Symmetrical Shapes:** Symmetrical shapes are recognised more quickly than asymmetrical ones. Avoid overly complex or visually busy shapes, as they can distract users or complicate interaction. \[[38](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]
* **Avoid Floating Elements:** Having borders around UI elements such as buttons and text makes it easier for users to read. It will be clear to the user what belongs to the GUI, e.g. a menu, and what does not. Users will also find it easier to select elements when they are part of the same enclosed environment, which can reduce physical motion and eye strain. \[[33, 48](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]
* **Favour Minimal Information Load:** Avoid overwhelming users with excessive text or visual clutter; keep the content simple. When possible, use (intuitive) icons, shapes or colour instead of text to make it easier for users, especially users with dyslexia or limited vision. \[[38](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]
* **Choose Appropriate Button Size and Spacing:** Buttons should be large enough for users to read the text, but not so large as to be intrusive in the overall scene. Additionally, buttons and other interactive elements should have sufficient spacing to avoid accidental selection. Studies have also shown that increasing button size and spacing resulted in a decrease in the number of errors observed and task completion time. \[[4, 48](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]
* **Favour Consistent Feedback:** Through visual or auditory feedback to indicate to the user what is interactable. This feedback could be a button colour change or click sounds to indicate a button press, or a hand shadow when the user is close to interactable objects. \[[4](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]

#### Position:

![image.png](uploads/05f90548cf6e8bc69c4b89fa5a9a688b/image.png){width="453" height="356"}\[4\]

* **Avoid Placing GUI Elements Outside the Comfortable Content Zone:** The comfortable content zone is the visual zone right in front of the user. Any element that is in the peripheral zone is only visible when the user rotates their head, and for elements in the curiosity zone, the user has to move their shoulders in addition to the head movement. Elements that are important or need more time for the user to focus on should be placed in the comfortable content zone. Any elements placed outside the comfortable content zone could cause discomfort, such as neck strain, for the user, or go unnoticed. \[[4](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]
* **Maintain a Comfortable Viewing Distance:** Any GUI elements should be placed at a good distance from the user. For comfort, the GUI should be placed somewhere **between 0.5m and 1m** away from the user. Elements that are placed too far can make interaction more difficult or make text harder to read. \[[4](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]
* **Avoid Pinning the GUI to the User's Camera:** In general, having 2D elements in a 3D environment can cause discomfort or diminish the user's sense of immersion. A pinned GUI, like a menu, could not only obstruct important information or objects in the user's view but also cause nausea while the user is looking around (see [Motion Sickness](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/4.-User-Comfort/Motion-Sickness.md)). To prevent this, wearable menus, e.g. pinned to the hand or arm, or giving the user the option to pin and unpin GUI panels, are recommended. If a pinned menu to the user’s view is required, a small delay in the menu's movement can help by allowing the user to look around and orient themselves for a few milliseconds before the menu appears in front of them. \[[4](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]

#### Colours:

* **Avoid Full Opacity:** Set GUI elements to a slight transparency so the user can see the outlines of objects behind the GUI. But do not make it too transparent, which could reduce readability. \[[33](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]
* **Use a Small Colour Plate:** Too many colour shades can overwhelm users and make text harder to read. \[[4, 48](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]
* **Favour Dark Mode:** Dark mode, light letters on dark background, induces significantly lower visual fatigue than light mode, dark letters on bright background. Additionally, studies have shown that dark mode is often preferred over light mode (see [Visual Fatigue](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/Visual-Fatigue.md)). \[[17](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]
* **Use Vivid Colours Appropriately:** Use vivid colours for important content to draw the user and to gain their attention. But avoid using vivid colours for elements in the peripheral zone, as they could unnecessarily distract them. \[[48](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]
* Check out the sections [Colours ](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/Colours.md)and [Visual Fatigue](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/Visual-Fatigue.md) for more guidance.

#### Examples:

**_Negative_ Example \[**[33](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)**\]:**

![image.png](uploads/b52bc9816ba24aa42a2fcb6d292d6d82/image.png)

* Blurry texts and images
* Located in the peripheral zone
* Floating buttons
* Too small font
* Not enough contrast between background and font
* Confusing shapes
* Inconsistent spacing
* Too intense and misplaced colour highlight

**Positive Example:**

![Screenshot 2026-01-14 142134.png](uploads/ab87074938a53cc42aa0507f820b100c/Screenshot_2026-01-14_142134.png){width="359" height="275"}

* Rounded design
* No floating buttons
* Readable text and icons
* Appropriate colour contrast
* Regular spacing
* Consistent and minimalistic colour scheme
* Simple and symmetric shapes
* Clear indicator for user selection