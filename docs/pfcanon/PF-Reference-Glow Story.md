# **What Glow is (product story)**

**Glow is a connection service** for friendship, love, collaboration, and creative work. People can start from **optional presets** (templates) **or** set their own **priorities/weights** across the ten categories. Those priorities guide who appears in the app. It’s powered by Human Design mechanics, but the user-facing language stays plain—no HD jargon.

**Key rule set**

* Every user chooses a **\#1 category** (their top priority) and sets **weights** (0–100) for all ten categories.

* **Presets are optional**: they’re just starting templates you can tweak—or skip entirely and set weights manually.

* If you set a **weight \= 0** for a category, you **won’t be shown people** who have that category as their **\#1** (the zero-weight rule).

# **How people actually use it (user story)**

## **A) Primary UX — Swiping**

1. **Intent & weights:** Either pick a preset **or** manually set your \#1 and weights.

2. **Swipe feed:** You get an ongoing, natural-feeling stream of profiles. It looks casual, but it’s guided by your priorities and the other person’s \#1.

3. **Open a card:**

   * At the top: the **band for your \#1 category** (the one you care about most).

   * Below: the **ten categories**, each with **two narratives**:

     * a **personal** line (addressed to **you** about this pair), and

     * a **shared** line (speaking to **both** of you together).

   * A **Download JSON** button for admins/testers.

4. **Act:** Like / pass / start a conversation. Adjust your weights anytime to change who you see.

## **B) Optional — Daily set**

* If enabled, you can also receive a small, paced **daily set** that respects your weights and avoids repeats. Swiping remains the main experience.

## **C) Direct compare (for testing or curiosity)**

* Pick/paste two profiles, press **Compare**, and see the same one-page result: **per-category bands** plus **two narratives per category**, with your **\#1** shown first.

# **What the engine actually returns (clear and minimal)**

For any **viewer** and a **candidate**:

* **Per-category number** (0–100) — used for admin/testing and tuning; not shown to end users initially.

* **Per-category band** (Cool / Open / Warm / Glow) — the user-visible signal.

* **Two narrative keys per category** — `{personal_key, shared_key}` used to render curated copy.

* A compact **JSON** bundling the above (plus IDs and minimal metadata).

**End-user view:** bands \+ narratives (numbers hidden).  
 **Admin/tester view:** numbers visible for tuning thresholds and band mapping.

# **How “who you meet” is chosen (swipe feed logic, plain English)**

* Build a **candidate pool** that respects **your weights** and the **zero-weight rule**.

* Score candidates using your **weighted categories**; the other person’s \#1 matters.

* **Diversify** the stream (avoid look-alikes and recent repeats) so it feels organic.

* **Replenish and shuffle** as you swipe, so the feed stays fresh without feeling mechanical.

# **Why narratives matter most**

* Every category yields **two lines** (personal \+ shared) chosen by **category \+ band \+ perspective**.

* Narratives are the **primary outcome** users read and discuss; numbers live under the hood for tuning and admin QA.

# **Business story (what we’re proving)**

* **Agency:** Users can **steer** who they encounter—via presets **or** manual priorities/weights.

* **Clarity:** Matches are **explained**, not just scored—ten short narratives foster trust and conversation.

* **Focus:** A user who wants **friendship only** really gets friendship-weighted results, enforced by the zero-weight and priority rules.

* **Testability:** Admins can **tune numbers → bands** without rewriting copy; copy can evolve without touching the math.

# **Shared vocabulary (so we stay aligned)**

* **Preset (optional):** A template for weights (Friendship / Love / Collaboration / Creative) you can use or ignore.

* **Weights:** Importance levels across the ten categories (0–100). **0** excludes others whose **\#1** is that category.

* **\#1 category:** Your top priority; shown first on match cards.

* **Band:** User-visible label per category (Cool/Open/Warm/Glow).

* **Numbers:** Admin/tester percentages that drive bands (hidden from end users at first).

* **Narratives:** **Two lines per category**—**personal** and **shared**—selected by `(category, band, perspective)`.

