/**
 * Foresight Scenarios Toolkit - Interactive Application
 * Handles tab navigation, matrix interactions, and scenario modals
 */

// Scenario Data
const scenarios = {
    'coordinated-caution': {
        quadrant: 'Incremental Capability + Harmonized Regulation',
        quadrantClass: 'q1',
        title: 'Coordinated Caution',
        tagline: '"The world agrees on AI guardrails before the horse leaves the barn."',
        narrative: `By 2027, frontier AI capabilities have continued advancing but without the dramatic leaps some predicted. Scaling laws hit diminishing returns around 2026, and while AI systems are more capable than GPT-4, they remain tools that augment rather than replace human judgment in high-stakes domains.

This breathing room allowed international coordination to mature. The EU AI Act served as a template, and after bruising negotiations, the US, EU, and key Asian economies reached a mutual recognition agreement on AI safety standards in 2028. China remains outside the framework but implements comparable domestic requirements for systems serving its market.`,
        features: [
            'International AI Safety Board (modeled on IAEA) established',
            'Tiered licensing for high-capability models',
            'Mandatory pre-deployment safety evaluations for frontier systems',
            'Harmonized incident reporting across jurisdictions',
            'Compute thresholds trigger regulatory scrutiny'
        ],
        winners: [
            'Large incumbent AI labs (compliance moat)',
            'GRC/compliance professionals',
            'Risk-averse enterprises',
            'International institutions'
        ],
        losers: [
            'Startups (regulatory burden)',
            'Open-source purists',
            'Move-fast cultures',
            'National sovereignty advocates'
        ],
        implications: [
            '<strong>For AI developers:</strong> Invest heavily in compliance infrastructure; safety becomes competitive advantage',
            '<strong>For deployers:</strong> Clearer compliance pathway but higher costs',
            '<strong>For policymakers:</strong> Template exists; focus on implementation',
            '<strong>For civil society:</strong> Seat at the table through formal processes'
        ]
    },
    'emergency-coordination': {
        quadrant: 'Discontinuous Capability + Harmonized Regulation',
        quadrantClass: 'q2',
        title: 'Emergency Coordination',
        tagline: '"A crisis forces cooperation that seemed impossible."',
        narrative: `In late 2026, a frontier lab achieves a significant capability discontinuity—an AI system demonstrating genuine recursive self-improvement and autonomous goal pursuit. The initial deployment causes no catastrophe, but the implications are immediately clear to technical experts and policymakers alike.

Faced with an obvious and present risk, geopolitical rivals find unprecedented common ground. Within 18 months, emergency international frameworks emerge—imperfect and contested, but functional. The memory of near-catastrophe drives sustained cooperation despite ongoing tensions.`,
        features: [
            'Mandatory compute reporting and controls globally',
            'International inspection regime for frontier facilities',
            'Shared "circuit breaker" protocols for concerning capabilities',
            'Aggressive restrictions on autonomous agentic deployment',
            'Massive public investment in AI safety research'
        ],
        winners: [
            'AI safety researchers',
            'Governments (expanded authority)',
            'Defensive/security applications',
            'Incumbent frontier labs'
        ],
        losers: [
            '"Move fast" advocates',
            'Lab autonomy',
            'Consumer AI applications (slowed)',
            'Challenger labs'
        ],
        implications: [
            '<strong>For AI developers:</strong> Safety-first is non-negotiable; expect intensive oversight',
            '<strong>For deployers:</strong> Limited access to frontier capabilities; focus on narrow applications',
            '<strong>For policymakers:</strong> Crisis creates mandate but implementation is chaotic',
            '<strong>For civil society:</strong> Urgency creates openings for influence'
        ]
    },
    'patchwork-progress': {
        quadrant: 'Incremental Capability + Fragmented Regulation',
        quadrantClass: 'q3',
        title: 'Patchwork Progress',
        tagline: '"AI advances steadily while governance remains a mess."',
        narrative: `AI capabilities continue their incremental advance through 2030, but international governance coordination never materializes. The EU enforces the AI Act strictly, the US maintains sector-specific voluntary frameworks, China pursues state-directed development, and emerging markets vary widely.

Companies adapt to this patchwork, building compliance capabilities for key markets while taking advantage of regulatory arbitrage where possible. Progress continues but is slowed by friction; no catastrophic failures occur, but neither does coherent global governance.`,
        features: [
            'EU as de facto global standard for companies wanting market access',
            'US innovation hub with minimal federal requirements',
            'Compliance complexity as major business cost',
            '"Good enough" safety through market pressure and liability risk',
            'Regulatory arbitrage for some applications'
        ],
        winners: [
            'Large multinationals (compliance scale)',
            'Legal/compliance industry',
            'Permissive jurisdictions',
            'Pragmatic deployers'
        ],
        losers: [
            'SMEs (compliance burden)',
            'Efficiency advocates',
            'Strict jurisdictions (some)',
            'Idealists (safety or innovation)'
        ],
        implications: [
            '<strong>For AI developers:</strong> Build modular compliance; design for strictest market',
            '<strong>For deployers:</strong> Jurisdiction shopping is real but limited',
            '<strong>For policymakers:</strong> Focus on domestic frameworks; international coordination is aspirational',
            '<strong>For civil society:</strong> National-level advocacy most effective'
        ]
    },
    'fragmented-scramble': {
        quadrant: 'Discontinuous Capability + Fragmented Regulation',
        quadrantClass: 'q4',
        title: 'Fragmented Scramble',
        tagline: '"Transformative AI arrives in a world unprepared to govern it."',
        narrative: `A discontinuous capability advance occurs—but unlike the Emergency Coordination scenario, no coordinated response emerges. Geopolitical competition intensifies rather than abates; nations rush to secure advantage rather than cooperate on safety. The US and China view frontier AI as decisive for strategic competition and resist any constraints.

The result is a dangerous period of rapid capability deployment with minimal guardrails. Some nations attempt strict controls but face circumvention. Others embrace unrestricted development. The international system fragments further under pressure.`,
        features: [
            'AI arms race dynamics dominate',
            'Regulatory arbitrage at massive scale',
            'Safety concerns subordinated to competitive pressures',
            'High variance in outcomes—some beneficial, some harmful deployments',
            'Crisis-driven ad hoc responses rather than systematic governance'
        ],
        winners: [
            'First movers (short term)',
            'Permissive jurisdictions',
            'State-aligned actors',
            'Defense/intelligence'
        ],
        losers: [
            'Everyone (long term risk)',
            'Cautious jurisdictions',
            'Independent actors',
            'Civil society'
        ],
        implications: [
            '<strong>For AI developers:</strong> Speed dominates; safety is afterthought',
            '<strong>For deployers:</strong> High reward, high risk; prepare for volatility',
            '<strong>For policymakers:</strong> National security frame dominates; governance is reactive',
            '<strong>For civil society:</strong> Limited influence; focus on harm mitigation'
        ]
    }
};

// DOM Elements
const tabs = document.querySelectorAll('.tab');
const tabContents = document.querySelectorAll('.tab-content');
const quadrants = document.querySelectorAll('.quadrant');
const modal = document.getElementById('scenario-modal');
const modalClose = document.querySelector('.modal-close');

// Tab Navigation
tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        // Remove active class from all tabs and contents
        tabs.forEach(t => t.classList.remove('active'));
        tabContents.forEach(c => c.classList.remove('active'));

        // Add active class to clicked tab and corresponding content
        tab.classList.add('active');
        const tabId = tab.getAttribute('data-tab');
        document.getElementById(tabId).classList.add('active');
    });
});

// Quadrant Click - Open Modal
quadrants.forEach(quadrant => {
    quadrant.addEventListener('click', () => {
        const scenarioId = quadrant.getAttribute('data-scenario');
        openModal(scenarioId);
    });
});

// Modal Functions
function openModal(scenarioId) {
    const scenario = scenarios[scenarioId];
    if (!scenario) return;

    // Populate modal content
    const quadrantBadge = modal.querySelector('.modal-quadrant');
    quadrantBadge.textContent = scenario.quadrant;
    quadrantBadge.className = `modal-quadrant ${scenario.quadrantClass}-bg`;

    modal.querySelector('.modal-title').textContent = scenario.title;
    modal.querySelector('.modal-tagline').textContent = scenario.tagline;
    modal.querySelector('.modal-narrative').innerHTML = scenario.narrative.replace(/\n\n/g, '</p><p>');

    // Features
    const featuresList = modal.querySelector('.modal-features');
    featuresList.innerHTML = scenario.features.map(f => `<li>${f}</li>`).join('');

    // Winners
    const winnersList = modal.querySelector('.modal-winners');
    winnersList.innerHTML = scenario.winners.map(w => `<li>${w}</li>`).join('');

    // Losers
    const losersList = modal.querySelector('.modal-losers');
    losersList.innerHTML = scenario.losers.map(l => `<li>${l}</li>`).join('');

    // Implications
    const implList = modal.querySelector('.modal-implications');
    implList.innerHTML = scenario.implications.map(i => `<li>${i}</li>`).join('');

    // Show modal
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    modal.classList.remove('active');
    document.body.style.overflow = '';
}

// Modal Close Events
modalClose.addEventListener('click', closeModal);

modal.addEventListener('click', (e) => {
    if (e.target === modal) {
        closeModal();
    }
});

document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('active')) {
        closeModal();
    }
});

// Smooth scroll for any anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add subtle animation to probability bars on scroll
function animateProbBars() {
    const bars = document.querySelectorAll('.bar-fill');
    bars.forEach(bar => {
        const width = bar.style.width;
        bar.style.width = '0';
        setTimeout(() => {
            bar.style.width = width;
        }, 100);
    });
}

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.2,
    rootMargin: '0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            if (entry.target.classList.contains('probability-summary')) {
                animateProbBars();
            }
        }
    });
}, observerOptions);

// Observe elements for scroll animations
document.querySelectorAll('.probability-summary, .driver-card, .process-step').forEach(el => {
    observer.observe(el);
});

// Add keyboard navigation for quadrants
quadrants.forEach((quadrant, index) => {
    quadrant.setAttribute('tabindex', '0');
    quadrant.setAttribute('role', 'button');
    quadrant.setAttribute('aria-label', `View ${quadrant.querySelector('h3').textContent} scenario`);

    quadrant.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            const scenarioId = quadrant.getAttribute('data-scenario');
            openModal(scenarioId);
        }
    });
});

// Console welcome message
console.log('%cForesight Scenarios Toolkit', 'font-size: 20px; font-weight: bold; color: #1a365d;');
console.log('%cInteractive AI Governance Scenarios 2024-2030', 'font-size: 14px; color: #4a5568;');
console.log('Learn more: https://github.com/delschlangen/foresight-scenarios-toolkit');
