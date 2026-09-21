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
<li>Limit interactions to essential elements to guide correct user behaviour</li>
<li>Break procedures into small, clear steps to prevent skipping or improvisation</li>
<li>Provide simple, unambiguous instructions to reduce guessing or random actions</li>
<li>Give precise, immediate feedback to reinforce correct actions</li>
<li>Use multisensory feedback (audio, haptics, etc.) to make actions feel realistic and meaningful</li>
</ul>
</td>
<td>
<ul>
<li>Allow unlimited freedom that could encourage skipping steps or unsafe improvisation</li>
<li>Present complex or confusing instructions that users might misinterpret</li>
<li>Give vague feedback that could let users reinforce incorrect behaviour</li>
<li>Neglect sensory cues that make virtual actions feel consequential</li>
</ul>
</td>
</tr>
</table>

Many XR applications aim to simulate realistic environments and immerse users as deeply as possible, but most users always know, on some level, that they are still inside a simulation. Because virtual environments carry fewer real-world consequences, users often feel unusually confident or invincible. This can lead to behaviours like skipping steps, ignoring instructions, experimenting with actions they would not try in reality, or even performing movements that could be unsafe outside the simulation. This becomes a design challenge, as it makes user behaviour harder to predict and can reduce the accuracy of training outcomes. In learning scenarios especially, users may remember their improvised or irrational actions as part of the official procedure and later repeat them in real life, where mistakes have actual consequences. \[[8](References.md#ref-8), [25](References.md#ref-25), [40](References.md#ref-40)\]

* **Favour Interaction Limitations:** Keep interactions more focused and restricted by making only the necessary elements, such as specific buttons or buttons, interactive. When users have unlimited freedom, they are more likely to press random buttons, skip critical steps, or engage with objects that are not part of the intended flow. Thoughtfully limiting interactions helps guide them toward the correct actions and reduces the likelihood of unsafe improvisation. \[[12](References.md#ref-12), [21](References.md#ref-21)\]

    ![Screenshot 2026-01-16 104749.png](/eac-ux-guidelines/uploads/1280838ece47c2e1882d63e8ac264669/Screenshot_2026-01-16_104749.png){width="900"}
* **Favour Small Steps:** Breaking procedures into small, clear steps helps users follow them correctly and reduces the temptation to jump ahead. This is especially important in simulated learning environments. If users perform steps in the wrong order or skip essential actions, they might remember these incorrect behaviours as part of the real procedure. Providing a steady, guided progression helps ensure accuracy and lowers the chance of unsafe habits forming. \[[12](References.md#ref-12)\]
* **Favour Simple Instructions:** If the user is presented with overly complicated instructions, they might misread or misunderstand them, leading to unintended mistakes. Especially for new users, some interactions are not as obvious as for more experienced users, which can lead to guessing, random button presses, or self-invented shortcuts. Clear instructions reduce frustration, improve accuracy, and make the experience smoother for both novice and experienced users. \[[12](References.md#ref-12), [25](References.md#ref-25)\]

    ![Screenshot 2026-01-16 144929.png](/eac-ux-guidelines/uploads/880ee4ada87c12b8459218c99eef645a/Screenshot_2026-01-16_144929.png){width="480"}
* **Avoid Ambiguous Feedback:** Users depend on feedback to understand how well they are following the intended process. If the feedback is too vague, users might not know what they did right or wrong. If a user acted out on their own and by coincidence fulfilled the task successfully, e.g. pushing random buttons or picking up various objects, they might remember their wrong actions as part of the instructions. Precise, immediate feedback helps reinforce the right behaviour. In some scenarios, allowing progression only after a correct action can prevent users from learning unsafe alternatives. \[[12](References.md#ref-12)\]
* **Favour Multisensory Feedback:** Studies suggest that a lack of sensory input highlights the unnaturalness of the simulated environment. When sensory input is minimal, users often become more aware that their actions have no real consequences, which can fuel overly confident or reckless behaviour. Research has shown that actions learned through multisensory interfaces may be better remembered when applied in the real world. While some sensory inputs, such as smell, taste, and touch, are challenging to replicate in a virtual environment, others, such as audio and tactile feedback, can make simulated actions feel more meaningful and realistic. \[[8](References.md#ref-8), [40](References.md#ref-40)\]
