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
<li>Use short, simple, and distinct commands that are easy to say and remember.</li>
<li>Ensure commands are safe, reversible, and consistent across the experience.</li>
<li>Test with diverse accents to improve recognition accuracy.</li>
<li>Provide users with a clear overview of available voice commands.</li>
</ul>
</td>
<td>
<ul>
<li>Use similar-sounding or overly complex phrases that cause confusion.</li>
<li>Keep commands active when they’re not relevant to the current context.</li>
<li>Override or conflict with system-level voice commands.</li>
<li>Assume voice alone is sufficient—combine with other input methods when needed.</li>
</ul>
</td>
</tr>
</table>

Voice input is a common interaction method in XR applications, particularly in situations where users need to interact with the system without using their hands. This can be especially beneficial in scenarios that require multitasking, physical movement, or sustained manual interaction, such as training, maintenance, or collaborative tasks. Voice-based interactions often enable faster and more natural communication, which can improve efficiency and enhance the overall sense of immersion. Most of the following guidelines have been taken from Microsoft’s AR Design guidelines regarding the Hololens \[[34](References.md)\].

* **Use concise commands:** When possible, choose keywords of two or more syllables. One-syllable words tend to use different vowel sounds when spoken by persons of different accents. Example: "Play video" is better than "Play the currently selected video"
* **Use simple vocabulary:** Simpler vocabulary is easier to say, more rememberable and can cause fewer mistakes. Example: "Show note" is better than "Show placard"
* **Make sure commands are non-destructive:** Make sure any speech command actions are non-destructive and can easily be undone in case another person speaking near the user accidentally triggers a command.
* **Avoid similar sounding commands:** Avoid registering multiple speech commands that sound similar. Example: "Show more" and "Show store" can be similar sounding.
* **Unregister your app when not it uses:** When your app is not in a state in which a particular speech command is valid, consider unregistering it so that other commands are not confused for that one.
* **Test with different accents:** Many of the users are not native English speaker and some words might not be registered correctly due to various accents. Thus, test your app with users of different accents.
* **Maintain voice command consistency:** If "Go back" goes to the previous page, maintain this behaviour in your applications.
* **Avoid using system commands:** Some systems might already have preregistered voice commands. These commands are reserved for the system, so avoid using them for interactions that do not align with their intended purpose in your applications.
* **Provide Access to Commands Overview:** It will be difficult for users to remember all the voice commands from the beginning no matter how intuitive they are. The user should have access to a list of possible voice commands. This can also be combined with other inputs such as gaze to offer voice commands only for the objects the user is interested in.