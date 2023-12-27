// // Function to check if the user is likely accessing from a system user
// function checkSystemUser() {
//     var userAgent = navigator.userAgent.toLowerCase();
    
//     // List of keywords to check for system users
//     var systemKeywords = ['windows', 'macintosh', 'linux', 'x11'];
    
//     // Loop through the systemKeywords array to check if any keyword matches with the user agent
//     for (var i = 0; i < systemKeywords.length; i++) {
//         if (userAgent.indexOf(systemKeywords[i]) > -1) {
//             return true; // User is likely accessing from a system user
//         }
//     }
    
//     // Additional checks based on other properties can be added here if needed
//     // For example, you can check if the user has certain plugins enabled, screen size, etc.
    
//     return false; // User is not a system user (mobile or other devices)
// }

// // Check system user on page load
// window.onload = function() {
//     if (checkSystemUser()) {
//         alert('دسترسی به این صفحه تنها از طریق تلغن همراه امکان پذیر است.');
//         // Redirect or perform other actions for system users
//         window.location.href = 'https://virasmart.co'; // Redirect to another site or show a message
//     }
// };