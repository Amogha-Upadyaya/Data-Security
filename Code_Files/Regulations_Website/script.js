function showDropdown(regulation) {
    document.getElementById('info-text').style.display = 'none';
    document.getElementById('dropdown-container').style.display = 'block';
    document.getElementById('content-display').innerHTML = ''; // Clear previous content
    document.getElementById('topic-dropdown').selectedIndex = 0; // Reset dropdown

    // Customize the prompt text based on the regulation if needed
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
            content = getScopeContent(regulation);
            header = 'Scope';
            break;
        case 'objective':
            content = getObjectiveContent(regulation);
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

function getScopeContent(regulation) {
    switch (regulation) {
        case 'gdpr':
            return "General Data Protection Regulation (GDPR): Applies to all organizations operating within the European Union (EU) and to those outside the EU if they offer goods or services to, or monitor the behavior of, EU residents. It governs the collection, processing, and storage of personal data, providing individuals with rights such as data access, correction, and deletion.";
        case 'hipaa':
            return "Health Insurance Portability and Accountability Act (HIPAA): Applies to healthcare providers, health plans, and healthcare clearinghouses in the United States that handle protected health information (PHI). It mandates the safeguarding of PHI through administrative, physical, and technical safeguards.";
        case 'pdpa':
            return "Personal Data Protection Act (PDPA): Singaporean law that regulates the collection, use, and disclosure of personal data by organizations. It grants individuals rights over their data and imposes obligations on organizations to protect and manage personal data appropriately.";
        case 'lgpd':
            return "Brazilian General Data Protection Law (LGPD): Applies to any entity processing personal data in Brazil, regardless of where the entity is located. It provides data protection rights to individuals and imposes requirements on data controllers and processors, including obtaining consent and ensuring data security.";
        case 'ccpa':
            return "California Consumer Privacy Act (CCPA): Applies to for-profit businesses operating in California that meet certain thresholds (e.g., annual gross revenues over $25 million). It gives California residents rights regarding their personal data, such as the right to access, delete, and opt out of the sale of their data.";
        case 'pcidss':
            return "Payment Card Industry Data Security Standard (PCI DSS): Applies to any organization that handles payment card information, including merchants and service providers. It sets requirements for securing cardholder data through various controls, including encryption, access controls, and regular security testing.";
        case 'china-cyber-law':
            return "China's Cybersecurity Law: Applies to network operators and operators of critical information infrastructure in China. It focuses on ensuring cybersecurity, protecting personal information, and maintaining data security through regulations on data localization, network security, and incident reporting.";
        case 'iso27001':
            return "ISO/IEC 27001: A standard providing a framework for managing information security risks, including requirements for establishing, implementing, maintaining, and continually improving an information security management system (ISMS).";
        case 'nis-directive':
            return "Network and Information Systems (NIS) Directive: Applies to operators of essential services and digital service providers within the EU. It aims to enhance the overall cybersecurity posture by setting requirements for risk management, incident reporting, and cooperation among member states.";
        case 'fisma':
            return "Federal Information Security Management Act (FISMA): Applies to U.S. federal agencies, as well as contractors and organizations that handle federal information systems. It mandates the implementation of information security programs, including risk management and security controls, to protect federal information and systems.";
        default:
            return 'Select a regulation to view its scope.';
    }
}

function getObjectiveContent(regulation) {
    switch (regulation) {
        case 'gdpr':
            return "To enhance data protection and privacy for individuals within the European Union and the European Economic Area. It aims to give individuals more control over their personal data and to standardize data protection laws across Europe.";
        case 'hipaa':
            return "To protect the privacy and security of individuals' medical information and to ensure the confidentiality and integrity of health information transmitted electronically.";
        case 'pdpa':
            return "To govern the collection, use, and disclosure of personal data in Singapore, ensuring that individuals' personal data is handled responsibly and in compliance with privacy principles.";
        case 'lgpd':
            return "To regulate the processing of personal data in Brazil, ensuring privacy and protection of individuals' personal information and establishing guidelines for data collection, use, and sharing.";
        case 'ccpa':
            return "To provide California residents with greater transparency and control over their personal data, including the right to know what personal information is being collected, the right to request deletion, and the right to opt-out of data sharing.";
        case 'pcidss':
            return "To enhance the security of payment card transactions by establishing a set of standards designed to protect cardholder data and prevent data breaches in the payment card industry.";
        case 'china-cyber-law':
            return "To strengthen cybersecurity and protect personal information and critical information infrastructure in China. It aims to ensure the security and stability of the internet and information systems.";
        case 'iso27001':
            return "To provide a framework for establishing, implementing, maintaining, and continually improving an information security management system (ISMS) to protect sensitive information and manage security risks.";
        case 'nis-directive':
            return "To improve the cybersecurity of network and information systems across the European Union, focusing on essential services and digital service providers to enhance overall resilience and response to cyber incidents.";
        case 'fisma':
            return "To provide a comprehensive framework for ensuring the effectiveness of information security controls over federal information systems in the United States. It aims to protect the confidentiality, integrity, and availability of federal information systems.";
        default:
            return 'Select a regulation to view its objective.';
    }
}
