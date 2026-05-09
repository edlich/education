# Design System Strategy: The Curated Mind

## 1. Overview & Creative North Star
This design system is built to transform a standard productivity tool into a high-end digital sanctuary. Our Creative North Star is **"The Curated Mind."** 

Unlike traditional productivity apps that feel like cluttered spreadsheets, this system treats information as an editorial masterpiece. We move beyond the "template" look by utilizing intentional asymmetry, expansive breathing room (whitespace), and a high-contrast typography scale. We favor tonal depth over structural lines, creating an environment that feels organized, quiet, and authoritative. Every interaction should feel like turning the page of a premium botanical or architectural journal.

## 2. Colors: Muted Organic Sophistication
The palette is rooted in a "Moss & Mineral" aesthetic. We use mid-tone botanical greens for focus and warm, mineral grays for grounding the interface.

### Color Roles
*   **Primary (`#488358`)**: Our "Moss." Used for key actions, brand identity, and focal points.
*   **Secondary (`#657d68`)**: Our "Slate." Used for secondary UI elements that need to feel integrated with the natural palette.
*   **Tertiary (`#8a4554`)**: Our "Bloom." A dusty accent used for highlights, badges, or specific decorative callouts.
*   **Neutral / Background (`#757873`)**: Our "Mineral." A warm, medium-toned base that provides a sophisticated, non-glaring backdrop for content.

### The "No-Line" Rule
**Explicit Instruction:** Do not use 1px solid borders to define sections or containers. Traditional borders create visual noise. Boundaries must be defined solely through:
1.  **Background Shifts:** Placing a `surface-container-low` element against a `surface` (`#757873`) background.
2.  **Intentional Negative Space:** Using large, consistent gaps to imply grouping.

### Surface Hierarchy & Nesting
Treat the UI as a series of stacked, physical layers. Use the surface-container tiers to create "nested" depth:
*   **Base Layer:** `surface` (`#757873`)
*   **Section Layer:** `surface-container-low`
*   **Interactive Cards:** `surface-container-lowest` 

### The "Glass & Gradient" Rule
For floating panels (sidebars or command palettes), use **Glassmorphism**. Apply `surface-container-lowest` at 70% opacity with a `backdrop-blur` of 20px. 
*   **Signature Texture:** For primary CTAs, apply a subtle linear gradient from `primary` (`#488358`) to a slightly deeper tonal variant at a 135-degree angle. This adds a "silk-finish" depth that flat color cannot replicate.

## 3. Typography: Editorial Precision
We use a duo-font system to balance character with utility.

*   **Display & Headlines (Manrope):** A modern, geometric sans-serif used for large-scale "Editorial" moments. 
    *   *Usage:* Use `display-lg` (3.5rem) with tight letter-spacing (-0.02em) for dashboard welcomes or empty states to create a high-end feel.
*   **Body & Labels (Inter):** A highly legible, neutral sans-serif for productivity.
    *   *Usage:* Use `body-md` (0.875rem) for most content to maximize information density without sacrificing clarity.
*   **The Contrast Rule:** Pair `headline-sm` in Manrope with `label-md` in Inter (all caps, letter-spaced) for a sophisticated metadata hierarchy.

## 4. Elevation & Depth: Tonal Layering
Depth is achieved through "Tonal Layering" rather than traditional heavy shadows.

*   **The Layering Principle:** Place a `surface-container-lowest` card on a `surface-container-low` section. This creates a soft, natural "lift" that feels architectural rather than digital.
*   **Ambient Shadows:** For elements that must float (modals, dropdowns), use a custom ambient shadow. 
    *   *Specs:* `0px 24px 48px -12px`. Color: `on-surface` at **6% opacity**. This mimics natural ambient light against the mineral background.
*   **The "Ghost Border":** If a container requires a boundary for accessibility, use the `outline-variant` at **15% opacity**. It should be felt, not seen.
*   **Interactivity:** On hover, transition an element from `surface-container-lowest` to `surface-bright`. This subtle shift in luminosity is more sophisticated than a color change.

## 5. Components

### Buttons
*   **Primary:** `primary` background, `on_primary` text. Radius: `1` (subtle rounding). No shadow.
*   **Secondary:** `surface-container-high` background. No border. Radius: `1`.
*   **Tertiary:** Ghost style. No background. Use `primary` text with an underline that only appears on hover.

### Cards & Knowledge Blocks
*   **Rule:** Forbid divider lines. 
*   **Structure:** Use `surface-container-low` for the card body. Use a `primary` vertical accent (2px wide) on the far left to indicate "Active" or "Selected" states.
*   **Spacing:** Use normal spacing (Level 2) to ensure content feels "curated" and breathable.

### Input Fields
*   **Style:** Minimalist. `surface-container-highest` background, no border. On focus, transition the background to `surface-container-lowest` and apply a 1px "Ghost Border" using the `surface_tint` at 40% opacity.

### Navigation (The Sidebar)
*   Use a "soft-bleed" approach. The sidebar should be `surface-container-low` with no hard vertical line separating it from the main content. The content should simply "begin" where the sidebar ends.

## 6. Do's and Don'ts

### Do
*   **Do** use asymmetrical layouts (e.g., a wide left margin for titles, narrow right columns for metadata).
*   **Do** use the Moss Green (`primary`) and Slate (`secondary`) for sophisticated tonal combinations.
*   **Do** prioritize vertical rhythm over horizontal dividers.
*   **Do** use `body-sm` for legal or secondary text to keep the UI feeling "clean."

### Don't
*   **Don't** use 100% black or white. Always use the established palette of greens and mineral grays.
*   **Don't** use high roundedness. Stick to the `1` (subtle) setting for a more professional, structured look.
*   **Don't** use high-contrast shadows. If the shadow is clearly visible, it's too dark.
*   **Don't** crowd the interface. If in doubt, increase the `surface` area to respect the "spacing: 2" baseline.
