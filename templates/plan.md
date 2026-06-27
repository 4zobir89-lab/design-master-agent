# Plan — {{project_name}}

## Workflow State
- **Mode**: design-master
- **Status**: Planning
- **Last Updated**: {{date}}

## Target Scope
{{scope_description}}

## Implementation Order
1. Design tokens (CSS :root)
2. Typography scale
3. Layout grid
4. Section HTML structure
5. CSS for all components
6. GSAP timeline for hero
7. ScrollTrigger for section reveals
8. ScrollTrigger.batch for grids
9. Interactive elements (filter, carousel, magnetic, cursor)
10. Theme toggle (if dual mode)
11. Lenis smooth scroll
12. Reduced-motion fallbacks
13. Mobile downgrades
14. ARIA labels and keyboard nav

## Recipes By Section
| # | Section | Recipe | Objective | Motion | Mobile | Status |
|---|---------|--------|-----------|--------|--------|--------|
| 1 | {{section_1}} | {{recipe_1}} | {{objective_1}} | {{motion_1}} | {{mobile_1}} | Planned |
| 2 | {{section_2}} | {{recipe_2}} | {{objective_2}} | {{motion_2}} | {{mobile_2}} | Planned |
| ... | ... | ... | ... | ... | ... | ... |

## Detected Project Signals
- **Direction**: {{rtl_or_ltr}}
- **Brand**: {{palette_summary}}
- **Typography**: {{fonts_summary}}
- **Tone**: {{tone_summary}}
- **Constraints**: {{constraints_list}}

## Validation Checklist
- [ ] Only transform and opacity animated
- [ ] ScrollTrigger.batch used for repeated elements
- [ ] < 20 active ScrollTriggers per page
- [ ] Mobile: no parallax, no pinning, simplified animations
- [ ] prefers-reduced-motion respected
- [ ] CSS initial states prevent FOUC
- [ ] Above-fold animates on load, below-fold on scroll
- [ ] Unused GSAP plugins not imported
- [ ] ScrollTrigger.refresh() called after load
