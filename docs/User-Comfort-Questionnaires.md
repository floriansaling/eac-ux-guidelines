### NASA Task Load Index (NASA-TLX)

**Description:** The NASA-TLX is standard workload measure that rates how much an task (or task sequence) has effected the user’s workload. \[[23](References.md)\]

**Steps:**

1. **Step: Setting the Weights**

   User set the weights of six factors that can contribute the workload. This is done by asking the user to compare two different factors for a task or task segment. The user quickly can mark the factor that contributed to workload for each comparison. Every time a factor is chosen, its weight will increase by one. Thus, creating weights for each factor going from 0 to 5. \[[23](References.md)\]

   <img src="/eac-ux-guidelines/uploads/e58db82ab5f352a844218b2506df1fed/image.png" alt="image.png" width="332" height="482"><img src="/eac-ux-guidelines/uploads/7bf902406d6c7cec923bb142429d8fd7/image.png" alt="image.png" width="341" height="474">
2. **Step: Magnitude of Loads**

   After step 1, each user has to rate the magnitude of each factor for that task or task sequence. The rating goes from 0 (low) to 100 (hight). The scale is usually presented in increments of 5. If a user chooses a value between two increments the value is rounded up to the next increment. \[[23, 35](References.md)\]

   <img src="/eac-ux-guidelines/uploads/47f0d34971831e5e74377b3d64d21c60/image.png" alt="image.png" width="402" height="600">

   https://humansystems.arc.nasa.gov/groups/tlx/downloads/TLXScale.pdf
3. **Step: Applying the Weights**

   The weighted ratings score for each factor is calculated by multiplying the rating from step 2 with the factor’s weights from step 1. The sum of all weighted rating scores is then divided by 15. The final result is workload score. \[[23](References.md)\]

   <img src="/eac-ux-guidelines/uploads/fe28414053b8deb01b86b97ef92b49f3/image.png" alt="image.png" width="274" height="69">
4. **Step: Interpretating the Results**

   There is no official threshold, so the results can be interpreted based on previous experience or personal decided cut-off table. One possible range could be as follows: \[[10](References.md)\]

   <img src="/eac-ux-guidelines/uploads/a4742607d317682d791dc288579c71a6/image.png" alt="image.png" width="462" height="299">

### Simulator Sickness Questionnaire (SSQ)

**Description:** The SSQ is most commonly used method to asses simulator-induced discomfort using VR and other immersive environments. \[[20](References.md)\]

**Steps:**

1. Step: Rating each Symptom

   The user goes through a list of 16 symptoms and rates them from 0 (Not at all) to 3 (Severe). \[[49](References.md)\]

   <img src="/eac-ux-guidelines/uploads/aded68856e0e3af5fde4e4e25df5840f/image.png" alt="image.png" width="457" height="600">

   https://conservancy.umn.edu/server/api/core/bitstreams/0c43ba9e-dc67-4361-8739-421f2e242ccb/content
2. **Step: Calculating the Score**

   Each rated symptom is then multiplied by their corresponding weight. There are three weight categories (Nausea, Oculomotor, and Disorientation). The sum of all weighted symptoms belonging to the each weight category are the weighted totals to that specific category (e.g. the sum of the rated score of General Discomfort, Increased Salvation, Sweating, Nausea, Difficulty concentrating, Stomach Awareness, and Burping is the weighted total for the nausea category). Each category score is calculated by the sum of their weighted totals multiplied by their corresponding weight factors (e.g. Nausea category score is the weight totals for nausea times 9.54). The final SSQ score is the sum of the weighted totals of all three categories multiplied by 3.74. \[[20, 30](References.md)\]

   <img src="/eac-ux-guidelines/uploads/9a1f0e03372ad591424e9da1144d4728/image.png" alt="image.png" width="575" height="565">
3. **Step: Interpretating the Results**

   There is also no official cut-off of SSQ results that defines the severity of the tested application. The interpretation is usually done based on central tendency (i.e., mean or median) of all the users that have filled out the questionnaire regarding the same application. If that is not possible the general rule of thumb is a SSQ score above 20 indicates mild symptoms and a score above 40 suggests moderate to severe simulator sickness. \[[20, 30](References.md)\]