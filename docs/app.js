/**
 * Foresight Scenarios Toolkit - Interactive Application
 * Tabs (ARIA pattern, deep-linkable), accessible scenario modal, scroll animations.
 */

// ---------------------------------------------------------------------------
// Scenario data (mirrors framework/scenarios.md)
// ---------------------------------------------------------------------------

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

// ---------------------------------------------------------------------------
// Tabs: WAI-ARIA tabs pattern with hash deep-linking
// ---------------------------------------------------------------------------

const tabs = Array.from(document.querySelectorAll('.tab[data-tab]'));
const tabPanels = Array.from(document.querySelectorAll('.tab-content'));
const tabIds = tabs.map(tab => tab.dataset.tab);
const tabsContainer = document.querySelector('.tabs-container');

function activateTab(id, options = {}) {
    const { updateHash = true, scroll = false } = options;
    if (!tabIds.includes(id)) return false;

    tabs.forEach(tab => {
        const active = tab.dataset.tab === id;
        tab.classList.toggle('active', active);
        tab.setAttribute('aria-selected', String(active));
        tab.setAttribute('tabindex', active ? '0' : '-1');
    });
    tabPanels.forEach(panel => panel.classList.toggle('active', panel.id === id));

    if (updateHash && location.hash !== '#' + id) {
        history.replaceState(null, '', '#' + id);
    }
    if (scroll && tabsContainer) {
        tabsContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
    return true;
}

tabs.forEach(tab => {
    tab.addEventListener('click', () => activateTab(tab.dataset.tab));

    tab.addEventListener('keydown', event => {
        const index = tabs.indexOf(tab);
        let next = null;
        if (event.key === 'ArrowRight') next = tabs[(index + 1) % tabs.length];
        if (event.key === 'ArrowLeft') next = tabs[(index - 1 + tabs.length) % tabs.length];
        if (event.key === 'Home') next = tabs[0];
        if (event.key === 'End') next = tabs[tabs.length - 1];
        if (next) {
            event.preventDefault();
            activateTab(next.dataset.tab);
            next.focus();
        }
    });
});

function tabFromHash() {
    return decodeURIComponent(location.hash.replace(/^#/, ''));
}

if (!activateTab(tabFromHash(), { updateHash: false })) {
    activateTab(tabIds[0], { updateHash: false });
}

window.addEventListener('hashchange', () => {
    activateTab(tabFromHash(), { updateHash: false });
});

// In-page links: a link to a tab id switches tabs; any other anchor scrolls smoothly.
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', event => {
        const id = anchor.getAttribute('href').slice(1);
        if (tabIds.includes(id)) {
            event.preventDefault();
            activateTab(id, { scroll: true });
            return;
        }
        const target = document.getElementById(id);
        if (target) {
            event.preventDefault();
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});

// ---------------------------------------------------------------------------
// Scenario modal: dialog semantics, focus trap, focus restore
// ---------------------------------------------------------------------------

const modal = document.getElementById('scenario-modal');
const modalContent = modal.querySelector('.modal-content');
const modalClose = modal.querySelector('.modal-close');
const quadrants = document.querySelectorAll('.quadrant');
const FOCUSABLE = 'a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])';
let modalOpener = null;

function escapeHtml(text) {
    return text
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;');
}

function openModal(scenarioId) {
    const scenario = scenarios[scenarioId];
    if (!scenario) return;

    const quadrantBadge = modal.querySelector('.modal-quadrant');
    quadrantBadge.textContent = scenario.quadrant;
    quadrantBadge.className = `modal-quadrant ${scenario.quadrantClass}-bg`;

    modal.querySelector('.modal-title').textContent = scenario.title;
    modal.querySelector('.modal-tagline').textContent = scenario.tagline;
    modal.querySelector('.modal-narrative').innerHTML = scenario.narrative
        .split(/\n\s*\n/)
        .map(paragraph => `<p>${escapeHtml(paragraph)}</p>`)
        .join('');

    modal.querySelector('.modal-features').innerHTML = scenario.features.map(f => `<li>${escapeHtml(f)}</li>`).join('');
    modal.querySelector('.modal-winners').innerHTML = scenario.winners.map(w => `<li>${escapeHtml(w)}</li>`).join('');
    modal.querySelector('.modal-losers').innerHTML = scenario.losers.map(l => `<li>${escapeHtml(l)}</li>`).join('');
    modal.querySelector('.modal-implications').innerHTML = scenario.implications.map(i => `<li>${i}</li>`).join('');

    modalOpener = document.activeElement;
    modal.classList.add('active');
    modal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    modalContent.scrollTop = 0;
    modalClose.focus();
}

function closeModal() {
    modal.classList.remove('active');
    modal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    if (modalOpener && typeof modalOpener.focus === 'function') {
        modalOpener.focus();
    }
    modalOpener = null;
}

modalClose.addEventListener('click', closeModal);

modal.addEventListener('click', event => {
    if (event.target === modal) closeModal();
});

document.addEventListener('keydown', event => {
    if (!modal.classList.contains('active')) return;

    if (event.key === 'Escape') {
        closeModal();
        return;
    }

    if (event.key === 'Tab') {
        const focusable = Array.from(modalContent.querySelectorAll(FOCUSABLE))
            .filter(element => element.offsetParent !== null);
        if (focusable.length === 0) {
            event.preventDefault();
            return;
        }
        const first = focusable[0];
        const last = focusable[focusable.length - 1];
        if (event.shiftKey && document.activeElement === first) {
            event.preventDefault();
            last.focus();
        } else if (!event.shiftKey && document.activeElement === last) {
            event.preventDefault();
            first.focus();
        }
    }
});

// Quadrants: clickable, keyboard-operable buttons that open the dialog
quadrants.forEach(quadrant => {
    const name = quadrant.querySelector('h3').textContent;
    quadrant.setAttribute('tabindex', '0');
    quadrant.setAttribute('role', 'button');
    quadrant.setAttribute('aria-haspopup', 'dialog');
    quadrant.setAttribute('aria-label', `View ${name} scenario details`);

    quadrant.addEventListener('click', () => openModal(quadrant.dataset.scenario));
    quadrant.addEventListener('keydown', event => {
        if (event.key === 'Enter' || event.key === ' ') {
            event.preventDefault();
            openModal(quadrant.dataset.scenario);
        }
    });
});

// ---------------------------------------------------------------------------
// Scroll animations
// ---------------------------------------------------------------------------

function animateProbBars() {
    document.querySelectorAll('.bar-fill').forEach(bar => {
        const width = bar.style.width;
        bar.style.width = '0';
        setTimeout(() => { bar.style.width = width; }, 100);
    });
}

const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            if (entry.target.classList.contains('probability-summary')) {
                animateProbBars();
            }
        }
    });
}, { threshold: 0.2, rootMargin: '0px' });

document.querySelectorAll('.probability-summary, .driver-card, .process-step, .toolkit-card').forEach(element => {
    observer.observe(element);
});

// ---------------------------------------------------------------------------
console.log('%cForesight Scenarios Toolkit', 'font-size: 20px; font-weight: bold; color: #1a365d;');
console.log('%cWorked example: AI governance scenarios (Q4 2024 baseline)', 'font-size: 14px; color: #4a5568;');
console.log('Build your own: https://github.com/delschlangen/foresight-scenarios-toolkit');
