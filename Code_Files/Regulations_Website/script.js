function showDropdown(regulation) {
    document.getElementById('info-text').style.display = 'none';
    document.getElementById('dropdown-container').style.display = 'block';
    document.getElementById('content-display').innerHTML = ''; // Clear previous content
    document.getElementById('topic-dropdown').selectedIndex = 0; // Reset dropdown

    // You can customize the prompt text based on the regulation if needed
    document.getElementById('dropdown-container').innerHTML = `
        <label for="topic-dropdown">Choose a topic for ${regulation.toUpperCase()}:</label>
        <select id="topic-dropdown" onchange="showContent('${regulation}', this.value)">
            <option value="">Select...</option>
            <option value="scope">Scope</option>
            <option value="objective">Objective</option>
            <option value="rights-individuals">Rights of Individuals</option>
            <option value="rights-organizations">Rights of Organizations</option>
            <option value="consequences">Consequences</option>
        </select>
    `;
}

function showContent(regulation, topic) {
    let content = '';
    let header = '';
    switch (topic) {
        case 'scope':
            content = `${regulation.toUpperCase()} Scope: ...`; // Add specific content
            header = 'Scope';
            break;
        case 'objective':
            content = `${regulation.toUpperCase()} Objective: ...`; // Add specific content
            header = 'Objective';
            break;
        case 'rights-individuals':
            content = `${regulation.toUpperCase()} Rights of Individuals: ...`; // Add specific content
            header = 'Rights of Individuals';
            break;
        case 'rights-organizations':
            content = `${regulation.toUpperCase()} Rights of Organizations: ...`; // Add specific content
            header = 'Rights of Organizations';
            break;
        case 'consequences':
            content = `${regulation.toUpperCase()} Consequences: ...`; // Add specific content
            header = 'Consequences';
            break;
        default:
            content = 'Select a topic from the dropdown';
            header = '';
            break;
    }
    document.getElementById('content-display').innerHTML = `<h2>${header}</h2><p>${content}</p>`;
    document.getElementById('dropdown-container').style.display = 'none';
    document.getElementById('info-text').style.display = 'none';
}
