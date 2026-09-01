

# **PF13-Reference-Glow Development Philosophy v1** 

## **A. Intent and audience**

**Purpose.** Guide AI sessions to plan EPICs, choose strategies, prevent drift, and move fast through controlled change.

**Audience.** AI agents that design or execute work at Glow.

**Scope.** Values, lenses, decision rubrics, tension guides, glossary, and a small machine-readable annex with stable keys only.

**Non-scope.** Procedures, steps, file paths, schemas, APIs, headers, tokens, environment variables, tools, team workflows, acceptance matrices, or examples tied to any specific project or stack.

**Routing rule.** When methods or specifications are needed, refer by category only: Process Guide, Architecture, Transport, Infrastructure, Security and Privacy, Data and ML, Testing and Quality.

**Non-redundancy and stability.** PF13 changes rarely. Edit only when a tenet changes meaning, category names change, or an elemental lens is added or retired. Before editing, apply these guard tests: the change alters philosophy rather than process; it avoids duplicating material that belongs in a category home; it remains true across projects and stacks.

**AI usage contract.** At the start or revision of an EPIC, AI sessions must 1\) read PF13, 2\) use the four elements as lenses for strategy, and 3\) emit the EPIC Strategy Card described later. PF13 is the source of truth for philosophy only. All methods and proofs live in their category homes.

## **B. Core tenets**

### **1\) Controlled change enables speed**

**What this means.** We move fast by shaping work into clear, verifiable changes that reduce rework. Speed comes from control, not from skipping steps.  
 **AI behaviors.** State the outcome in one paragraph, choose a batch size that proves it quickly, finish before starting something else, and include an explicit verify step.  
 **Anti-drift checks.** Is the intent legible in one paragraph? Will this slice prove value quickly? What must be true to call it verified?

### **2\) Single home per concept**

**What this means.** Every concept has one authoritative home. Other texts point to it rather than copy it.  
 **AI behaviors.** When you need a fact or rule, point readers to the home by category. If a new concept appears, propose a home before spreading details across documents.  
 **Anti-drift checks.** Are we duplicating content that already has a home? If a new idea emerged, did we name its home?

### **3\) Coherent public surfaces**

**What this means.** There is one calm place where truth is observed. Interfaces stay simple and human. Internals remain private.  
 **AI behaviors.** Prefer one published surface per concept, keep public contracts minimal, and avoid leaking internal scaffolding. Treat reads as confirmation of reality.  
 **Anti-drift checks.** Did we create a second surface for the same idea? Does the interface expose internals?

### **4\) Clear boundaries with versioned evolution**

**What this means.** Name the contract first, then change the implementation behind it. Evolve by adding versions instead of breaking agreements.  
 **AI behaviors.** Separate public surface, application logic, and core ideas. Use explicit, programmatic configuration. Allow old and new to coexist during migration.  
 **Anti-drift checks.** Is there a named contract? Can versions coexist safely? Is configuration explicit rather than hidden flags?

### **5\) Professionalism and stewardship**

**What this means.** Respect people and future readers. Favor privacy, least privilege, and legible intent.  
 **AI behaviors.** Minimize data collected, design observability that identifies events without exposing secrets, and write decisions so they are understandable later.  
 **Anti-drift checks.** Are we collecting only what is needed? Would leaked logs cause harm? Can a future reader see why we chose this?

### **6\) Phase discipline and verification before scale**

**What this means.** Work flows through lightweight phases: intent, scope, design, implement, verify, release, learn. Verification precedes scale.  
 **AI behaviors.** Declare entry and exit signals for each phase, keep work visible, and never skip verification to gain speed.  
 **Anti-drift checks.** Are phase boundaries clear? Is there a concrete verify step and success signal before release?

## **C. The four elements**

### **1\) FIRE — Truth (effectiveness and momentum)**

**Aim.** Make a specific truth real fast, with proof.  
 **AI must emit before work begins.**

* **Outcome (one sentence):** “After this change, **X is true**.”  
* **Success signal:** the smallest observable that proves X (metric, log key, state check).  
* **Scope line:** what is in and out for this cut.

**Design rules.**

* Choose the **smallest implementation** that makes X true without side quests.  
* Keep one owner and one intent for the cut.  
* Prefer clarity over cleverness.

**Developer moves.**

* Name the user or system effect, not the technique.  
* Wire a **single observation** that proves X happened.  
* Finish and stabilize before starting anything adjacent.

**Fast proof and exit.**

* Show the observation once in a controlled run.  
* Record the one-paragraph intent and result.  
* Declare what the next increment would be.

**Anti-patterns to avoid.**

* Multi-intent bundles, vague outcomes, “we’ll verify later.”  
  ---

  ### **2\) WATER — Love & Integrity (coherence and consistency)**

**Aim.** Honor relationships. Keep one calm surface people can trust.  
 **AI must emit before work begins.**

* **Surface statement:** name the single public surface this change touches.  
* **Promise check:** what existing promise must remain true.  
* **Minimal contract phrase:** plain words for what the surface will now express.

**Design rules.**

* One **home per concept**. Point to it; do not copy.  
* Public contracts are **humane and minimal**. Internals stay private.  
* Reads confirm reality. Writes are gentle and do not claim to be truth.

**Developer moves.**

* Remove duplicate public faces for the same idea.  
* Trim internal numerics or scaffolding from public messages.  
* Keep terminology consistent with prior promises.

**Fast proof and exit.**

* Demonstrate the surface shows the expected truth in one place only.  
* Show that older clients or readers still understand the message.

**Anti-patterns to avoid.**

* Second surfaces, leaky abstractions, novelty that breaks consistency.  
  ---

  ### **3\) AIR — Knowledge & Data (boundaries and evolution)**

**Aim.** Decide with knowledge, design clear boundaries, evolve by version.  
 **AI must emit before work begins.**

* **Contract name:** what agreement defines this change.  
* **Evolution plan:** add a version or additive field rather than break in place.  
* **Data posture:** the minimum data needed and how it is observed.

**Design rules.**

* **Contracts first.** Implementation follows behind the boundary.  
* **Version forward.** Old and new can coexist. Plan the coexistence period.  
* **Programmatic configuration.** No hidden flags or magic defaults.  
* **Data minimalism.** Collect only what supports decisions and proofs.

**Developer moves.**

* Introduce a versioned seam instead of rewriting a live contract.  
* Make configuration explicit and typed.  
* Separate core logic from time, IO, and concurrency concerns.

**Fast proof and exit.**

* Show old and new behaviors running side-by-side without conflict.  
* Show rollback is one move that restores prior behavior.

**Anti-patterns to avoid.**

* Hidden cross-layer coupling, flag sprawl, rollbacks that require rewrites.  
  ---

  ### **4\) EARTH — Foundation (everything comes together)**

**Aim.** Land the change on solid ground that is safe, understandable, and durable.  
 **AI must emit before work begins.**

* **Ownership:** who is responsible for this change.  
* **Phase signals:** entry condition, exit condition, and handoff target.  
* **Safety note:** the failure mode and why it is acceptable.

**Design rules.**

* Least privilege. Observability without exposing secrets.  
* Clear ownership and continuity. The future reader can follow the why.  
* Resilience first. Degraded behavior is intentional and safe.

**Developer moves.**

* Write the one-paragraph “why” where future readers will look.  
* Choose defaults that fail closed and recover cleanly.  
* Prove the change works in an environment that resembles reality.

**Fast proof and exit.**

* Demonstrate the happy path once and the failure path once.  
* Show that failure leaves the system coherent and recoverable.

**Anti-patterns to avoid.**

* Over-collection of data, logs that reveal payloads, irreversible migrations.  
  ---

  ### **How you apply this in development (one pass per element, fast)**

* **Start with FIRE:** write the one-sentence outcome, success signal, and scope line.  
* **Check WATER:** confirm the single public surface and restate the promise that must hold.  
* **Define AIR:** name the contract, state the version step, and the minimum data you will observe.  
* **Anchor EARTH:** name ownership, entry/exit signals, and the acceptable failure mode.

If any element fails its fast proof, stop and adjust there before proceeding.

## **D. Alchemical delivery cycle**

> Seven lightweight phases that let AI sessions move fast through **controlled change**. For each phase, capture only: **purpose**, **entry signal**, **exit signal**, **handoff**. No steps or checklists live in PF13.

### **1\) Intent**

* **Purpose.** State the single **truth** we will make real and why it matters.  
* **Entry signal.** A clear problem/opportunity and the audience who cares.  
* **Exit signal.** One-sentence outcome and success signal agreed.  
* **Handoff.** Pass the outcome and success signal to **Scope**.

  ### **2\) Scope**

* **Purpose.** Set **boundaries** and batch size; decide what’s in/out for this cut.  
* **Entry signal.** Accepted outcome \+ any hard constraints or assumptions.  
* **Exit signal.** Crisp “in/out” list, target surface named, risks acknowledged.  
* **Handoff.** Provide constraints, target surface, and risks to **Design**.

  ### **3\) Design**

* **Purpose.** Choose the approach that satisfies the outcome while preserving **coherence**, **data minimalism**, and a **versioned** path forward.  
* **Entry signal.** Scoped constraints, target surface, and quality bar.  
* **Exit signal.** Named contract, version/evolution note, minimal data to observe, and stated failure mode.  
* **Handoff.** Deliver the design record (contract, version, observables, failure note) to **Implement**.

  ### **4\) Implement**

* **Purpose.** Make the change real with the smallest construction that meets the design; keep ownership singular.  
* **Entry signal.** Accepted design record and a representative environment to run in.  
* **Exit signal.** Working change with the success signal wired, safe defaults chosen, and intent recorded in one paragraph.  
* **Handoff.** Provide the running change and observation instructions to **Verify**.

  ### **5\) Verify**

* **Purpose.** Prove the change achieved the intended **truth** and did not create drift.  
* **Entry signal.** Deployed change \+ ready observables.  
* **Exit signal.** Evidence shows the success signal; coherence preserved; rollback remains one move.  
* **Handoff.** Share a short verification note and approvals to **Release**.

  ### **6\) Release**

* **Purpose.** Make the promise **durable and visible** without creating new surfaces; keep reversibility.  
* **Entry signal.** Verified change and go-live approval.  
* **Exit signal.** Promise live; ownership and reversibility documented; communications delivered where they belong.  
* **Handoff.** Provide outcomes and any follow-ups to **Learn**.

  ### **7\) Learn**

* **Purpose.** Capture insights and remove waste to accelerate the next cycle.  
* **Entry signal.** Post-release data and stakeholder feedback.  
* **Exit signal.** Succinct learning notes, next increment decision, and any corrections to language or heuristics.  
* **Handoff.** Begin the next **Intent** with updated understanding.

## **E. Working nimble without waste**

### **1\) Define outcomes in plain language *(FIRE: truth)***

**Principle.** Say exactly what will be true when you are done. Plain words create speed.  
 **Decision prompts.** Is the outcome specific, falsifiable, and meaningful to the people who care? Does it avoid technique words? Could a skeptical reader tell if it happened?  
 **Red flags.** Vague verbs (improve, optimize), stacked goals in one sentence, success that depends on unspoken conditions.

### **2\) Choose batch size that proves value fast *(AIR: knowledge, WATER: integrity)***

**Principle.** Ship a slice that demonstrates value without pulling in side concerns.  
 **Decision prompts.** What is the smallest change that would convince a reasonable reviewer? What can be safely deferred without corrupting the result? Does the slice have one intent and one place it shows up?  
 **Red flags.** Scope creep, attaching “quick extras,” slices that only make sense if several other things land at the same time.

### **3\) Limit WIP and finish slices *(EARTH: foundation, FIRE: truth)***

**Principle.** Flow beats multitasking. Finished work teaches and reduces risk.  
 **Decision prompts.** How many things are truly in progress right now? What is blocking the oldest slice, and is that blockade explicit? Does the next action directly move the current slice to finished?  
 **Red flags.** Two or more active slices touching the same surface, “nearly done” items aging without a clear blocker, new work starting before closure.

### **4\) Prefer proofs over narrative *(AIR: knowledge, WATER: integrity)***

**Principle.** Evidence ends debate. Stories follow facts.  
 **Decision prompts.** What simple observation would show the outcome happened? Can another reader repeat that observation without inside knowledge? Does the observation check what matters rather than a side effect?  
 **Red flags.** Long explanations without a crisp observation, proofs that rely on internals, success declared without something observable.

## **F. Drift prevention and double-checking**

**Goal.** No orphaned code, no duplicate truths, no undocumented behavior. Every meaningful change is traceable as **Intent → Change → Proof**, bound to a single home.

### **1\) Single home rule for concepts *(WATER · EARTH)***

**Principle.** Each concept has one authoritative home; everything else points to it.  
 **How this prevents drift.** A change that cannot be named to its home **cannot disappear**—it is either attached or it doesn’t ship.  
 **Decision prompts.** What is the concept’s home? If the change implies a new concept, what will its home be? Does any sentence in this work duplicate a truth that already has a home?  
 **Red flags.** New terms introduced with no home; two documents describing the same truth; “temporary” write-ups that become de facto sources.

### **2\) Titles-only cross references between documents *(WATER · AIR)***

**Principle.** Reference by **category/title only**; never restate the content.  
 **How this prevents drift.** When the source changes, nothing else needs updating—no copied text to rot.  
 **Decision prompts.** Are we pointing to the home, or are we restating it here? Does this sentence force a second place to maintain the same idea?  
 **Red flags.** Pasted definitions; parallel “summaries” that diverge; examples that quietly become normative text.

### **3\) Two-pass check: author intent, then reader inference *(FIRE · AIR)***

**Principle.** The maker states the intent; an independent reader (or AI session) re-states what the change **actually** does. Both must match.  
 **How this prevents drift.** Catching mismatch early stops code from shipping with a different truth than the one documented.  
 **Decision prompts.** If a skeptical reader saw only the change and its public effects, would they infer the same outcome sentence? Can the change be mistaken for a different promise?  
 **Red flags.** Intent that can be read two ways; change that alters semantics beyond what the intent claims; “it’s obvious from the code.”

### **4\) Evidence and its index updated together, at the source home only *(AIR · EARTH)***

**Principle.** **Proof** (what shows the change happened) and the **index entry** that names that proof move as one, and **only** in the home that owns the concept.  
 **How this prevents drift.** No orphan proofs; no indexes pointing to nowhere; no duplicate indexes to forget later.  
 **Decision prompts.** Where does the owning home list proofs for this concept? Does this change add or retire a proof there? Is any other place trying to track the same proof?  
 **Red flags.** “We’ll update the index later”; evidence stored away from its owning home; more than one index tracking the same thing.

---

## **G. Alignment to EPICs (stay in frame)**

**Directive.** For delivery, **adhere to the Epic process as documented in the Process Guide**. PF13 does not restate or modify that process.

**AI discipline to prevent drift (no process, just guardrails):**

* **Read before write.** Consult the category homes (Process, Architecture, Transport, Infrastructure, Security & Privacy, Data & ML, Testing & Quality). If something’s missing, ask the **smallest** clarifying question.  
* **No embellishment.** Do not invent paths, fields, tokens, schemas, or “helper” surfaces. If it isn’t in the docs, don’t create it.  
* **Single home only.** Every concept is bound to **one** home; point to it by category. If a new concept appears, propose a home (category) rather than scattering details.  
* **Titles-only routing.** Refer by category titles, not document text; never copy definitions across docs.  
* **No second surface.** Do not add a new public surface for an existing truth. If a change implies one, pause and escalate.  
* **Match intent to observable behavior.** Keep the stated outcome and what is observable in alignment; if they diverge, stop and reconcile.  
* **Contradictions → halt.** When docs conflict, stop work and pinpoint the conflict for adjudication. No “best guesses.”

Not process. Section H is a **decision lens** you use when options are close, so choices stay consistent and drift-free without prescribing steps.

## **H. Tension guides and decision rubric**

### **Purpose**

Resolve tough choices quickly and consistently using the four elements as a lens. No steps, no checklists. This is a tie-breaker, not a procedure.

### **Tie-breakers**

* **FIRE (truth) vs speed.** Prefer the option that makes a specific truth plainly real and provable now. If speed risks muddy truth, choose truth.  
* **WATER (love/integrity) vs breadth.** Prefer coherence of the single public surface over adding more capability that fractures it.  
* **AIR (knowledge/data) vs quick fix.** Prefer a clear contract and additive version path over a patch that hides coupling or blocks rollback.  
* **EARTH (foundation) vs convenience.** Prefer the safer failure shape, clearer ownership, and future legibility over shortcuts that increase risk.

  ### **Simple four-lens scoring (1–5)**

Score each option on FIRE, WATER, AIR, EARTH. Keep it quick and qualitative.

* **FIRE (truth).** 1 \= outcome vague or unprovable. 5 \= outcome crisp, observable now.  
* **WATER (integrity).** 1 \= fragments the surface or leaks internals. 5 \= keeps one calm surface, honors prior promises.  
* **AIR (knowledge).** 1 \= hidden coupling, breakage risk, data bloat. 5 \= named contract, additive version, minimal necessary data.  
* **EARTH (foundation).** 1 \= unclear ownership, unsafe failure, hard to understand later. 5 \= clear owner, safe failure, legible intent.

Add the four numbers. Use it to focus the discussion, not to mechanize it.

### **Tie resolution rule**

If totals tie, pick the option with:

1. **safer reversibility**, then  
2. **clearer ownership**, then  
3. **fewer public surfaces or flags**.

If still tied, prefer the option that reduces future choices rather than multiplying them.

### **Why this prevents drift**

* It anchors every decision to truth, surface coherence, explicit contracts, and safe foundations.  
* It blocks “quick fixes” that create second surfaces, silent contract changes, or undocumented behavior.  
* It keeps AI sessions inside the frame: adhere to procedure elsewhere, apply this lens to choose well.

## **I. Definition of done (philosophical)**

> A change is **done** when these element-truths hold. This is a lens, not a procedure.

### **1\) FIRE — Outcome is clear and matched by the change (truth)**

**Principle.** The promised truth is now real and plainly observable.  
 **Decision prompts.** Would a skeptical reader state the same outcome after seeing the result? Does any part of the change claim more than the outcome?  
 **Red flags.** Vague outcome, side-effects presented as success, multiple outcomes hiding in one change.

### **2\) WATER — No second surface created (love / integrity)**

**Principle.** There remains **one** calm public surface for this truth; prior promises still hold.  
 **Decision prompts.** Did we add or imply another place for users or systems to look? Did we leak internals into the public face?  
 **Red flags.** Duplicate interfaces, renamed concepts without continuity, “temporary” surfaces that become permanent.

### **3\) AIR — Boundaries respected and versioned (knowledge / data)**

**Principle.** Contracts are named; evolution is **additive** and reversible; knowledge captured is minimal and relevant.  
 **Decision prompts.** Which contract did we change, and how is the path forward versioned? Can old and new coexist without guesswork? Are we storing only what supports decisions?  
 **Red flags.** Hidden coupling across layers, breaking changes in place, flag sprawl, data collected “just in case.”

### **4\) EARTH — Stewardship evident; learning captured (foundation)**

**Principle.** The change is safe, legible, and leaves the system whole; what we learned will guide the next cut.  
 **Decision prompts.** Does this fail safely? Can a future reader understand the why in a paragraph? What did we learn that materially shapes the next move?  
 **Red flags.** Risk moved to users, logs that expose secrets, outcomes that can’t be understood later, no takeaway for the next iteration.

* ## **J. Glossary**

* **Controlled change** *(FIRE · EARTH)*  
   A way of working where each change has a single, stated truth to make real and a clear boundary around it. It accelerates delivery by reducing rework and surprise.  
   Anti-drift focus: if the truth cannot be stated plainly, the change is not ready.  
* **Single home** *(WATER)*  
   The one authoritative place a concept lives. All other texts point to it rather than restating it.  
   Anti-drift focus: if a fact appears in two places, one of them is wrong.  
* **Calm surface** *(WATER)*  
   The single coherent public face where reality is observed. It is plain, minimal, and stable; internals remain private.  
   Anti-drift focus: do not create a second surface for the same idea.  
* **Deterministic core (as an idea)** *(AIR)*  
   Logic that gives the same output for the same inputs, with uncertainty and side effects kept at the edges. This is a design stance, not a stack choice.  
   Anti-drift focus: if results vary without input change, the core is leaking outside influence.  
* **Programmatic configuration** *(AIR)*  
   Behavior controlled by explicit, typed, versioned inputs rather than hidden flags or guesses.  
   Anti-drift focus: if behavior changes without an intentional input change, configuration is not truly programmatic.  
* **Drift** *(FIRE · WATER · AIR · EARTH)*  
   Any divergence between intended truth, public surface, named contract, and observable reality. It includes orphan code, duplicate truths, and undocumented changes.  
   Anti-drift focus: every meaningful change binds to a home, a stated outcome, and a way to observe it.  
* **Versioned evolution** *(AIR)*  
   Changing agreements by adding versions or additive fields so old and new can coexist. No breaking in place.  
   Anti-drift focus: if consumers must guess or break to keep up, evolution was not truly versioned.

K. Machine-readable annex

Stable constants for AI ingestion. Keys only. No IDs, paths, tokens, or project specifics.

{

  "pf13\_annex": {

    "audience": "AI-only",

    "tenets": \[

      "controlled\_change",

      "single\_home",

      "coherent\_surface",

      "clear\_boundaries\_versioned",

      "stewardship",

      "phase\_discipline\_verification"

    \],

    "elements": {

      "FIRE": { "label": "truth", "prompts": \["outcome", "success\_signal", "scope\_line"\] },

      "WATER": { "label": "love\_integrity", "prompts": \["surface", "promise\_check"\] },

      "AIR": { "label": "knowledge\_data", "prompts": \["contract", "version\_path", "data\_minimum"\] },

      "EARTH": { "label": "foundation", "prompts": \["ownership", "fail\_safe", "legibility"\] }

    },

    "strategy\_card\_fields": \[

      "outcome\_fire",

      "surface\_water",

      "boundary\_air",

      "stewardship\_earth"

    \],

    "rubric\_fields": \["FIRE", "WATER", "AIR", "EARTH"\],

    "tie\_breaker\_rule": "prefer\_option\_with\_safer\_reversibility\_then\_clearer\_ownership"

  }

}

## **L. Stewardship of PF13**

**Reference only, low change rate.** PF13 is philosophy for AI sessions. It should be stable and sparse. Treat it as a compass, not a playbook.

**Rare update triggers (the only reasons to edit PF13):**

1. A **tenet** changes in meaning.  
2. The set or names of **category homes** change (Process, Architecture, Transport, Infrastructure, Security and Privacy, Data and ML, Testing and Quality).  
3. An elemental **lens** is added or retired (FIRE, WATER, AIR, EARTH) or their mappings shift (truth, love/integrity, knowledge/data, foundation).

**Immutables.**

* Audience \= **AI only**.  
* Scope \= **philosophy and lenses**; Non-scope \= **procedures, paths, schemas, APIs, tokens, tools, examples tied to a project**.  
* **Titles-only** routing to category homes; no duplication.  
* Machine-readable annex \= **stable keys only**.

**Change guards (must all be true before any edit):**

* The edit adjusts **philosophy**, not process or examples.  
* It **does not duplicate** content that lives in a category home.  
* It remains **true across projects and stacks**.

If a proposed change fails any guard, do not edit PF13; update or create the relevant category document instead.

