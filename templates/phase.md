# Phase P{{number}} — {{section_name}}

## Scope
- **Page**: {{page_name}}
- **Section**: {{section_name}}
- **Recipe**: {{recipe_name}}

## Objective
{{objective_description}}

## Tasks
- [ ] Read phase file
- [ ] Write semantic HTML using seed classes
- [ ] Write section-specific CSS (additions only, no token overrides)
- [ ] Write section JS using recipe
- [ ] Add ARIA attributes
- [ ] Verify mobile downgrade
- [ ] Update phase status

## HTML Structure
```html
<section id="{{section_id}}" data-bg="{{bg_color}}">
  <div class="container container-wide">
    <!-- ... -->
  </div>
</section>
```

## CSS Tokens Used
- `var(--bg)` — background
- `var(--fg)` — foreground text
- `var(--accent)` — accent (≤ 2 visible uses per screen)
- `var(--space-*)` — spacing scale
- `var(--font-display-ar)` / `var(--font-body-ar)` — typography

## Animation Recipe
```js
// {{recipe_name}}
gsap.from(".{{section_id}} .element", {
  opacity: 0, y: 50, duration: 0.8, ease: "power3.out",
  scrollTrigger: {
    trigger: ".{{section_id}}",
    start: "top 80%",
    toggleActions: "play none none none",
  },
});
```

## Validation
- [ ] Reduced Motion: elements visible immediately, no transforms
- [ ] Mobile Downgrade: {{mobile_downgrade_description}}
- [ ] Only transform/opacity animated (no width/height/top/left)
- [ ] ARIA: {{aria_requirements}}
- [ ] Color: var(--accent) used ≤ 2 times visibly
- [ ] Touch targets ≥ 24×24

## Status: Planned → In Progress → Done
