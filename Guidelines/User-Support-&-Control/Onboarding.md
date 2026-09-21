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
<li>Provide instructions that are always accessible and easy to revisit</li>
<li>Make tutorials interactive, flexible, and paced for the user</li>
<li>Use clear, simple visual cues, diagrams, or tooltips to guide actions</li>
<li>Give immediate and specific feedback on user actions</li>
</ul>
</td>
<td>
<ul>
<li>Overwhelm users with too much text or complex instructions</li>
<li>Assume all users will complete tutorials successfully on the first attempt</li>
<li>Hide instructions or tutorials outside the user’s field of view</li>
<li>Force a rigid tutorial pace that pressures or frustrates the user</li>
</ul>
</td>
</tr>
</table>

User experience with XR applications varies widely, with most having no prior experience. For this reason, onboarding is an important part of any application. Onboarding is the process of providing new users with instructions on how to use a digital application. The degree of onboarding can vary from application to application, depending on the application's usage duration and the expected user autonomy. The following onboarding variations will be discussed: tutorial, controller diagram, and virtual controller with tooltips.

#### General Onboarding

* **Instructions Need To Be Consistently Available:** No matter the onboarding method used for the application, the instructions need to be consistently available to the user. Users can accidentally close the onboarding, misunderstand instructions, or simply forget parts. Especially at the beginning, when everything can be quite overwhelming for new users, it can be difficult to focus solely on onboarding. Ensuring instructions are always retrievable helps them revisit content at their own pace. \[[12, 47](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]
* **Appropriate Colour Choices:** It is important, especially for larger areas such as backgrounds, to choose appropriate colours. Studies have shown that certain colours, such as highly saturated and highly luminescent colours, can cause fatigue (see [Visual Fatigue](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/User-Comfort/Visual-Fatigue.md) and [Colours](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/Visual-Design-&-Presentation/Colours.md)). Additionally, some font or icon colours might be hard to read depending on the environment colours, so those have to be chosen and tested accordingly. \[[31, 33](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]

#### Tutorials

* **Benefits:** While in-person guidance can be helpful, studies show that users often prefer non-verbal tutorial formats. Supplementing or replacing verbal instructions with interactive tutorials improves both understanding and engagement. \[[12](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]
* **Make the Tutorial Interactive:** Interactive means that the tutorial asks the user to perform the action as part of the tutorial. Studies have shown that having the user interact with the system as part of the tutorial can encourages deeper learning, increases focus, and boosts motivation. \[[12](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]
* **No Time Pressure:** Users should progress at their own pace. Rushing through it could cause mistakes. Added pressure can also make users, especially inexperienced ones, feel overwhelmed. \[[12](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]
* **Tutorial Should Be Noticeable:** Tutorials must remain visible and easy to identify. If the tutorial is positioned outside the user's field of view or blends in with the environment, the user might miss the instructions. If there are multiple instructions, make sure that it is clear which instruction is the current one. This can be done by placing it in front of the user, highlighting it with colours or markers (e.g., arrows), or getting the user's attention through sound or vibration. \[[12](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]
* **Tutorial Should Be Flexible:** Not every user has the same level of experience with the device or application. Some users do not need to go through the tutorial and should be able to **skip** the tutorials. This should also be possible inside the tutorial if it has already started and the user has changed their mind, or if the user wants to explore only a specific section and skip everything else. Some other users may be overwhelmed and want to hear particular instructions again. Especially important sections should have a **redo** option. \[[12, 16](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]
* **Keep Content Complexity Appropriate:** Too complex or long instructions can overwhelm users and could lead to misinformed or random actions (see [Super Soldier Syndrome](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/User-Support-&-Control/Super-Soldier-Syndrome.md)). On the other hand, too minimalistic or short instructions could lead to ambiguity, frustration and confusion. Aim for small, manageable steps with enough detail to be clear and actionable. \[[12](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]
* **Give Feedback:** Feedback is crucial for tutorials. Users need to know when they have completed a section and how successful they were to help them progress and learn, and to ensure they perform the action. The more specific feedback, the better. The degree of feedback can range from making the next section available once the previous one is completed successfully, to telling them if an action went well or not, to what exactly went wrong, and how to fix it. \[[12](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]
* **Be Aware of Accidental Success:** Users can accidentally complete a section or even the tutorial, either by accidentally pressing the right button or by trying multiple things at once because they are confused. For these reasons, it is important to make the **feedback** as clear as possible, so if they succeed, they know why and to make it possible to **redo** sections so they can consciously perform the right action during their second attempt. \[[12](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]

#### Controller Diagram

<img src="https://raw.githubusercontent.com/theorchestrator/eac-ux-guidelines/main/uploads/7c90ec898851eb81a06c08d579b13753/Screenshot_2026-01-16_110011.png" alt="Screenshot 2026-01-16 110011.png" width="457" height="321">

* **Benefits:** Studies have shown that controller diagrams have a significantly higher controller learnability than just text-based instructions. \[[29](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]
* **Keep It Simple:** Do not overwhelm users with too much text. Keeping it simple helps the user to quickly understand the diagram without being too overwhelmed by the new instructions. Too much text could also lead users to miss vital information if they only skim it. \[[12, 29](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]
* **Make It Easy Accessible:** The user should know where to find the controller diagram. One solution would be to have the controller diagram always open when the application starts. Having that, the user is aware that a controller diagram exists and can immediately familiarise themself with the controls once they enter the virtual environment.

#### Virtual Controllers with Tooltips

<img src="https://raw.githubusercontent.com/theorchestrator/eac-ux-guidelines/main/uploads/3389668743aed3d80d19ab61eda594ae/Screenshot_2026-01-13_145345.png" alt="Screenshot 2026-01-13 145345.png" width="434" height="257">

* **Benefits:** Virtual controller with tooltips typically outperform text-based instructions and diagrams for complex applications, offering higher learnability, better performance, and improved player experience. \[[29](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]
* **Keep It Simple:** The texts on the controller tooltips should be short and simple (ideally no more than two words). Too long descriptions could make reading harder, and the labels would obstruct more of the environment. \[[12](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]
* **Appropriate Access:** The controller tooltips could block the user's view in certain situations. In those situations, the user should have the option to hide the tooltips, or it automatically turns off. It should also be easy to make it visible again. Having a button that makes it appear again could make the controls unnecessarily complicated. The best option would be to have it appear automatically (e.g. only available in certain situations, through specific hand gestures, or upon user inactivity) or via an instructor's outside influence. \[[29](https://github.com/theorchestrator/eac-ux-guidelines/blob/main/Guidelines/References.md)\]