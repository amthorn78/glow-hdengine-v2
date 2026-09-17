# GCFPE Repair — Installed Skill Binding Evidence v1.0

The two proven installed candidate binding defects are corrected and saved. The local candidate validator, strict Change Flow/Primary/R1 validation and all 126 successor cases pass. This is a checkpoint for the existing unselected candidate; semantic impact reconciliation and independent governance postflight remain open.

| Skill | Current revision | Disposition |
|---|---|---|
| change-flow | 3.2.4 | Candidate resource revision 4.0.3 and narrow source-binding validator corrected; workflow instructions unchanged. |
| flowmaster-validate | 3.2.3 | Corrected candidate contract/graph pins and byte counts; five source regression cases added; all prior predicates and fixtures preserved. |
| glow-hde-pr-development | 1.2.4 | Confirmed unchanged; sole PR-30/PR-35/recovery/eligible RS-40 execution owner. |
| glow-hde-devops | 1.5.0 | Confirmed unchanged; bounded supporting operational capability only. |
| glow-merged-change-attribution-lock | 1.2.0 | Confirmed unchanged; optional read-only post-merge PR-40 evidence only. |
| amthor-workspace-governance-audit | 1.11.1 | Confirmed unchanged; independent governance audit ownership, no repair or worker execution authority. |

The Change Flow behavior revision remains 3.2.4 because its workflow instructions did not change. Its candidate resource revision advances to 4.0.3. Flowmaster Validate advances to 3.2.3 for exact raw-source checks and five regression cases. The original 121 cases and all 33 section-13 scenarios remain intact.

Two post-save remote commits changed only the skills’ SVG icons. Complete tree diffs establish the presentation-only scope; every authored source file read back exactly. The icon changes were preserved and explicitly repinned as SRC-002 observations, not silently attributed to the requested source correction. No other skill package changed.

Production aliases, selected catalog/register, PF10 and Alpha remain outside these corrections. No product repository, PR, GitHub, CI, merge, deployment, archive or runtime action was performed. The two personal-skill maintenance saves are recorded below; they do not authorize release selection.

## Machine-readable evidence

The JSON below is valid YAML 1.2. It includes complete package file identities, exact before/after objects, reviewed diff, fixture results and the strict validator output.

```yaml
{
  "schema": "gcfpe-current-skill-binding-evidence/1.0",
  "created_at": "2026-09-14T22:52:23.426484+00:00",
  "run_id": "GCFPE-REPAIR-RECOVERY-CORRECTION-20260914.1",
  "base_commit": "517039dc7d2ddc2c4b0a8adbde83cae6cf3bb0be",
  "current_head": "0499abfd44c28614e02de8b67839a6c255f86fb6",
  "remote_head": "0499abfd44c28614e02de8b67839a6c255f86fb6",
  "clean": true,
  "selected_release": "GCFPE-20260913.1",
  "selected_prompt_version": "091326.2",
  "selected_member_count": 54,
  "candidate_release": "GCFPE-20260914.1",
  "candidate_prompt_version": "091426.1",
  "candidate_member_count": 55,
  "candidate_selected": false,
  "contract_revision": "4.0.3",
  "contract_sha256": "b3204610933a1d0f966dc98e884e193e4a2ff431066d9b082436ca2e7ccaa0fc",
  "graph_sha256": "47439465a46866e4f0c98a648887a822913a3a8ad18be66b6651634fb90eb7cb",
  "source_manifest_url": "https://drive.google.com/file/d/14lL-wbaefBcieLxVLVsoMXyvk_DdZCcc/view?usp=drivesdk",
  "source_snapshot_sha256": "a8f3351c15279224af81eac4e013d7bbcc7436c3dd5b26b7385abd870f7160be",
  "scope": "INSTALLED_SOURCE_IDENTITIES_STATIC_CONTRACTS_AND_DETERMINISTIC_FIXTURES_ONLY",
  "independent_governance_postflight": "NOT_PERFORMED",
  "semantic_impact_ledger": "PENDING_COMPLETE_RECONCILIATION",
  "promotion_authorized": false,
  "alpha_resumed": false,
  "pf10_mutated": false,
  "skills": [
    {
      "skill": "change-flow",
      "package": "skill-6a8f94d50bd08191ae150422fb3a6a2f",
      "revision": "3.2.4",
      "disposition": "Candidate resource revision 4.0.3 and narrow source-binding validator corrected; workflow instructions unchanged.",
      "tree_before": "9dfc917480bafe1fd4e2cfe7867f109c2202c3ea",
      "tree_after": "a932268f63b6dc36501570825dac9ea3158bcf4d",
      "main_sha256": "57971dcd64b426cfc952a653ce10492a5d6840659f408a5e8fa5621444fb1042",
      "changed_paths": [
        "skill-6a8f94d50bd08191ae150422fb3a6a2f/assets/icon.svg",
        "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json",
        "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json",
        "skill-6a8f94d50bd08191ae150422fb3a6a2f/scripts/validate_gcfpe_20260914.py"
      ],
      "files": [
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/SKILL.md",
          "bytes": 75080,
          "sha256": "57971dcd64b426cfc952a653ce10492a5d6840659f408a5e8fa5621444fb1042",
          "git_blob": "58fe1b906eec6d651b41b353356d9733cfa6e802",
          "complete": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/agents/openai.yaml",
          "bytes": 415,
          "sha256": "cfe06596b7111a22e3238ed0d2446237136c540d7413c10978ca8532ad448846",
          "git_blob": "9e525ba6caa53373d67c0f2056248b1ff117add6",
          "complete": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/assets/icon.svg",
          "bytes": 786,
          "sha256": "72343cc4b66256ae7de8474c7cad14e711ad84a94c473732a44f96a56124c42d",
          "git_blob": "f19f1b68e96ba7df24829e7aec93ebd17396a341",
          "complete": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/alpha-feedback-correction.json",
          "bytes": 1670,
          "sha256": "617c8b6cc3799012996ec616912facfe48bd4768219ac139ad4ec94b9738aee3",
          "git_blob": "199c58d8c3d31b4f02b32847cb8409d5f7bc25d2",
          "complete": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/epic-alpha-repair-correction.json",
          "bytes": 36876,
          "sha256": "84fdd252dfe71ba843cd015b8d527fa840d42569232757a90dab6a9edf142374",
          "git_blob": "8c1dfd32d82dd7792fac4af99b92acfae7481da5",
          "complete": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/epic-reengineering-correction.json",
          "bytes": 5922,
          "sha256": "888967e4549eb532f8f8408f7a0bc1f48311821fa4f28dd4b5d1f36d6091a230",
          "git_blob": "bbe31ad118aba01bf9e4d72e34a7fa0b2b235ca9",
          "complete": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/final-cycle-scan-extension.json",
          "bytes": 3084,
          "sha256": "495ffc9df997230c492e8d286758fe45a3b63fd741a62fe75246adef27a43ab8",
          "git_blob": "b250e4ca8c0636dfc1ef68687f32289d2165ce27",
          "complete": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-20260912.2-direct-handoff-contract.json",
          "bytes": 4339,
          "sha256": "d5aaf6d1a59d627a91d034beb729335feb3cbd536fcb6dc480088c3ec66704a4",
          "git_blob": "9e3b51041ce331e5f5d84e6295750d5b40ea3373",
          "complete": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-20260913.1-091326.2-direct-handoff-contract.json",
          "bytes": 35706,
          "sha256": "bb682e7d649837ba55aa047505e4aef08a64dc2e4ebe7a559be039bc6e2e145b",
          "git_blob": "da136654b913650c838e31274f4ecb5e30488344",
          "complete": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-20260913.1-direct-handoff-contract.json",
          "bytes": 31643,
          "sha256": "92d6a5475ac98e40d88d4ef14b690b9c0c93eb28567aa1e507afb53396857fd4",
          "git_blob": "1b86e9cf957fb9aab5222ae804e7db2deaaa9c64",
          "complete": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json",
          "bytes": 518308,
          "sha256": "47439465a46866e4f0c98a648887a822913a3a8ad18be66b6651634fb90eb7cb",
          "git_blob": "2dde65ae34f0b9cda6fb541815d800ad98f1b8a8",
          "complete": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json",
          "bytes": 559697,
          "sha256": "b3204610933a1d0f966dc98e884e193e4a2ff431066d9b082436ca2e7ccaa0fc",
          "git_blob": "97b4b8b4c7369c2c569673438164438b7a9a0acf",
          "complete": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-20260914.1-091426.1-prompt-topology-readback.json",
          "bytes": 118178,
          "sha256": "705f5acfad74c9b32b91f4305e64372098f5cd82d7cd91f2388888ca7db661e3",
          "git_blob": "a67d8b01b0131dd07c1a5511c28b40f1321d73ab",
          "complete": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-20260914.1-091426.1-prompt-url-map.json",
          "bytes": 16118,
          "sha256": "d9173a288105d69686ae8de6b61d3c0ae9925fd44204fa3393d2f431d106f397",
          "git_blob": "3dbaf223da416355c8abecefae6568f472f37a11",
          "complete": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-current-direct-handoff-contract.json",
          "bytes": 35706,
          "sha256": "2b4682b34d7323abf30a4b14fa81465fcf65501aa17959be49a6524f07a212e0",
          "git_blob": "08a78c4b9f251948ebe7b67bed22de7aa45750c0",
          "complete": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/glow-hde-canonical-change-flow-r1-runtime-map.json",
          "bytes": 45691,
          "sha256": "5574666e5975c104ccf13e77a13d94e0d16f37af37de7eb26d7e0f7b00f45b0e",
          "git_blob": "f2e2d484b4801f23ef6e9516bc5b3923d377d105",
          "complete": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/integrated-qa-readiness-correction.json",
          "bytes": 20810,
          "sha256": "e94b0c8836210c934fe35fad69cf98cabe8688f86fb9c2346052c08383390949",
          "git_blob": "f14d3470543192aa700470123bd9298167da4050",
          "complete": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/pre-guide-audit-correction.json",
          "bytes": 3978,
          "sha256": "b4c00cb20ed6321b729c034bde6ef09973d5ffa4fe5d40b7a6030a0855669131",
          "git_blob": "2f05659782cfb7804d2806dbb17240aadf5cf365",
          "complete": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/strength-analyzer-middleware-correction.json",
          "bytes": 28075,
          "sha256": "76b7cfc54cd2706f5d6e0b4ee7b734362055d2001242b63039121387a23313fb",
          "git_blob": "3d8c708aabc54d6ca480eff17aa0e3b69d419ee2",
          "complete": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/scripts/pf_header_parity.py",
          "bytes": 6743,
          "sha256": "a2e0401ed37776984b3cb46dce909921ebaa1d1cd8e6fce29b4ce869f607bb4b",
          "git_blob": "38cf02fc5c6e84fc2f6a9c0d1bb50625179b57dd",
          "complete": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/scripts/validate_gcfpe_20260914.py",
          "bytes": 16423,
          "sha256": "1925788ed31d1eb470b45e6c047295e7b5e5ba49d4995a759ab3cf2fd1f33b2e",
          "git_blob": "312d7ae5c66dfdd8536f3bf49f6423e30b9fc66e",
          "complete": true
        }
      ]
    },
    {
      "skill": "flowmaster-validate",
      "package": "skill-6a8f973972a88191ae25426f5a818169",
      "revision": "3.2.3",
      "disposition": "Corrected candidate contract/graph pins and byte counts; five source regression cases added; all prior predicates and fixtures preserved.",
      "tree_before": "db36454bc51e47ba7a672fcd3e9fc0792e33c30e",
      "tree_after": "7d6e6e702c80f71b325768a06f16d027be85e780",
      "main_sha256": "0b90c73a59356c7ec2bd0d0a79c625404bb25136189aad369a97caf374ce9b2c",
      "changed_paths": [
        "skill-6a8f973972a88191ae25426f5a818169/SKILL.md",
        "skill-6a8f973972a88191ae25426f5a818169/assets/icon.svg",
        "skill-6a8f973972a88191ae25426f5a818169/references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json",
        "skill-6a8f973972a88191ae25426f5a818169/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json",
        "skill-6a8f973972a88191ae25426f5a818169/references/gcfpe-20260914.1-091426.1-validation-profile.json",
        "skill-6a8f973972a88191ae25426f5a818169/scripts/run_gcfpe_20260914_fixtures.py",
        "skill-6a8f973972a88191ae25426f5a818169/scripts/validate_flowmaster.py",
        "skill-6a8f973972a88191ae25426f5a818169/scripts/validate_gcfpe_20260914.py"
      ],
      "files": [
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/SKILL.md",
          "bytes": 23165,
          "sha256": "0b90c73a59356c7ec2bd0d0a79c625404bb25136189aad369a97caf374ce9b2c",
          "git_blob": "2c92ef232a42d034df3d2c9641681a291ca6b0cd",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/agents/openai.yaml",
          "bytes": 438,
          "sha256": "2c31e2e0b7355b0da7a558ad2d209e5e983efd38e6f46e90675b5688ba5f721d",
          "git_blob": "360461d26f53bbedd5fb6366a414aa51fc00893d",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/assets/icon.svg",
          "bytes": 420,
          "sha256": "e9301497fa98ef56aaca7ede0857b9a18dc06c34040f0679c609a6bf49b1d38b",
          "git_blob": "2468028d1ed0fc8009b1fc45e7bb027adaf0d079",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/fixtures/change-flow/scenarios.json",
          "bytes": 10581,
          "sha256": "130c234c57512d8960361fb83511de2c5120d5ab42a6abe7490244ce85f4772d",
          "git_blob": "7f461d9a7b8a1d69626d1d1bd00a6f2c633e56ae",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/fixtures/gcfpe-20260913.1-091326.2/scenarios.json",
          "bytes": 20526,
          "sha256": "92fc48a98da2341c60f70de14623477522983ccd95077118c9465139dec52250",
          "git_blob": "67975247b656e636cad1f4e71366661d740a02d0",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/fixtures/gcfpe-20260913.1/scenarios.json",
          "bytes": 2286,
          "sha256": "df75623c66ab47696c0c98edda4ec5b19b7a376ef095983149f6032a9321535e",
          "git_blob": "865f84dca7eec9ff1f7d42f7d0e066c15b77badd",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/fixtures/gcfpe-20260914.1-091426.1/scenarios.json",
          "bytes": 14451,
          "sha256": "8d216ba44858ae2bb7afbc39a889e4cd5d8f591bdc0fa0a60a0cd75ddef3ee25",
          "git_blob": "e54a1524749b9c02861a1f0ccfe191e7acfd4f9b",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json",
          "bytes": 518308,
          "sha256": "47439465a46866e4f0c98a648887a822913a3a8ad18be66b6651634fb90eb7cb",
          "git_blob": "2dde65ae34f0b9cda6fb541815d800ad98f1b8a8",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json",
          "bytes": 559697,
          "sha256": "b3204610933a1d0f966dc98e884e193e4a2ff431066d9b082436ca2e7ccaa0fc",
          "git_blob": "97b4b8b4c7369c2c569673438164438b7a9a0acf",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/references/gcfpe-20260914.1-091426.1-validation-profile.json",
          "bytes": 2505,
          "sha256": "3a4742486c72905598c2c656f837757c2eaa8526d70966d8b8a910e4f74c7e85",
          "git_blob": "3acf8c02adb39fe0c7b03579bc3ebf7fcaa6b55a",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/references/glow-hde-canonical-change-flow-r1.json",
          "bytes": 52767,
          "sha256": "52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e",
          "git_blob": "f524143a0563bddc8cea08a26a72ce8aff754b24",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/run_alpha_feedback_fixtures.py",
          "bytes": 6268,
          "sha256": "35837bc8cd7ec7524b887399fbbc7e62ce424ead6680ef07148af0053af0957d",
          "git_blob": "3229b2516179af0a1bc07c05a1df310f4d69b48d",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/run_change_flow_fixtures.py",
          "bytes": 3108,
          "sha256": "522f1b5c65bd011ce8a89668b1e9002a40c49935e99c6267567456310543ef17",
          "git_blob": "8701f6aeadb333977d774c9c224a476ad6293696",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/run_epic_alpha_fixtures.py",
          "bytes": 22899,
          "sha256": "efef2d10c1535639a896b10a3a7111addcf9a87cdf08840c4e937a3500f6ecf1",
          "git_blob": "3d6b95f262a8c9fa7d488517297587876fff6b57",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/run_final_scan_fixtures.py",
          "bytes": 5017,
          "sha256": "47aef4784685de2a30a6334ea9b5b8f47d93aeb67186807d254611336b78a491",
          "git_blob": "fd4f05338d14452dc7d2d9fdf546adce64acb81f",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/run_gcfpe_20260914_fixtures.py",
          "bytes": 27806,
          "sha256": "2afeef2eef454245938b44683eee9411768b94b021f85ccee1198685ab7fb7ec",
          "git_blob": "ab339489fcd5b98e2b778a7e57bfd7551282b511",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/run_gcfpe_current_fixtures.py",
          "bytes": 14479,
          "sha256": "fa89aa6a5c9a2ddc69bd3a99da6ab24afb4617c485649778af6047a8580f77b6",
          "git_blob": "b04130ce6fd5f0d497708e9f8f8d1dfca6914057",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/run_integrated_readiness_fixtures.py",
          "bytes": 8929,
          "sha256": "bd12286366ecdd90a15c04a87be35ff3f1143ee624bd69df550205318eabe1ac",
          "git_blob": "8476c4f0852673f9f71c6a0bd87a0df3a4694748",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/run_strength_middleware_fixtures.py",
          "bytes": 7500,
          "sha256": "5949fa1c45da3a327c9c3909848fbfaf00456ca7875431052342409ca1c68df6",
          "git_blob": "67a9391606abe63fe8fd26f22d0e3f32ef456054",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/validate_alpha_feedback.py",
          "bytes": 7245,
          "sha256": "9d192b9c9b2d060a4a98d5d73ce6db4d97a95444b14578417000293d188d27af",
          "git_blob": "de4eaea0b8809651c0dfeea846c38302e76cd026",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/validate_epic_alpha.py",
          "bytes": 28772,
          "sha256": "0b751a9e469fc5f0d530587a59165da2da73a07c9ef14779094079804b8ff0d5",
          "git_blob": "f25334be7d8f57fb4e2f2788410e3a82ee824234",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/validate_epic_reengineering.py",
          "bytes": 10533,
          "sha256": "a66b81d707c92179abf6e609293aedf96352ef17400fd5d27c6f00f3495fda91",
          "git_blob": "25455079aaebfba29d98b3ee67d51a4871b53ba3",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/validate_final_scan.py",
          "bytes": 5733,
          "sha256": "8254d5eef3a2bc43805709f3a16a978b9b7a9951b85138b72f843b8b31385a7f",
          "git_blob": "0f084303d2ba2a46cda87e225c2fe44d633dbc04",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/validate_flowmaster.py",
          "bytes": 58845,
          "sha256": "4282f2835e37c8e14971457b697b395a99aa8a3896069852e40801a192186b39",
          "git_blob": "85d6ebd4da87b00bf94c900881d8dc168d9af4c5",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/validate_gcfpe_20260914.py",
          "bytes": 73909,
          "sha256": "cb24997a326276c1e3703ebbc370278b513d6b50814e699cd9433622e5ae5c84",
          "git_blob": "80ebbc00770b84d81decdb75f5efd9b8ed51468a",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/validate_gcfpe_current.py",
          "bytes": 38758,
          "sha256": "c960c1d0b3499e2e19e7ceee9eda02d7b096d5c1fa010300d2a35d753b6d3c87",
          "git_blob": "8425d94ef782201370f0185cf706d329fb2e9082",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/validate_integrated_readiness.py",
          "bytes": 15106,
          "sha256": "c70565f3594336c7f6a82f46313c115fc34b82a805976bdb39ad806813d2a5ba",
          "git_blob": "d257d1d83f6a0b1bcfe3a7c1db0284d555247b17",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/validate_pre_guide_correction.py",
          "bytes": 5932,
          "sha256": "bcb7904d9bba35dacaea56bf9dc47bfce3a2eb49e30b289113af5d6542bb88ca",
          "git_blob": "8669118dbfe145e32938a472437b2b4ea6cec197",
          "complete": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/validate_strength_middleware.py",
          "bytes": 13062,
          "sha256": "fbc31888f3d0dc987ed0fb8b9d9d13e876ddeb5294aa55c7669b55aeada9e965",
          "git_blob": "d25eba436e1e3407e2332f2b634d3f84432206e3",
          "complete": true
        }
      ]
    },
    {
      "skill": "glow-hde-pr-development",
      "package": "skill-6aa5cd9382ec8191b9f2111ba7e16aa7",
      "revision": "1.2.4",
      "disposition": "Confirmed unchanged; sole PR-30/PR-35/recovery/eligible RS-40 execution owner.",
      "tree_before": "5314203649febdfe1e5ac345442eeb072e522407",
      "tree_after": "5314203649febdfe1e5ac345442eeb072e522407",
      "main_sha256": "cd7acb3a7c72e08318606b91c3d3a011602c3cfb6cf553aadcbf382a06b6c5dc",
      "changed_paths": [],
      "files": [
        {
          "path": "skill-6aa5cd9382ec8191b9f2111ba7e16aa7/SKILL.md",
          "bytes": 24252,
          "sha256": "cd7acb3a7c72e08318606b91c3d3a011602c3cfb6cf553aadcbf382a06b6c5dc",
          "git_blob": "4ed7e72166e7d0df830e318d7b20ed67c0f061d8",
          "complete": true
        },
        {
          "path": "skill-6aa5cd9382ec8191b9f2111ba7e16aa7/agents/openai.yaml",
          "bytes": 402,
          "sha256": "54ed379fa4c573bb93b019d6814db56d0bd75865aa5c9335b1b07dfc4dd3eb8e",
          "git_blob": "89042d88bb5f7d256ef760a887edbff135294037",
          "complete": true
        },
        {
          "path": "skill-6aa5cd9382ec8191b9f2111ba7e16aa7/assets/icon.svg",
          "bytes": 1738,
          "sha256": "8936b24f674a1250d999e2c2b5901374fb4240426f32bd1ae340c352a90d617d",
          "git_blob": "c782ded19ff8d6a930f75d1c6433f509da0df66a",
          "complete": true
        },
        {
          "path": "skill-6aa5cd9382ec8191b9f2111ba7e16aa7/references/behavior-cases.md",
          "bytes": 11554,
          "sha256": "06ba372111d8ea22cedeb16ed24ddec4a812c4ea57a952dad99e80a8e2bd46eb",
          "git_blob": "84d69c03f5173cdc76aa921c6078cb9ee69a3ffd",
          "complete": true
        },
        {
          "path": "skill-6aa5cd9382ec8191b9f2111ba7e16aa7/scripts/validate_glow_hde_pr_development.py",
          "bytes": 8947,
          "sha256": "d583563d83d424432ae5a166f4941cf13275753c74d0cd140ad370c0616de9bb",
          "git_blob": "1f2137abb2b5825d39a83ccee77e915ced612e05",
          "complete": true
        }
      ]
    },
    {
      "skill": "glow-hde-devops",
      "package": "skill-6a92b8d4dae08191a05cc865278a13c6",
      "revision": "1.5.0",
      "disposition": "Confirmed unchanged; bounded supporting operational capability only.",
      "tree_before": "403b7bac031c8f058307c5a4ed6058e80a5ce553",
      "tree_after": "403b7bac031c8f058307c5a4ed6058e80a5ce553",
      "main_sha256": "499b8c23a28f488efa50cf4aad61981ece33314633d520a631259153742bfb4b",
      "changed_paths": [],
      "files": [
        {
          "path": "skill-6a92b8d4dae08191a05cc865278a13c6/SKILL.md",
          "bytes": 13582,
          "sha256": "499b8c23a28f488efa50cf4aad61981ece33314633d520a631259153742bfb4b",
          "git_blob": "d5c972e6900eb197a50e034f4960735fd7cd30ab",
          "complete": true
        },
        {
          "path": "skill-6a92b8d4dae08191a05cc865278a13c6/agents/openai.yaml",
          "bytes": 345,
          "sha256": "0e3cb90ce59beb9abd08729369523e4c6fb5d97cefb49a52484c5b1459dd2245",
          "git_blob": "5985c91365cb4465a94e4483f15aadb08ae7442f",
          "complete": true
        },
        {
          "path": "skill-6a92b8d4dae08191a05cc865278a13c6/assets/icon.svg",
          "bytes": 1738,
          "sha256": "8936b24f674a1250d999e2c2b5901374fb4240426f32bd1ae340c352a90d617d",
          "git_blob": "c782ded19ff8d6a930f75d1c6433f509da0df66a",
          "complete": true
        },
        {
          "path": "skill-6a92b8d4dae08191a05cc865278a13c6/references/database-ops.md",
          "bytes": 3825,
          "sha256": "bc733cce4edad4c16fdc2af7ec94388be68f465ca98ba7197c08c8a12df61eff",
          "git_blob": "949edd9184cd73295745c655b150f06ac35373fc",
          "complete": true
        },
        {
          "path": "skill-6a92b8d4dae08191a05cc865278a13c6/references/evidence-and-recovery.md",
          "bytes": 5182,
          "sha256": "77312b5eb86af9f112994a1d018739a4e0f23540b8f850594b79dc3dbdb0292b",
          "git_blob": "d95bd3a159639610d2d058534adfccb56ead05fb",
          "complete": true
        },
        {
          "path": "skill-6a92b8d4dae08191a05cc865278a13c6/references/github-and-local-qa.md",
          "bytes": 9164,
          "sha256": "ee22dba7b61b12d26b0ebeb87acfba34c0d2b1b8f69cfc06655ec7829bac1171",
          "git_blob": "bfcbdd7f6009f5cd971ef3edf4346ef2de5f1637",
          "complete": true
        },
        {
          "path": "skill-6a92b8d4dae08191a05cc865278a13c6/references/openrails-vendor.md",
          "bytes": 2950,
          "sha256": "f07d139935e3fede8f1ea506ec20656d5aad8d487385aef2ba43a1e80eb91554",
          "git_blob": "f338ec008a8e21173e9407b929eeea879f095dc6",
          "complete": true
        },
        {
          "path": "skill-6a92b8d4dae08191a05cc865278a13c6/references/railway-and-secrets.md",
          "bytes": 7614,
          "sha256": "09e39a875ba415a27664db161491bd097d8a09377b8182cce93c2e98480992fa",
          "git_blob": "41989f5859dab7705badc0c23576bab49563c860",
          "complete": true
        },
        {
          "path": "skill-6a92b8d4dae08191a05cc865278a13c6/references/repository-contract.md",
          "bytes": 2686,
          "sha256": "2ff70f201774a765d5ae0d58b30d963048590fb52e3cb122b09a852d3593ace6",
          "git_blob": "397678c83943b48af2ee5f50ffc5fb5f40577bdd",
          "complete": true
        },
        {
          "path": "skill-6a92b8d4dae08191a05cc865278a13c6/references/workstation-capabilities.md",
          "bytes": 6509,
          "sha256": "b6f9f9d869978a37fc16b3f5d5f42d652cf3b985fff351cd611f29d35bdcb281",
          "git_blob": "2f30ebe7cf4280ccca98cbe6c044b5fe3f749b39",
          "complete": true
        },
        {
          "path": "skill-6a92b8d4dae08191a05cc865278a13c6/scripts/bootstrap_hde.sh",
          "bytes": 9275,
          "sha256": "b1dca102c3582e9f15bc049a2926eae3edfc618b859f84a8ad1c2eec1080cfeb",
          "git_blob": "86f803390a42d73f1f4eb495d8567b86490da73d",
          "complete": true
        },
        {
          "path": "skill-6a92b8d4dae08191a05cc865278a13c6/scripts/hde_devops.py",
          "bytes": 21909,
          "sha256": "324f23577201eb98c7fb8bc7be34fc89eeb9ebc5de0af58d6255455a048ec236",
          "git_blob": "ded46b08713fdb0f0c065bb6fb43cb35cc2c66f0",
          "complete": true
        },
        {
          "path": "skill-6a92b8d4dae08191a05cc865278a13c6/scripts/openrails_compat.py",
          "bytes": 10435,
          "sha256": "18907a40c68c54a429f4085679ba41362ff91af688dcc9e5b93707cacdf5950a",
          "git_blob": "33b6943000dfa00d2d4969856e7b9441c889c2e8",
          "complete": true
        },
        {
          "path": "skill-6a92b8d4dae08191a05cc865278a13c6/scripts/validate_hde_devops.py",
          "bytes": 16856,
          "sha256": "1cf83e559e2334813fbd049583ec0d5e7cc8d36c9b57c0301683124601ea8017",
          "git_blob": "751461ac94c05bbd8fc30473dd9c1b9507713d9d",
          "complete": true
        }
      ]
    },
    {
      "skill": "glow-merged-change-attribution-lock",
      "package": "skill-6a920c8fc8bc819181e251269b792d32",
      "revision": "1.2.0",
      "disposition": "Confirmed unchanged; optional read-only post-merge PR-40 evidence only.",
      "tree_before": "017b4d614b91bd0bd5f160093d1e47cb9f17aec6",
      "tree_after": "017b4d614b91bd0bd5f160093d1e47cb9f17aec6",
      "main_sha256": "4da572c959c814417138b439f71402db46dd2aa7f33858e8c8b548b29d529470",
      "changed_paths": [],
      "files": [
        {
          "path": "skill-6a920c8fc8bc819181e251269b792d32/.gitignore",
          "bytes": 23,
          "sha256": "6feaded4e28ea86e001a6751b4e3d960e8b7c31b9616ff9936b79297086e809b",
          "git_blob": "43ae0e2a6c6d8fca34872506ca0f2e64194fec7c",
          "complete": true
        },
        {
          "path": "skill-6a920c8fc8bc819181e251269b792d32/SKILL.md",
          "bytes": 13350,
          "sha256": "4da572c959c814417138b439f71402db46dd2aa7f33858e8c8b548b29d529470",
          "git_blob": "dbd4a2a074c5a69c17cab2407fc845a32a0d04d0",
          "complete": true
        },
        {
          "path": "skill-6a920c8fc8bc819181e251269b792d32/agents/openai.yaml",
          "bytes": 443,
          "sha256": "ccf8afd5c7bdc8f6369155f81e373f96f61383d681a05d43ea8c3ad163d0e444",
          "git_blob": "68852123b48f75feaed2a5efbcce5c053a52a198",
          "complete": true
        },
        {
          "path": "skill-6a920c8fc8bc819181e251269b792d32/assets/icon.svg",
          "bytes": 843,
          "sha256": "0cdb7990dea3ad89ead04743eeac2dc58c119fb0b8b4a01499a21237f155bc1a",
          "git_blob": "3aa5522d9c0f47cbeaabca31dcbcb2111d99531b",
          "complete": true
        },
        {
          "path": "skill-6a920c8fc8bc819181e251269b792d32/references/attribution-interface.md",
          "bytes": 12349,
          "sha256": "8f987b006e8c17858f1bbe30d6d07800b507405ca34e2b020b37a141be693355",
          "git_blob": "224fcb240c77dcb05d80486936c4e4db6581f7c8",
          "complete": true
        },
        {
          "path": "skill-6a920c8fc8bc819181e251269b792d32/references/merge-method-semantics.md",
          "bytes": 4249,
          "sha256": "c6fa4b08de47e059ff3b7d221d4a95d533809500f04d826d16085dbb8096ce77",
          "git_blob": "5ed12c6a363af6d390f32f760a84f8e09eb5e537",
          "complete": true
        },
        {
          "path": "skill-6a920c8fc8bc819181e251269b792d32/references/validation-matrix.md",
          "bytes": 6369,
          "sha256": "9e4bf01273e65a1fa4a7c854db38ab908adf4ccf6428114d7a862cf1d40b2a25",
          "git_blob": "a0cd6c9bb677fe57b207eb6faaa1fa84d4fbce46",
          "complete": true
        },
        {
          "path": "skill-6a920c8fc8bc819181e251269b792d32/scripts/collect_git_attribution.py",
          "bytes": 50196,
          "sha256": "17fa2d0c1daf219f8735f5d662596a6791b8fce8cdc9f87608f89ab366dcbaa0",
          "git_blob": "69dacf3aff7ef07bf4dcfe0844b09ed7b18c8fd9",
          "complete": true
        },
        {
          "path": "skill-6a920c8fc8bc819181e251269b792d32/scripts/run_artifact_adversarial_tests.py",
          "bytes": 31627,
          "sha256": "b693aa9a1e783ef96e8526d1c10902e3a0345022cfed8de3376fff157da3ea9d",
          "git_blob": "c70c3af463d165dd0558d71e14681bf10e51aae0",
          "complete": true
        },
        {
          "path": "skill-6a920c8fc8bc819181e251269b792d32/scripts/run_collector_adversarial_tests.py",
          "bytes": 45677,
          "sha256": "5556713dcc0927ea70569e71e8d750c94eb6ad5f754c4c758ba9d9afe2661239",
          "git_blob": "31c475c2a729af01c37013cb9f6a290e1021f778",
          "complete": true
        },
        {
          "path": "skill-6a920c8fc8bc819181e251269b792d32/scripts/run_fixture_tests.py",
          "bytes": 27695,
          "sha256": "285fed394dd6b32744871e7a7365fd8087479a0d123289d32512a34a14a60db4",
          "git_blob": "0e7a12f0797aa553fc51a24c0892f367ef419a49",
          "complete": true
        },
        {
          "path": "skill-6a920c8fc8bc819181e251269b792d32/scripts/validate_attribution_artifact.py",
          "bytes": 53630,
          "sha256": "9ebf302ec6b49c8ecc0ab977d32688ecdd2d45afd1d97e70770e6a6c22add055",
          "git_blob": "e1b57723f2a1593d7e9d00fcbb9ad7009888e83a",
          "complete": true
        }
      ]
    },
    {
      "skill": "amthor-workspace-governance-audit",
      "package": "skill-6a93504b3ac881918977417b1bb8085e",
      "revision": "1.11.1",
      "disposition": "Confirmed unchanged; independent governance audit ownership, no repair or worker execution authority.",
      "tree_before": "7401b01715a82760f7bca5fc3bf199322201a37d",
      "tree_after": "7401b01715a82760f7bca5fc3bf199322201a37d",
      "main_sha256": "e4536aae8c5c65c7fd12b9c9390dd8cf0c2cbfd844cfea897f2f1e3a1be158a8",
      "changed_paths": [],
      "files": [
        {
          "path": "skill-6a93504b3ac881918977417b1bb8085e/SKILL.md",
          "bytes": 21817,
          "sha256": "e4536aae8c5c65c7fd12b9c9390dd8cf0c2cbfd844cfea897f2f1e3a1be158a8",
          "git_blob": "e76bdbbcedcc1e0142823072afcdfd04145d601c",
          "complete": true
        },
        {
          "path": "skill-6a93504b3ac881918977417b1bb8085e/agents/openai.yaml",
          "bytes": 415,
          "sha256": "47a13f93a2b83edc6fefcff8f29c8d30fa148a5cd517004f920c90282cb0afae",
          "git_blob": "986c658187b0018ad0b0f4a517b58f64537dc928",
          "complete": true
        },
        {
          "path": "skill-6a93504b3ac881918977417b1bb8085e/assets/icon.svg",
          "bytes": 420,
          "sha256": "e9301497fa98ef56aaca7ede0857b9a18dc06c34040f0679c609a6bf49b1d38b",
          "git_blob": "2468028d1ed0fc8009b1fc45e7bb027adaf0d079",
          "complete": true
        },
        {
          "path": "skill-6a93504b3ac881918977417b1bb8085e/references/behavioral-fixtures.md",
          "bytes": 5895,
          "sha256": "715140cbb7eaaa91039d22ad860f526294ba5023b1ae2daa4b8d894316711131",
          "git_blob": "6126358fc482bcf25617de5b8c5cf47dee3f6a0f",
          "complete": true
        },
        {
          "path": "skill-6a93504b3ac881918977417b1bb8085e/references/epic-reengineering-interoperability.md",
          "bytes": 18029,
          "sha256": "faa3bcaff47d1db63220ef766fd66fce976789fb5125319f4630f9aeed73da07",
          "git_blob": "e89aa8e7fc113641dbb54bbccf8ee93a09ccfbd9",
          "complete": true
        },
        {
          "path": "skill-6a93504b3ac881918977417b1bb8085e/references/interoperability-contracts.md",
          "bytes": 15954,
          "sha256": "138f6b90b5c915bdf54438c43dc615cedbaaf8a3b62840e809cf6bc11b9740c2",
          "git_blob": "e6d63b8ca43a84f72caaf92b9e034b13396f1077",
          "complete": true
        },
        {
          "path": "skill-6a93504b3ac881918977417b1bb8085e/references/project-prompt-registry-schema.md",
          "bytes": 3348,
          "sha256": "3aef369fc78811a85d6bf476a960fbac3244bdd129d07281e8b25262de8cefb9",
          "git_blob": "cae982d76713a31c91db885fcb0b7bc6ba24c495",
          "complete": true
        },
        {
          "path": "skill-6a93504b3ac881918977417b1bb8085e/references/report-contracts.md",
          "bytes": 2767,
          "sha256": "ba9919ba19b505c2997e1053f96344f262fcde30448fbee35ccfb4a3222c4c07",
          "git_blob": "5df502f867e91c38f2d1dc1a994301f941e61846",
          "complete": true
        },
        {
          "path": "skill-6a93504b3ac881918977417b1bb8085e/references/rule-catalog.md",
          "bytes": 3231,
          "sha256": "2ee514fc9b9e6296dbb7ef49836f9fe3f530d2612414fb3a606d0c79124ca722",
          "git_blob": "06b4ae57a99cc82de574f08865bce4640862ad39",
          "complete": true
        },
        {
          "path": "skill-6a93504b3ac881918977417b1bb8085e/references/workspace-skill-registry-schema.md",
          "bytes": 2603,
          "sha256": "b79bd5197371109b17ba0626203c9c398c6fc3a9dee7662283dbe1decf900f91",
          "git_blob": "1c51fb4b6d124e1abfaa2aef6d027fd60ff7b6a9",
          "complete": true
        },
        {
          "path": "skill-6a93504b3ac881918977417b1bb8085e/scripts/audit_workspace_governance.py",
          "bytes": 43901,
          "sha256": "f7471bb398e1f3815868707eaa3fb7ba4946cd0bbdceb685af94e2e925e102fa",
          "git_blob": "06a99edb91422890ed4c18ec0e99db41aa5fab03",
          "complete": true
        },
        {
          "path": "skill-6a93504b3ac881918977417b1bb8085e/scripts/build_snapshot_manifest.py",
          "bytes": 1055,
          "sha256": "f8ae769c03813e827e463cef0da64bbf01fdef0a0f98b771de15bc3659d4779f",
          "git_blob": "8ec56d4eb27b667a15ee762bf22784a20def11e1",
          "complete": true
        },
        {
          "path": "skill-6a93504b3ac881918977417b1bb8085e/scripts/detect_skill_collisions.py",
          "bytes": 1256,
          "sha256": "3fcc40f4988d4be0d876a9ddb681af6f1cd288fb801cf4405bd5384de6a28f38",
          "git_blob": "cb19ad2d142120dd4e7a3e2efd31b36360f6c6df",
          "complete": true
        },
        {
          "path": "skill-6a93504b3ac881918977417b1bb8085e/scripts/run_fixture_suite.py",
          "bytes": 18346,
          "sha256": "1d19c25d8392e4fe7cd176b8ec1ba3d73ae31537bfeb588bea2d6b7a53679fc0",
          "git_blob": "79dbad12169a417347414ebf5bb7d63ff857e89e",
          "complete": true
        },
        {
          "path": "skill-6a93504b3ac881918977417b1bb8085e/scripts/validate_project_prompt_registry.py",
          "bytes": 700,
          "sha256": "f0499082570ffc889d55dcc33b00e0b4ad9f6a63de3bf4ec1591ef4f8fcd4a16",
          "git_blob": "130704db0f7606fd3b9b70c0e8a4ae6a8824cfbf",
          "complete": true
        },
        {
          "path": "skill-6a93504b3ac881918977417b1bb8085e/scripts/validate_workspace_skill_registry.py",
          "bytes": 696,
          "sha256": "59307bd42eb4b0a80f90bc141de3713e887d5071d34e34d73f6a9a81ac2b1a5d",
          "git_blob": "480caa66e3b21b34e6395d464cece2261ce80b06",
          "complete": true
        }
      ]
    }
  ],
  "protected": [
    {
      "path": "skill-6a8f9341ec3481918d531eca7d2d7f97/SKILL.md",
      "sha256": "30540aaf33501c1e24a9d380a5b45ac7e832bfc729bb56ca71ff7ff1e2947571",
      "unchanged": true
    },
    {
      "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/SKILL.md",
      "sha256": "57971dcd64b426cfc952a653ce10492a5d6840659f408a5e8fa5621444fb1042",
      "unchanged": true
    },
    {
      "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/glow-hde-canonical-change-flow-r1-runtime-map.json",
      "sha256": "5574666e5975c104ccf13e77a13d94e0d16f37af37de7eb26d7e0f7b00f45b0e",
      "unchanged": true
    },
    {
      "path": "skill-6a8f973972a88191ae25426f5a818169/references/glow-hde-canonical-change-flow-r1.json",
      "sha256": "52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e",
      "unchanged": true
    },
    {
      "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-current-direct-handoff-contract.json",
      "sha256": "2b4682b34d7323abf30a4b14fa81465fcf65501aa17959be49a6524f07a212e0",
      "unchanged": true
    }
  ],
  "save_receipts": [
    {
      "schema": "gcfpe-skill-save-readback/1.0",
      "retrieved_at": "2026-09-14T22:45:13.327627+00:00",
      "skill": "change-flow",
      "authored_commit": "d8197c5075d9867f1da8baaa503c9a3ff5c86932",
      "remote_head": "6f2a480d2f64b37f8b24c874ec07c4220612a053",
      "local_head": "6f2a480d2f64b37f8b24c874ec07c4220612a053",
      "clean": true,
      "result": "PASS",
      "representation_drift": {
        "rule": "SRC-002",
        "finding": "REC-CORR-SRC-002-02",
        "status": "EXPLICITLY_REPINNED_PRESENTATION_ONLY",
        "changed_path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/assets/icon.svg",
        "authoritative_source_or_behavior_changed": false,
        "basis": "Entire authored..remote tree diff contains only assets/icon.svg; every instruction, contract, validator and selected alias is byte-identical to authored commit. Commit message alone was not proof.",
        "remote_event": "Materialized from stored content",
        "action": "Preserved remote icon; fast-forwarded clean existing checkout and read back complete package."
      },
      "files": [
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/SKILL.md",
          "git_blob": "58fe1b906eec6d651b41b353356d9733cfa6e802",
          "sha256": "57971dcd64b426cfc952a653ce10492a5d6840659f408a5e8fa5621444fb1042",
          "bytes": 75080,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/agents/openai.yaml",
          "git_blob": "9e525ba6caa53373d67c0f2056248b1ff117add6",
          "sha256": "cfe06596b7111a22e3238ed0d2446237136c540d7413c10978ca8532ad448846",
          "bytes": 415,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/assets/icon.svg",
          "git_blob": "f19f1b68e96ba7df24829e7aec93ebd17396a341",
          "sha256": "72343cc4b66256ae7de8474c7cad14e711ad84a94c473732a44f96a56124c42d",
          "bytes": 786,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/alpha-feedback-correction.json",
          "git_blob": "199c58d8c3d31b4f02b32847cb8409d5f7bc25d2",
          "sha256": "617c8b6cc3799012996ec616912facfe48bd4768219ac139ad4ec94b9738aee3",
          "bytes": 1670,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/epic-alpha-repair-correction.json",
          "git_blob": "8c1dfd32d82dd7792fac4af99b92acfae7481da5",
          "sha256": "84fdd252dfe71ba843cd015b8d527fa840d42569232757a90dab6a9edf142374",
          "bytes": 36876,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/epic-reengineering-correction.json",
          "git_blob": "bbe31ad118aba01bf9e4d72e34a7fa0b2b235ca9",
          "sha256": "888967e4549eb532f8f8408f7a0bc1f48311821fa4f28dd4b5d1f36d6091a230",
          "bytes": 5922,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/final-cycle-scan-extension.json",
          "git_blob": "b250e4ca8c0636dfc1ef68687f32289d2165ce27",
          "sha256": "495ffc9df997230c492e8d286758fe45a3b63fd741a62fe75246adef27a43ab8",
          "bytes": 3084,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-20260912.2-direct-handoff-contract.json",
          "git_blob": "9e3b51041ce331e5f5d84e6295750d5b40ea3373",
          "sha256": "d5aaf6d1a59d627a91d034beb729335feb3cbd536fcb6dc480088c3ec66704a4",
          "bytes": 4339,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-20260913.1-091326.2-direct-handoff-contract.json",
          "git_blob": "da136654b913650c838e31274f4ecb5e30488344",
          "sha256": "bb682e7d649837ba55aa047505e4aef08a64dc2e4ebe7a559be039bc6e2e145b",
          "bytes": 35706,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-20260913.1-direct-handoff-contract.json",
          "git_blob": "1b86e9cf957fb9aab5222ae804e7db2deaaa9c64",
          "sha256": "92d6a5475ac98e40d88d4ef14b690b9c0c93eb28567aa1e507afb53396857fd4",
          "bytes": 31643,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json",
          "git_blob": "2dde65ae34f0b9cda6fb541815d800ad98f1b8a8",
          "sha256": "47439465a46866e4f0c98a648887a822913a3a8ad18be66b6651634fb90eb7cb",
          "bytes": 518308,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json",
          "git_blob": "97b4b8b4c7369c2c569673438164438b7a9a0acf",
          "sha256": "b3204610933a1d0f966dc98e884e193e4a2ff431066d9b082436ca2e7ccaa0fc",
          "bytes": 559697,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-20260914.1-091426.1-prompt-topology-readback.json",
          "git_blob": "a67d8b01b0131dd07c1a5511c28b40f1321d73ab",
          "sha256": "705f5acfad74c9b32b91f4305e64372098f5cd82d7cd91f2388888ca7db661e3",
          "bytes": 118178,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-20260914.1-091426.1-prompt-url-map.json",
          "git_blob": "3dbaf223da416355c8abecefae6568f472f37a11",
          "sha256": "d9173a288105d69686ae8de6b61d3c0ae9925fd44204fa3393d2f431d106f397",
          "bytes": 16118,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-current-direct-handoff-contract.json",
          "git_blob": "08a78c4b9f251948ebe7b67bed22de7aa45750c0",
          "sha256": "2b4682b34d7323abf30a4b14fa81465fcf65501aa17959be49a6524f07a212e0",
          "bytes": 35706,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/glow-hde-canonical-change-flow-r1-runtime-map.json",
          "git_blob": "f2e2d484b4801f23ef6e9516bc5b3923d377d105",
          "sha256": "5574666e5975c104ccf13e77a13d94e0d16f37af37de7eb26d7e0f7b00f45b0e",
          "bytes": 45691,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/integrated-qa-readiness-correction.json",
          "git_blob": "f14d3470543192aa700470123bd9298167da4050",
          "sha256": "e94b0c8836210c934fe35fad69cf98cabe8688f86fb9c2346052c08383390949",
          "bytes": 20810,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/pre-guide-audit-correction.json",
          "git_blob": "2f05659782cfb7804d2806dbb17240aadf5cf365",
          "sha256": "b4c00cb20ed6321b729c034bde6ef09973d5ffa4fe5d40b7a6030a0855669131",
          "bytes": 3978,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/strength-analyzer-middleware-correction.json",
          "git_blob": "3d8c708aabc54d6ca480eff17aa0e3b69d419ee2",
          "sha256": "76b7cfc54cd2706f5d6e0b4ee7b734362055d2001242b63039121387a23313fb",
          "bytes": 28075,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/scripts/pf_header_parity.py",
          "git_blob": "38cf02fc5c6e84fc2f6a9c0d1bb50625179b57dd",
          "sha256": "a2e0401ed37776984b3cb46dce909921ebaa1d1cd8e6fce29b4ce869f607bb4b",
          "bytes": 6743,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/scripts/validate_gcfpe_20260914.py",
          "git_blob": "312d7ae5c66dfdd8536f3bf49f6423e30b9fc66e",
          "sha256": "1925788ed31d1eb470b45e6c047295e7b5e5ba49d4995a759ab3cf2fd1f33b2e",
          "bytes": 16423,
          "remote_readback_equal": true
        }
      ]
    },
    {
      "schema": "gcfpe-skill-save-readback/1.0",
      "retrieved_at": "2026-09-14T22:50:11.882596+00:00",
      "skill": "flowmaster-validate",
      "validator_revision": "3.2.3",
      "authored_commit": "7b8b5838c060fb9877ea60d9ee048b75876d3d1d",
      "remote_head": "0499abfd44c28614e02de8b67839a6c255f86fb6",
      "local_head": "0499abfd44c28614e02de8b67839a6c255f86fb6",
      "clean": true,
      "result": "PASS",
      "representation_drift": {
        "rule": "SRC-002",
        "finding": "REC-CORR-SRC-002-03",
        "status": "EXPLICITLY_REPINNED_PRESENTATION_ONLY",
        "changed_path": "skill-6a8f973972a88191ae25426f5a818169/assets/icon.svg",
        "authoritative_source_or_behavior_changed": false,
        "basis": "Entire authored..remote tree diff contains only assets/icon.svg; all instructions, contracts, validators, fixtures and selected aliases remain byte-identical.",
        "remote_event": "Materialized from stored content",
        "action": "Preserved remote icon; fast-forwarded clean existing checkout and read back complete package."
      },
      "files": [
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/SKILL.md",
          "git_blob": "2c92ef232a42d034df3d2c9641681a291ca6b0cd",
          "sha256": "0b90c73a59356c7ec2bd0d0a79c625404bb25136189aad369a97caf374ce9b2c",
          "bytes": 23165,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/agents/openai.yaml",
          "git_blob": "360461d26f53bbedd5fb6366a414aa51fc00893d",
          "sha256": "2c31e2e0b7355b0da7a558ad2d209e5e983efd38e6f46e90675b5688ba5f721d",
          "bytes": 438,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/assets/icon.svg",
          "git_blob": "2468028d1ed0fc8009b1fc45e7bb027adaf0d079",
          "sha256": "e9301497fa98ef56aaca7ede0857b9a18dc06c34040f0679c609a6bf49b1d38b",
          "bytes": 420,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/fixtures/change-flow/scenarios.json",
          "git_blob": "7f461d9a7b8a1d69626d1d1bd00a6f2c633e56ae",
          "sha256": "130c234c57512d8960361fb83511de2c5120d5ab42a6abe7490244ce85f4772d",
          "bytes": 10581,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/fixtures/gcfpe-20260913.1-091326.2/scenarios.json",
          "git_blob": "67975247b656e636cad1f4e71366661d740a02d0",
          "sha256": "92fc48a98da2341c60f70de14623477522983ccd95077118c9465139dec52250",
          "bytes": 20526,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/fixtures/gcfpe-20260913.1/scenarios.json",
          "git_blob": "865f84dca7eec9ff1f7d42f7d0e066c15b77badd",
          "sha256": "df75623c66ab47696c0c98edda4ec5b19b7a376ef095983149f6032a9321535e",
          "bytes": 2286,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/fixtures/gcfpe-20260914.1-091426.1/scenarios.json",
          "git_blob": "e54a1524749b9c02861a1f0ccfe191e7acfd4f9b",
          "sha256": "8d216ba44858ae2bb7afbc39a889e4cd5d8f591bdc0fa0a60a0cd75ddef3ee25",
          "bytes": 14451,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json",
          "git_blob": "2dde65ae34f0b9cda6fb541815d800ad98f1b8a8",
          "sha256": "47439465a46866e4f0c98a648887a822913a3a8ad18be66b6651634fb90eb7cb",
          "bytes": 518308,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json",
          "git_blob": "97b4b8b4c7369c2c569673438164438b7a9a0acf",
          "sha256": "b3204610933a1d0f966dc98e884e193e4a2ff431066d9b082436ca2e7ccaa0fc",
          "bytes": 559697,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/references/gcfpe-20260914.1-091426.1-validation-profile.json",
          "git_blob": "3acf8c02adb39fe0c7b03579bc3ebf7fcaa6b55a",
          "sha256": "3a4742486c72905598c2c656f837757c2eaa8526d70966d8b8a910e4f74c7e85",
          "bytes": 2505,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/references/glow-hde-canonical-change-flow-r1.json",
          "git_blob": "f524143a0563bddc8cea08a26a72ce8aff754b24",
          "sha256": "52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e",
          "bytes": 52767,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/run_alpha_feedback_fixtures.py",
          "git_blob": "3229b2516179af0a1bc07c05a1df310f4d69b48d",
          "sha256": "35837bc8cd7ec7524b887399fbbc7e62ce424ead6680ef07148af0053af0957d",
          "bytes": 6268,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/run_change_flow_fixtures.py",
          "git_blob": "8701f6aeadb333977d774c9c224a476ad6293696",
          "sha256": "522f1b5c65bd011ce8a89668b1e9002a40c49935e99c6267567456310543ef17",
          "bytes": 3108,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/run_epic_alpha_fixtures.py",
          "git_blob": "3d6b95f262a8c9fa7d488517297587876fff6b57",
          "sha256": "efef2d10c1535639a896b10a3a7111addcf9a87cdf08840c4e937a3500f6ecf1",
          "bytes": 22899,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/run_final_scan_fixtures.py",
          "git_blob": "fd4f05338d14452dc7d2d9fdf546adce64acb81f",
          "sha256": "47aef4784685de2a30a6334ea9b5b8f47d93aeb67186807d254611336b78a491",
          "bytes": 5017,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/run_gcfpe_20260914_fixtures.py",
          "git_blob": "ab339489fcd5b98e2b778a7e57bfd7551282b511",
          "sha256": "2afeef2eef454245938b44683eee9411768b94b021f85ccee1198685ab7fb7ec",
          "bytes": 27806,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/run_gcfpe_current_fixtures.py",
          "git_blob": "b04130ce6fd5f0d497708e9f8f8d1dfca6914057",
          "sha256": "fa89aa6a5c9a2ddc69bd3a99da6ab24afb4617c485649778af6047a8580f77b6",
          "bytes": 14479,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/run_integrated_readiness_fixtures.py",
          "git_blob": "8476c4f0852673f9f71c6a0bd87a0df3a4694748",
          "sha256": "bd12286366ecdd90a15c04a87be35ff3f1143ee624bd69df550205318eabe1ac",
          "bytes": 8929,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/run_strength_middleware_fixtures.py",
          "git_blob": "67a9391606abe63fe8fd26f22d0e3f32ef456054",
          "sha256": "5949fa1c45da3a327c9c3909848fbfaf00456ca7875431052342409ca1c68df6",
          "bytes": 7500,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/validate_alpha_feedback.py",
          "git_blob": "de4eaea0b8809651c0dfeea846c38302e76cd026",
          "sha256": "9d192b9c9b2d060a4a98d5d73ce6db4d97a95444b14578417000293d188d27af",
          "bytes": 7245,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/validate_epic_alpha.py",
          "git_blob": "f25334be7d8f57fb4e2f2788410e3a82ee824234",
          "sha256": "0b751a9e469fc5f0d530587a59165da2da73a07c9ef14779094079804b8ff0d5",
          "bytes": 28772,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/validate_epic_reengineering.py",
          "git_blob": "25455079aaebfba29d98b3ee67d51a4871b53ba3",
          "sha256": "a66b81d707c92179abf6e609293aedf96352ef17400fd5d27c6f00f3495fda91",
          "bytes": 10533,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/validate_final_scan.py",
          "git_blob": "0f084303d2ba2a46cda87e225c2fe44d633dbc04",
          "sha256": "8254d5eef3a2bc43805709f3a16a978b9b7a9951b85138b72f843b8b31385a7f",
          "bytes": 5733,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/validate_flowmaster.py",
          "git_blob": "85d6ebd4da87b00bf94c900881d8dc168d9af4c5",
          "sha256": "4282f2835e37c8e14971457b697b395a99aa8a3896069852e40801a192186b39",
          "bytes": 58845,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/validate_gcfpe_20260914.py",
          "git_blob": "80ebbc00770b84d81decdb75f5efd9b8ed51468a",
          "sha256": "cb24997a326276c1e3703ebbc370278b513d6b50814e699cd9433622e5ae5c84",
          "bytes": 73909,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/validate_gcfpe_current.py",
          "git_blob": "8425d94ef782201370f0185cf706d329fb2e9082",
          "sha256": "c960c1d0b3499e2e19e7ceee9eda02d7b096d5c1fa010300d2a35d753b6d3c87",
          "bytes": 38758,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/validate_integrated_readiness.py",
          "git_blob": "d257d1d83f6a0b1bcfe3a7c1db0284d555247b17",
          "sha256": "c70565f3594336c7f6a82f46313c115fc34b82a805976bdb39ad806813d2a5ba",
          "bytes": 15106,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/validate_pre_guide_correction.py",
          "git_blob": "8669118dbfe145e32938a472437b2b4ea6cec197",
          "sha256": "bcb7904d9bba35dacaea56bf9dc47bfce3a2eb49e30b289113af5d6542bb88ca",
          "bytes": 5932,
          "remote_readback_equal": true
        },
        {
          "path": "skill-6a8f973972a88191ae25426f5a818169/scripts/validate_strength_middleware.py",
          "git_blob": "d25eba436e1e3407e2332f2b634d3f84432206e3",
          "sha256": "fbc31888f3d0dc987ed0fb8b9d9d13e876ddeb5294aa55c7669b55aeada9e965",
          "bytes": 13062,
          "remote_readback_equal": true
        }
      ]
    }
  ],
  "changeflow_binding_regression": {
    "schema": "gcfpe-installed-source-binding-recovery/1.0",
    "created_at": "2026-09-14T22:42:49.366764+00:00",
    "scope": "STATIC_INSTALLED_CANDIDATE_BINDING_AND_IN_MEMORY_NEGATIVE_TESTS_NOT_EXTERNAL_SOURCE_CERTIFICATION",
    "package": "skill-6a8f94d50bd08191ae150422fb3a6a2f",
    "base_commit": "517039dc7d2ddc2c4b0a8adbde83cae6cf3bb0be",
    "observed_head": "517039dc7d2ddc2c4b0a8adbde83cae6cf3bb0be",
    "contract_revision": "4.0.3",
    "skill_behavior_revision": "3.2.4 UNCHANGED; source resource and validator correction only",
    "contract_sha256": "b3204610933a1d0f966dc98e884e193e4a2ff431066d9b082436ca2e7ccaa0fc",
    "contract_bytes": 559697,
    "graph_sha256": "47439465a46866e4f0c98a648887a822913a3a8ad18be66b6651634fb90eb7cb",
    "graph_bytes": 518308,
    "contract_diffs": [
      {
        "path": "/canonical_source_contract/current_pf10/binding_role",
        "before": null,
        "after": "REPAIR_BASELINE_EVIDENCE_ONLY_FRESH_RUNTIME_RESOLUTION_REQUIRED"
      },
      {
        "path": "/canonical_source_contract/current_pf10/byte_count",
        "before": null,
        "after": 175083
      },
      {
        "path": "/canonical_source_contract/current_pf10/representation",
        "before": null,
        "after": "EXACT_RAW_DRIVE_FILE_BYTES"
      },
      {
        "path": "/canonical_source_contract/current_pf10/sha256",
        "before": "4a2545197cf6fec854f053ca888651b737384f4db11fde9e68eca91b4f4f0b48",
        "after": "4b2b0d198cecf6f4ece852c82951342e512124abfb93fa90678df8d97b4f4f86"
      },
      {
        "path": "/contract_revision",
        "before": "4.0.2",
        "after": "4.0.3"
      },
      {
        "path": "/source_snapshot/corrected_source_manifest",
        "before": null,
        "after": {
          "file_id": "14lL-wbaefBcieLxVLVsoMXyvk_DdZCcc",
          "url": "https://drive.google.com/file/d/14lL-wbaefBcieLxVLVsoMXyvk_DdZCcc/view?usp=drivesdk",
          "sha256": "252fbc9abf573af052e2572c77a3e8dac9725dc8a35c8acbc42d74ee9dca680a",
          "source_snapshot_sha256": "a8f3351c15279224af81eac4e013d7bbcc7436c3dd5b26b7385abd870f7160be",
          "role": "REPAIR_BASELINE_EVIDENCE_ONLY_NOT_RUNTIME_CURRENT_AUTHORITY"
        }
      },
      {
        "path": "/source_snapshot/frozen_candidate_graph/sha256",
        "before": "c746f3f0c0f6f7b4df4c7e845d2b491f01370693c8327a7d0a3f877ef6fe06f7",
        "after": "47439465a46866e4f0c98a648887a822913a3a8ad18be66b6651634fb90eb7cb"
      },
      {
        "path": "/source_snapshot/governing_plan/byte_count",
        "before": null,
        "after": 53118
      },
      {
        "path": "/source_snapshot/governing_plan/representation",
        "before": null,
        "after": "EXACT_RAW_DRIVE_FILE_BYTES"
      },
      {
        "path": "/source_snapshot/governing_plan/sha256",
        "before": "94478a230055b9119074086e225c7f09697448edb96155ca3859f11f42d4a80d",
        "after": "e14c9fa0574633186959c0f96dc62c7a28998336bf892f8046d6359820e7df01"
      }
    ],
    "graph_changes_only": [
      "authority_sources",
      "source_bindings"
    ],
    "fixtures": [
      {
        "id": "valid_corrected_installed_contract",
        "result": "PASS",
        "observed": "PASS: change-flow GCFPE-20260914.1 contract and Markdown-only source policy"
      },
      {
        "id": "reject_defective_pf10_digest",
        "result": "PASS",
        "observed": "FAIL: exact raw PF10 repair-baseline pin"
      },
      {
        "id": "reject_appended_lf_pf10_size",
        "result": "PASS",
        "observed": "FAIL: exact raw PF10 repair-baseline pin"
      },
      {
        "id": "reject_defective_plan_digest",
        "result": "PASS",
        "observed": "FAIL: exact raw governing-plan pin"
      },
      {
        "id": "reject_snapshot_disagreement",
        "result": "PASS",
        "observed": "FAIL: corrected source snapshot parity"
      },
      {
        "id": "reject_repair_pin_as_runtime_authority",
        "result": "PASS",
        "observed": "FAIL: repair pin is not runtime current authority"
      }
    ],
    "protected": [
      {
        "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/SKILL.md",
        "sha256": "57971dcd64b426cfc952a653ce10492a5d6840659f408a5e8fa5621444fb1042",
        "unchanged": true,
        "git_blob": "58fe1b906eec6d651b41b353356d9733cfa6e802"
      },
      {
        "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-current-direct-handoff-contract.json",
        "sha256": "2b4682b34d7323abf30a4b14fa81465fcf65501aa17959be49a6524f07a212e0",
        "unchanged": true,
        "git_blob": "08a78c4b9f251948ebe7b67bed22de7aa45750c0"
      },
      {
        "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/glow-hde-canonical-change-flow-r1-runtime-map.json",
        "sha256": "5574666e5975c104ccf13e77a13d94e0d16f37af37de7eb26d7e0f7b00f45b0e",
        "unchanged": true,
        "git_blob": "f2e2d484b4801f23ef6e9516bc5b3923d377d105"
      },
      {
        "path": "skill-6a8f9341ec3481918d531eca7d2d7f97/SKILL.md",
        "sha256": "30540aaf33501c1e24a9d380a5b45ac7e832bfc729bb56ca71ff7ff1e2947571",
        "unchanged": true,
        "git_blob": "872eb0046f19c5b0d07171681d84fecc6c9faaba"
      }
    ],
    "changed_files": [
      {
        "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json",
        "sha256": "47439465a46866e4f0c98a648887a822913a3a8ad18be66b6651634fb90eb7cb",
        "git_object_before": "cb0032807bd7e01091cc107a5890abf260a3a0a7",
        "git_object_after": "2dde65ae34f0b9cda6fb541815d800ad98f1b8a8"
      },
      {
        "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json",
        "sha256": "b3204610933a1d0f966dc98e884e193e4a2ff431066d9b082436ca2e7ccaa0fc",
        "git_object_before": "8eb6f67841cc0b9ad868cc335dd844e98012c85a",
        "git_object_after": "97b4b8b4c7369c2c569673438164438b7a9a0acf"
      },
      {
        "path": "skill-6a8f94d50bd08191ae150422fb3a6a2f/scripts/validate_gcfpe_20260914.py",
        "sha256": "1925788ed31d1eb470b45e6c047295e7b5e5ba49d4995a759ab3cf2fd1f33b2e",
        "git_object_before": "6ab682b97f82c337f5355e3f986b6467daaf76ef",
        "git_object_after": "312d7ae5c66dfdd8536f3bf49f6423e30b9fc66e"
      }
    ],
    "diff": "diff --git a/skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json b/skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json\nindex cb00328..2dde65a 100644\n--- a/skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json\n+++ b/skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json\n@@ -30,7 +30,7 @@\n     \"state\": \"ALPHA_STOPPED_PENDING_CHANGE_FLOW_REFACTOR\"\n   },\n   \"authority_sources\": [\n-    \"baseline/core/GCFPE-Change-Flow-Repair-Plan-v2.0-20260914.md §§5–8\",\n+    \"recovery-20260914.1/sources/drive/1QfCDo6pw3_FRjJi5qTooLaxgLThFcURI-repin.md §§5–8\",\n     \"candidate/contracts/GCFPE-20260914.1-Candidate-Authoring-Contract.md\",\n     \"baseline/preflight/project-prompt-registry.yaml\"\n   ],\n@@ -10055,6 +10055,158 @@\n   },\n   \"schema_version\": \"gcfpe-candidate-graph-contract/2.1\",\n   \"selection_status\": \"UNSELECTED_CANDIDATE\",\n+  \"source_bindings\": {\n+    \"binding_revision\": \"20260914.1-recovery.1\",\n+    \"binding_scope\": \"REPAIR_BASELINE_EVIDENCE_ONLY_NOT_A_RUNTIME_CURRENT_PF10_ALIAS\",\n+    \"bindings\": [\n+      {\n+        \"external_id\": \"1MEMi5OTUr-c7Qd3rtjntnNjSpnxfIXJ4\",\n+        \"parent_ids\": [\n+          \"1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3\"\n+        ],\n+        \"path\": \"recovery-20260914.1/sources/drive/1MEMi5OTUr-c7Qd3rtjntnNjSpnxfIXJ4.md\",\n+        \"provider_size_bytes\": 354325,\n+        \"representation\": \"EXACT_RAW_DRIVE_FILE_BYTES\",\n+        \"retrieved_at\": \"2026-09-14T21:29:11.721Z\",\n+        \"sha256\": \"4f4f015bc8fe8c0a9f7d518fce13b7428a1427b49ca463982b769827169b22a0\",\n+        \"size_bytes\": 354325,\n+        \"source_id\": \"drive:1MEMi5OTUr-c7Qd3rtjntnNjSpnxfIXJ4\",\n+        \"title\": \"PF27-Canon-Plan-Templates-v2.0.5.md\",\n+        \"url\": \"https://drive.google.com/file/d/1MEMi5OTUr-c7Qd3rtjntnNjSpnxfIXJ4/view?usp=drivesdk\"\n+      },\n+      {\n+        \"external_id\": \"1PUqOyiY285Yo4dxq3JucrzakiNTNLc-j\",\n+        \"parent_ids\": [\n+          \"1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3\"\n+        ],\n+        \"path\": \"recovery-20260914.1/sources/drive/1PUqOyiY285Yo4dxq3JucrzakiNTNLc-j.md\",\n+        \"provider_size_bytes\": 26815,\n+        \"representation\": \"EXACT_RAW_DRIVE_FILE_BYTES\",\n+        \"retrieved_at\": \"2026-09-14T21:29:14.265Z\",\n+        \"sha256\": \"106c50bb2e06702c1c72764ccece3d5c500bddf4b553e12afa0c4d1f8c7a4c21\",\n+        \"size_bytes\": 26815,\n+        \"source_id\": \"drive:1PUqOyiY285Yo4dxq3JucrzakiNTNLc-j\",\n+        \"title\": \"PF13- Reference-Glow-Development-Philosophy v1.md\",\n+        \"url\": \"https://drive.google.com/file/d/1PUqOyiY285Yo4dxq3JucrzakiNTNLc-j/view?usp=drivesdk\"\n+      },\n+      {\n+        \"external_id\": \"1PfbPLcgsI5T7UbbPK1bJNvcdsf3vMzsQ\",\n+        \"parent_ids\": [\n+          \"1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3\"\n+        ],\n+        \"path\": \"recovery-20260914.1/sources/drive/1PfbPLcgsI5T7UbbPK1bJNvcdsf3vMzsQ.md\",\n+        \"provider_size_bytes\": 619584,\n+        \"representation\": \"EXACT_RAW_DRIVE_FILE_BYTES\",\n+        \"retrieved_at\": \"2026-09-14T21:29:16.935Z\",\n+        \"sha256\": \"90e6af98fd18ce3ab4e91cb16fcfefbdb5bdf539690d8726f8e47359238bf853\",\n+        \"size_bytes\": 619584,\n+        \"source_id\": \"drive:1PfbPLcgsI5T7UbbPK1bJNvcdsf3vMzsQ\",\n+        \"title\": \"PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md\",\n+        \"url\": \"https://drive.google.com/file/d/1PfbPLcgsI5T7UbbPK1bJNvcdsf3vMzsQ/view?usp=drivesdk\"\n+      },\n+      {\n+        \"external_id\": \"1Q83saZ9QqxG9c9slV6bYkfDiCXLSK4Lp\",\n+        \"parent_ids\": [\n+          \"1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3\"\n+        ],\n+        \"path\": \"recovery-20260914.1/sources/drive/1Q83saZ9QqxG9c9slV6bYkfDiCXLSK4Lp.md\",\n+        \"provider_size_bytes\": 558988,\n+        \"representation\": \"EXACT_RAW_DRIVE_FILE_BYTES\",\n+        \"retrieved_at\": \"2026-09-14T21:29:20.208Z\",\n+        \"sha256\": \"e8234398902ab47e3492d54a83d79ef5e2d17399dee8ad03d0688aec98a23696\",\n+        \"size_bytes\": 558988,\n+        \"source_id\": \"drive:1Q83saZ9QqxG9c9slV6bYkfDiCXLSK4Lp\",\n+        \"title\": \"PF04-Canon-HDE-Governance-v2.8.6.md\",\n+        \"url\": \"https://drive.google.com/file/d/1Q83saZ9QqxG9c9slV6bYkfDiCXLSK4Lp/view?usp=drivesdk\"\n+      },\n+      {\n+        \"external_id\": \"1XdZYpx0Kcuu800fW0Yhi7aicD4wU_dJt\",\n+        \"parent_ids\": [\n+          \"1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3\"\n+        ],\n+        \"path\": \"recovery-20260914.1/sources/drive/1XdZYpx0Kcuu800fW0Yhi7aicD4wU_dJt.md\",\n+        \"provider_size_bytes\": 657008,\n+        \"representation\": \"EXACT_RAW_DRIVE_FILE_BYTES\",\n+        \"retrieved_at\": \"2026-09-14T21:29:23.438Z\",\n+        \"sha256\": \"2a4a254422da92933e7f4dce9e074bcd7e1a1a6609ed54a7897d3f5f8cc059d0\",\n+        \"size_bytes\": 657008,\n+        \"source_id\": \"drive:1XdZYpx0Kcuu800fW0Yhi7aicD4wU_dJt\",\n+        \"title\": \"PF19-Canon-Glow-QA-Guide-v3.0.5.md\",\n+        \"url\": \"https://drive.google.com/file/d/1XdZYpx0Kcuu800fW0Yhi7aicD4wU_dJt/view?usp=drivesdk\"\n+      },\n+      {\n+        \"external_id\": \"1_ej-UY2JaKS1vFnxMfSKnK881Y_hzlrP\",\n+        \"parent_ids\": [\n+          \"1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3\"\n+        ],\n+        \"path\": \"recovery-20260914.1/sources/drive/1_ej-UY2JaKS1vFnxMfSKnK881Y_hzlrP.md\",\n+        \"provider_size_bytes\": 175083,\n+        \"representation\": \"EXACT_RAW_DRIVE_FILE_BYTES\",\n+        \"retrieved_at\": \"2026-09-14T21:29:09.197Z\",\n+        \"sha256\": \"4b2b0d198cecf6f4ece852c82951342e512124abfb93fa90678df8d97b4f4f86\",\n+        \"size_bytes\": 175083,\n+        \"source_id\": \"drive:1_ej-UY2JaKS1vFnxMfSKnK881Y_hzlrP\",\n+        \"title\": \"PF10-HDE-Build-Notes-v13.2.6.md\",\n+        \"url\": \"https://drive.google.com/file/d/1_ej-UY2JaKS1vFnxMfSKnK881Y_hzlrP/view?usp=drivesdk\"\n+      },\n+      {\n+        \"external_id\": \"1f9hWZbmKVt6bMDs4RbdGAONFC_r06yR9\",\n+        \"parent_ids\": [\n+          \"1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3\"\n+        ],\n+        \"path\": \"recovery-20260914.1/sources/drive/1f9hWZbmKVt6bMDs4RbdGAONFC_r06yR9.md\",\n+        \"provider_size_bytes\": 395891,\n+        \"representation\": \"EXACT_RAW_DRIVE_FILE_BYTES\",\n+        \"retrieved_at\": \"2026-09-14T21:29:26.388Z\",\n+        \"sha256\": \"ad238a8fc07af27bcecf5afce71368766d96d0d40104649b2a005a0f721dd2f9\",\n+        \"size_bytes\": 395891,\n+        \"source_id\": \"drive:1f9hWZbmKVt6bMDs4RbdGAONFC_r06yR9\",\n+        \"title\": \"PF06-Canon-Change-Process-Guide-v2.5.4.md\",\n+        \"url\": \"https://drive.google.com/file/d/1f9hWZbmKVt6bMDs4RbdGAONFC_r06yR9/view?usp=drivesdk\"\n+      },\n+      {\n+        \"external_id\": \"1zYQC27hl7ynq8b2cWGlQ4kkIRBGxaWmI\",\n+        \"parent_ids\": [\n+          \"1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3\"\n+        ],\n+        \"path\": \"recovery-20260914.1/sources/drive/1zYQC27hl7ynq8b2cWGlQ4kkIRBGxaWmI.md\",\n+        \"provider_size_bytes\": 10375,\n+        \"representation\": \"EXACT_RAW_DRIVE_FILE_BYTES\",\n+        \"retrieved_at\": \"2026-09-14T21:29:29.374Z\",\n+        \"sha256\": \"391bf7d2eb51022e22edb69b90a2ed6eaa63f621dedcf817513c2ae1a0c77e24\",\n+        \"size_bytes\": 10375,\n+        \"source_id\": \"drive:1zYQC27hl7ynq8b2cWGlQ4kkIRBGxaWmI\",\n+        \"title\": \"PF21-Reference-7 Phases of Alchemical Engineering.md\",\n+        \"url\": \"https://drive.google.com/file/d/1zYQC27hl7ynq8b2cWGlQ4kkIRBGxaWmI/view?usp=drivesdk\"\n+      },\n+      {\n+        \"external_id\": \"1QfCDo6pw3_FRjJi5qTooLaxgLThFcURI\",\n+        \"parent_ids\": [\n+          \"1pRJ8R1a-p5dYQFY89a1YyJpDceYZ2MLc\"\n+        ],\n+        \"path\": \"recovery-20260914.1/sources/drive/1QfCDo6pw3_FRjJi5qTooLaxgLThFcURI-repin.md\",\n+        \"provider_size_bytes\": 53118,\n+        \"representation\": \"EXACT_RAW_DRIVE_FILE_BYTES\",\n+        \"retrieved_at\": \"2026-09-14T21:48:21.881Z\",\n+        \"sha256\": \"e14c9fa0574633186959c0f96dc62c7a28998336bf892f8046d6359820e7df01\",\n+        \"size_bytes\": 53118,\n+        \"source_id\": \"drive:1QfCDo6pw3_FRjJi5qTooLaxgLThFcURI\",\n+        \"title\": \"GCFPE-Change-Flow-Repair-Plan-v2.0-20260914.md\",\n+        \"url\": \"https://drive.google.com/file/d/1QfCDo6pw3_FRjJi5qTooLaxgLThFcURI/view?usp=drivesdk\"\n+      }\n+    ],\n+    \"candidate_release\": \"GCFPE-20260914.1\",\n+    \"candidate_version_family\": \"091426.1\",\n+    \"correction_report_url\": \"https://drive.google.com/file/d/1BlPiTmlfSdtpkgSkKm9pHaPSvyL4L6br/view?usp=drivesdk\",\n+    \"prior_capture_disposition\": \"HISTORICAL_DEFECTIVE_RAW_CAPTURE_PLUS_ONE_LF_NOT_AUTHORITY\",\n+    \"runtime_rule\": \"Each affected runtime receiver must freshly resolve current controlled PF10 after manual drain; these historical repair pins never replace that lookup.\",\n+    \"schema_version\": \"gcfpe-recovery-source-bindings/1.0\",\n+    \"selection_status\": \"UNSELECTED_CANDIDATE\",\n+    \"source_manifest_file_sha256\": \"252fbc9abf573af052e2572c77a3e8dac9725dc8a35c8acbc42d74ee9dca680a\",\n+    \"source_manifest_url\": \"https://drive.google.com/file/d/14lL-wbaefBcieLxVLVsoMXyvk_DdZCcc/view?usp=drivesdk\",\n+    \"source_snapshot_id\": \"GCFPE-REPAIR-RECOVERY-CORRECTION-20260914.1\",\n+    \"source_snapshot_sha256\": \"a8f3351c15279224af81eac4e013d7bbcc7436c3dd5b26b7385abd870f7160be\"\n+  },\n   \"state_routes\": {\n     \"CF-C-10\": [\n       {\ndiff --git a/skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json b/skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json\nindex 8eb6f67..97b4b8b 100644\n--- a/skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json\n+++ b/skill-6a8f94d50bd08191ae150422fb3a6a2f/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json\n@@ -1,7 +1,7 @@\n {\n   \"schema_version\": \"gcfpe-direct-handoff-contract/4.0\",\n   \"contract_id\": \"GCFPE-20260914.1-091426.1-DIRECT-HANDOFF-CANDIDATE\",\n-  \"contract_revision\": \"4.0.2\",\n+  \"contract_revision\": \"4.0.3\",\n   \"status\": \"UNSELECTED_CANDIDATE\",\n   \"selection_status\": \"UNSELECTED_CANDIDATE\",\n   \"publication_evidence\": false,\n@@ -79,12 +79,14 @@\n       \"title\": \"GCFPE Change Flow Repair Plan v2.0 — 20260914\",\n       \"drive_file_id\": \"1QfCDo6pw3_FRjJi5qTooLaxgLThFcURI\",\n       \"url\": \"https://drive.google.com/file/d/1QfCDo6pw3_FRjJi5qTooLaxgLThFcURI/view?usp=drivesdk\",\n-      \"sha256\": \"94478a230055b9119074086e225c7f09697448edb96155ca3859f11f42d4a80d\"\n+      \"sha256\": \"e14c9fa0574633186959c0f96dc62c7a28998336bf892f8046d6359820e7df01\",\n+      \"byte_count\": 53118,\n+      \"representation\": \"EXACT_RAW_DRIVE_FILE_BYTES\"\n     },\n     \"frozen_candidate_graph\": {\n       \"path\": \"references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json\",\n       \"contract_id\": \"GCFPE-20260914.1-CANDIDATE-GRAPH\",\n-      \"sha256\": \"c746f3f0c0f6f7b4df4c7e845d2b491f01370693c8327a7d0a3f877ef6fe06f7\",\n+      \"sha256\": \"47439465a46866e4f0c98a648887a822913a3a8ad18be66b6651634fb90eb7cb\",\n       \"external_source_path\": \"candidate/graph/GCFPE-20260914.1-Candidate-Graph-Contract.json\",\n       \"schema_version\": \"gcfpe-candidate-graph-contract/2.1\"\n     },\n@@ -99,6 +101,13 @@\n       \"role\": \"HISTORICAL_SELECTED_PREDECESSOR_EVIDENCE\"\n     },\n     \"complete_source_required\": true,\n+    \"corrected_source_manifest\": {\n+      \"file_id\": \"14lL-wbaefBcieLxVLVsoMXyvk_DdZCcc\",\n+      \"url\": \"https://drive.google.com/file/d/14lL-wbaefBcieLxVLVsoMXyvk_DdZCcc/view?usp=drivesdk\",\n+      \"sha256\": \"252fbc9abf573af052e2572c77a3e8dac9725dc8a35c8acbc42d74ee9dca680a\",\n+      \"source_snapshot_sha256\": \"a8f3351c15279224af81eac4e013d7bbcc7436c3dd5b26b7385abd870f7160be\",\n+      \"role\": \"REPAIR_BASELINE_EVIDENCE_ONLY_NOT_RUNTIME_CURRENT_AUTHORITY\"\n+    },\n     \"prompt_topology_move_readback\": {\n       \"path\": \"references/gcfpe-20260914.1-091426.1-prompt-topology-readback.json\",\n       \"sha256\": \"705f5acfad74c9b32b91f4305e64372098f5cd82d7cd91f2388888ca7db661e3\",\n@@ -168,7 +177,10 @@\n       \"version\": \"13.2.6\",\n       \"file_id\": \"1_ej-UY2JaKS1vFnxMfSKnK881Y_hzlrP\",\n       \"url\": \"https://drive.google.com/file/d/1_ej-UY2JaKS1vFnxMfSKnK881Y_hzlrP/view?usp=drivesdk\",\n-      \"sha256\": \"4a2545197cf6fec854f053ca888651b737384f4db11fde9e68eca91b4f4f0b48\",\n+      \"sha256\": \"4b2b0d198cecf6f4ece852c82951342e512124abfb93fa90678df8d97b4f4f86\",\n+      \"byte_count\": 175083,\n+      \"representation\": \"EXACT_RAW_DRIVE_FILE_BYTES\",\n+      \"binding_role\": \"REPAIR_BASELINE_EVIDENCE_ONLY_FRESH_RUNTIME_RESOLUTION_REQUIRED\",\n       \"direct_parent_id\": \"1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3\"\n     },\n     \"pre_drain_reference_role\": \"PRE_DRAIN_BASELINE_EVIDENCE\",\ndiff --git a/skill-6a8f94d50bd08191ae150422fb3a6a2f/scripts/validate_gcfpe_20260914.py b/skill-6a8f94d50bd08191ae150422fb3a6a2f/scripts/validate_gcfpe_20260914.py\nindex 6ab682b..312d7ae 100644\n--- a/skill-6a8f94d50bd08191ae150422fb3a6a2f/scripts/validate_gcfpe_20260914.py\n+++ b/skill-6a8f94d50bd08191ae150422fb3a6a2f/scripts/validate_gcfpe_20260914.py\n@@ -17,7 +17,9 @@ GRAPH = ROOT / \"references\" / \"gcfpe-20260914.1-091426.1-candidate-graph-contrac\n URL_MAP = ROOT / \"references\" / \"gcfpe-20260914.1-091426.1-prompt-url-map.json\"\n TOPOLOGY_READBACK = ROOT / \"references\" / \"gcfpe-20260914.1-091426.1-prompt-topology-readback.json\"\n SOURCE_POLICY = ROOT / \"scripts\" / \"pf_header_parity.py\"\n-EXPECTED_GRAPH_SHA = \"c746f3f0c0f6f7b4df4c7e845d2b491f01370693c8327a7d0a3f877ef6fe06f7\"\n+EXPECTED_GRAPH_SHA = \"47439465a46866e4f0c98a648887a822913a3a8ad18be66b6651634fb90eb7cb\"\n+EXPECTED_PLAN_SHA = \"e14c9fa0574633186959c0f96dc62c7a28998336bf892f8046d6359820e7df01\"\n+EXPECTED_PF10_SHA = \"4b2b0d198cecf6f4ece852c82951342e512124abfb93fa90678df8d97b4f4f86\"\n EXPECTED_URL_MAP_SHA = \"d9173a288105d69686ae8de6b61d3c0ae9925fd44204fa3393d2f431d106f397\"\n EXPECTED_TOPOLOGY_SHA = \"705f5acfad74c9b32b91f4305e64372098f5cd82d7cd91f2388888ca7db661e3\"\n EXPECTED_CORE_SHA = \"495c2ca6f33a8b6b837754a518b1cbc64570e9c911e137fd5b81004d487e498c\"\n@@ -80,9 +82,22 @@ def main() -> None:\n     require(\"Do not infer a `Glow / Ops` procedure route\" in skill, \"no inferred Ops procedure route\")\n     require(sha256(marked_core(skill_bytes)) == EXPECTED_CORE_SHA, \"protected Primary core SHA\")\n     require(contract[\"target_release\"] == \"GCFPE-20260914.1\", \"target release\")\n+    require(contract[\"contract_revision\"] == \"4.0.3\", \"corrected-source contract revision\")\n     require(contract[\"prompt_version\"] == \"091426.1\", \"prompt family\")\n     require(contract[\"candidate_member_count\"] == 55, \"candidate member count\")\n     require(contract[\"selection_status\"] == \"UNSELECTED_CANDIDATE\", \"candidate lifecycle\")\n+    plan = contract[\"source_snapshot\"][\"governing_plan\"]\n+    pf10 = contract[\"canonical_source_contract\"][\"current_pf10\"]\n+    require(plan[\"sha256\"] == EXPECTED_PLAN_SHA and plan[\"byte_count\"] == 53118, \"exact raw governing-plan pin\")\n+    require(pf10[\"sha256\"] == EXPECTED_PF10_SHA and pf10[\"byte_count\"] == 175083, \"exact raw PF10 repair-baseline pin\")\n+    require(plan[\"representation\"] == pf10[\"representation\"] == \"EXACT_RAW_DRIVE_FILE_BYTES\", \"raw source representations\")\n+    require(pf10[\"binding_role\"] == \"REPAIR_BASELINE_EVIDENCE_ONLY_FRESH_RUNTIME_RESOLUTION_REQUIRED\", \"repair pin is not runtime current authority\")\n+    manifest = contract[\"source_snapshot\"][\"corrected_source_manifest\"]\n+    require(manifest[\"sha256\"] == graph[\"source_bindings\"][\"source_manifest_file_sha256\"], \"corrected source manifest parity\")\n+    require(manifest[\"source_snapshot_sha256\"] == graph[\"source_bindings\"][\"source_snapshot_sha256\"], \"corrected source snapshot parity\")\n+    bindings = {row[\"external_id\"]: row for row in graph[\"source_bindings\"][\"bindings\"]}\n+    require(bindings[plan[\"drive_file_id\"]][\"sha256\"] == EXPECTED_PLAN_SHA, \"graph governing-plan pin\")\n+    require(bindings[pf10[\"file_id\"]][\"sha256\"] == EXPECTED_PF10_SHA, \"graph PF10 pin\")\n     require(sha256(graph_bytes) == EXPECTED_GRAPH_SHA, \"bundled graph bytes\")\n     require(sha256(url_map_bytes) == EXPECTED_URL_MAP_SHA, \"bundled URL-map bytes\")\n     require(sha256(topology_bytes) == EXPECTED_TOPOLOGY_SHA, \"bundled topology-readback bytes\")\n",
    "result": "PASS"
  },
  "candidate_validator": {
    "candidate_member_count": 55,
    "contract_sha256": "b3204610933a1d0f966dc98e884e193e4a2ff431066d9b082436ca2e7ccaa0fc",
    "contract_status": "UNSELECTED_CANDIDATE",
    "errors": [],
    "frozen_graph_edge_count": 230,
    "frozen_graph_node_count": 55,
    "frozen_graph_sha256": "47439465a46866e4f0c98a648887a822913a3a8ad18be66b6651634fb90eb7cb",
    "ok": true,
    "pf10_producers": [
      "CF-C-30",
      "CF-E-30",
      "ESC-40",
      "IA-30",
      "QA-70",
      "RS-20"
    ],
    "plan_writers": [
      "CF-C-20",
      "CF-C-40",
      "CF-E-20",
      "CF-E-40",
      "ESC-30",
      "IA-10",
      "IA-20",
      "IA-40",
      "PR-10",
      "PR-20",
      "QA-20",
      "QA-50",
      "QA-60",
      "QA-80"
    ],
    "profile": "GCFPE-20260914.1-091426.1-VALIDATION",
    "prompt_bodies_validated": true,
    "prompt_body_count": 55,
    "prompt_body_sha256": {
      "CF-C-10": "ac7746cb6f1e0d86edfd1703e1e4be81fa13f11fa0e4ac05a3c440b3793a73f2",
      "CF-C-20": "f3ad94f78b28a8609a22ee4d89998a9d5b2bcc9efdad3d29bbcc4c2f02b82539",
      "CF-C-30": "d12dab750df7fb492f937f019ed811516ef02d799622fbdad46e150bd4703064",
      "CF-C-40": "e30af7f63785bee5b9258b2d9317cf9d3f879d48c3eb40cc7bd70d0b10630f13",
      "CF-E-10": "e40f7571a569fa6331b39c4b47a0385945c0a87f06580085de9c76cc600782d2",
      "CF-E-20": "534756d5a7ba78c3695c26014164b838a088e489509a5833761b929a9769e8ff",
      "CF-E-30": "03621506ee52fe8526911c2fb46985606fde6aa196e0b771b7ae0b8c1bac53a4",
      "CF-E-40": "16c379f6d98abcf8cd819d539822e498433575e4686aa2ee27be7fd24178e8fe",
      "CF-PO-10": "d55ff76e2350634dfbd5c630adff7e9960f8d09555584f9441a4cb7718848f8d",
      "CL-20": "4f57d2292e3e44fc242f0b3af2b6a914a66f657767b89bf775bc4b430835df2d",
      "CL-30": "d39b4bc9d04db4258c2848097cf02ae2e20f7efeedc257cb148d31934ee64019",
      "CL-40": "0ac50c1fb41d4f846ae5bdbe190d62675c8c8d2b94899f41c40490f4e906b1c7",
      "CL-C-10": "bcbfffd5d2d65bdaf679f91a8b04a1581432e9cbd4a27895711b2b171deb7919",
      "CL-E-10": "67c97542ac5ae9c6c2da58d5a2f24826e918bcee8d7d3cdc5a04292b8017174d",
      "CL-E-20": "f48b1b862d46e331474ab0605d6e2475553aaa80141f7d70580f8540e8e448ad",
      "CL-E-30": "6c95b7694f90e866f19b0deb20ac15aae1132c0f4a4b65eec5235c15d7d1a4f0",
      "CL-E-40": "c9bd26b2655e7e678033ecdf3a9537f9e049332aca8e620ef8b791b2abda841f",
      "DOC-10": "d58b0799674ef65d43220de6617023fd3864d8e094958ada6c176d1b807604ee",
      "DOC-20": "a573a6fe0ec9112d4c9a1766e0d1f4860c791e69bb8fc687f281fc00dae7f582",
      "ESC-10": "b17995c37df63c50c2ec18283691b35b763050588c1b2b500291375349f7a8cf",
      "ESC-25": "9501b12844adbb23dd0f318a294577b9a5584d1f5c85ec568cc3477cd31c0764",
      "ESC-30": "7545d97147dd4cb4c73536948c3ea04afbf4c1e44c7185ad5ce8a5b5b5d51577",
      "ESC-40": "0354325faacfa0c1f48d842422dbe1d675799397a747d34b25c23cb4c9cb5037",
      "GCFPE-MGMT-10": "d50febce248792450f33f43113a470c9d45e734626230fa3db31cb2ca500b4e8",
      "IA-10": "91dab36d0d5e885a0868dae11e54ff080558b6f7cea57aae1575930d0d4224b6",
      "IA-20": "e3d1125537428cd11aeeb9c67e330e99da535f5f53f443775d8b5e6851ea0a6f",
      "IA-30": "eea92923da5ccafa8f39c538ec0669ef451b10306d7087786274ca2b67fcf242",
      "IA-40": "1db8ab68e6486aa19767bf5f32377170ea43cbc6632e15341b0c02d7706c1ba6",
      "IA-50": "f23bea75941bb6656e7f91184e9e5f0ac9a9590dfb03873f1f8a159a3b31c02c",
      "IA-60": "7f71aac8b97a74c6f797442eedf4270401d39522c9d9f1e84590dc41a727347c",
      "MGR-10": "6f8ab2e44347735cf0428f30e2be629a72426405412b94fe9b00e372a7c792cf",
      "OPS-10": "71e8de8e6ad822ce91159de9a7c3e008beede1536f047827280e04b172cc79ce",
      "OPS-20": "a2b585d096ce1037e140cb9c506e80f60a58f5ce6f982c18cd9aecce0a86abca",
      "OPS-30": "cdc21652c7b425b58b5af17dc65b527050bd774add225cdf0ce6d5667ecff271",
      "PR-10": "deb1c6f7d8733e5d5b630a2e5aba79922665fbb20b7c4e87f230ffd4194ef4aa",
      "PR-20": "d71cd112bc4c3b561fb05382bd1ffcdd7afdd01e8a8f31c3b8d39117e0cd745c",
      "PR-30": "2294b0220835fc36981dedd2eaaf04e58834b2b61ac3b7cb21e8c80f39fe474d",
      "PR-35": "c4212335c155a3c5346dd1fd2db7b77820f3203b56edd62ed44c0b193ea24bcc",
      "PR-40": "18e2c57c28ba2ead6c9e11aaaf7149c21cab8922e9d500393d8cdde64746a594",
      "PR-50": "d3acbf0943f58e88be3bf2a8e10dfdf9bd17210d90deef4a2d39ab6ccdc2b194",
      "QA-10": "9c1f64e37d65a54ef52f87cb7550b6c1631d161a8f6f26de51e1e62ecf09d20c",
      "QA-100": "398ee5931680152bbe386e0c201170cfcd35d6ebdaeafd8d2ffdea04bc82f650",
      "QA-110": "429351e900b4ff4a8048f58f4d090900c6d6fe074971b775b83cdcb0662e1af5",
      "QA-120": "25a9590701adc5d8217f7b5bd6b22ed3c7947a6a67ec8e2443d76a0992372a55",
      "QA-20": "3b3c300ebcc6d73b3a9d03d2236fb62a4ec95a5b9303e7c0739b49df7824b308",
      "QA-50": "adf0c45e0548a90d659e04a3835c85ffd4641bbe28df0831f3f87dbe1c839628",
      "QA-60": "98f385fd78602db3ed6d85dbbbdf335bc9a9411393609cdaeabf2aee7bdbd5c5",
      "QA-70": "d8bd5353331e457ac1d17c5b7ac67e5107a00d41f62c596fa26198de61bf0aab",
      "QA-80": "c04a2618acbb675e188bf7b39debca52dbeb3d184952b3a6d9bdc0b5282e2c84",
      "QA-90": "a1d52e2fb04bb279d533dfde6345bba219ff1fa310778edb92c50ea5c04a3e7c",
      "RS-10": "855dc1733922613df0449fc092ab56d9c248ed5fc2bd21d8e91e7c1fe4e61c29",
      "RS-20": "56b465b76dc342ba4b17b5bedd9849df7ef82b1d9b8c9b4ef79927168703dad2",
      "RS-30": "5159506c242aff06f57aea78a87ef42a6ca735eabae9e5d007dfc2e633d58700",
      "RS-40": "aa21d25ab08226c2a410236fc89766a562d02f93f34aaa3e33dd22f7e83a7ebf",
      "UTIL-10": "c654986cd5b0e3a056179b4ac5c910a9ad217ddf20b4283de0840ac074d994b9"
    },
    "prompt_version": "091426.1",
    "selected_alias_during_staging": {
      "member_count": 54,
      "prompt_version": "091326.2",
      "target_release": "GCFPE-20260913.1"
    },
    "selected_member_count": null,
    "selection_status": "UNSELECTED_CANDIDATE",
    "target_release": "GCFPE-20260914.1"
  },
  "candidate_fixtures": {
    "case_count": 126,
    "cases": [
      {
        "errors": [],
        "name": "section-13-fixture-document",
        "passed": true
      },
      {
        "errors": [],
        "name": "clean-versioned-contract",
        "passed": true
      },
      {
        "expected": "PR30_TO_PR35_SAME_SESSION",
        "expected_rule": null,
        "fixture_id": "PR-SPLIT-POS-01",
        "name": "PR-SPLIT-POS-01",
        "observed": "PR30_TO_PR35_SAME_SESSION",
        "passed": true,
        "polarity": "POSITIVE"
      },
      {
        "expected": "RECOVER_EXISTING_NO_DUPLICATE",
        "expected_rule": null,
        "fixture_id": "PR-SPLIT-POS-02",
        "name": "PR-SPLIT-POS-02",
        "observed": "RECOVER_EXISTING_NO_DUPLICATE",
        "passed": true,
        "polarity": "POSITIVE"
      },
      {
        "expected": "VALIDATION_FAILURE",
        "expected_rule": "PR35_ADDED_BOUNDARY",
        "fixture_id": "PR-SPLIT-NEG-01",
        "name": "PR-SPLIT-NEG-01",
        "observed": "VALIDATION_FAILURE",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "VALIDATION_FAILURE",
        "expected_rule": "PR35_ADDED_BOUNDARY",
        "fixture_variant": "PR-SPLIT-NEG-01",
        "name": "PR-SPLIT-NEG-01::extra-proceed-only",
        "observed": "VALIDATION_FAILURE",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "VALIDATION_FAILURE",
        "expected_rule": "PR35_ADDED_BOUNDARY",
        "fixture_variant": "PR-SPLIT-NEG-01",
        "name": "PR-SPLIT-NEG-01::new-session-only",
        "observed": "VALIDATION_FAILURE",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "VALIDATION_FAILURE",
        "expected_rule": "PR30_COHERENT_PUBLICATION",
        "fixture_id": "PR-SPLIT-NEG-02",
        "name": "PR-SPLIT-NEG-02",
        "observed": "VALIDATION_FAILURE",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "REVIEW_FIRST_COHERENT_PUSH",
        "expected_rule": null,
        "fixture_id": "PR-COST-POS-01",
        "name": "PR-COST-POS-01",
        "observed": "REVIEW_FIRST_COHERENT_PUSH",
        "passed": true,
        "polarity": "POSITIVE"
      },
      {
        "expected": "STALE_CI_LOCAL_CORRECTION",
        "expected_rule": null,
        "fixture_id": "PR-COST-POS-02",
        "name": "PR-COST-POS-02",
        "observed": "STALE_CI_LOCAL_CORRECTION",
        "passed": true,
        "polarity": "POSITIVE"
      },
      {
        "expected": "VALIDATION_FAILURE",
        "expected_rule": "PR_ACTION_ECONOMY",
        "fixture_id": "PR-COST-NEG-01",
        "name": "PR-COST-NEG-01",
        "observed": "VALIDATION_FAILURE",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "VALIDATION_FAILURE",
        "expected_rule": "PR_ACTION_ECONOMY",
        "fixture_variant": "PR-COST-NEG-01",
        "name": "PR-COST-NEG-01::micro-commit-only",
        "observed": "VALIDATION_FAILURE",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "VALIDATION_FAILURE",
        "expected_rule": "PR_ACTION_ECONOMY",
        "fixture_variant": "PR-COST-NEG-01",
        "name": "PR-COST-NEG-01::per-edit-push-only",
        "observed": "VALIDATION_FAILURE",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "VALIDATION_FAILURE",
        "expected_rule": "PR_SKIP_CI_AUTHORITY",
        "fixture_id": "PR-COST-NEG-02",
        "name": "PR-COST-NEG-02",
        "observed": "VALIDATION_FAILURE",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "MERGE_PENDING",
        "expected_rule": null,
        "fixture_id": "PR-READY-POS-01",
        "name": "PR-READY-POS-01",
        "observed": "MERGE_PENDING",
        "passed": true,
        "polarity": "POSITIVE"
      },
      {
        "expected": "VALIDATION_FAILURE",
        "expected_rule": "PR_MERGE_AUTHORITY",
        "fixture_id": "PR-MERGE-NEG-01",
        "name": "PR-MERGE-NEG-01",
        "observed": "VALIDATION_FAILURE",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "VALIDATION_FAILURE",
        "expected_rule": "PR_MERGE_AUTHORITY",
        "fixture_variant": "PR-MERGE-NEG-01",
        "name": "PR-MERGE-NEG-01::agent-merge-only",
        "observed": "VALIDATION_FAILURE",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "VALIDATION_FAILURE",
        "expected_rule": "PR_MERGE_AUTHORITY",
        "fixture_variant": "PR-MERGE-NEG-01",
        "name": "PR-MERGE-NEG-01::auto-merge-only",
        "observed": "VALIDATION_FAILURE",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "APPROVE_ONE_UNDRAINED_ADDENDUM_THEN_RS40",
        "expected_rule": null,
        "fixture_id": "PF10-POS-01",
        "name": "PF10-POS-01",
        "observed": "APPROVE_ONE_UNDRAINED_ADDENDUM_THEN_RS40",
        "passed": true,
        "polarity": "POSITIVE"
      },
      {
        "expected": "DRAIN_VERIFIED_RESUME_PR35_VIA_RS40",
        "expected_rule": null,
        "fixture_id": "PF10-POS-02",
        "name": "PF10-POS-02",
        "observed": "DRAIN_VERIFIED_RESUME_PR35_VIA_RS40",
        "passed": true,
        "polarity": "POSITIVE"
      },
      {
        "expected": "RESOLVE_CURRENT_MARKDOWN_INDEPENDENTLY",
        "expected_rule": "PF10_FRESH_CURRENT_RESOLUTION",
        "fixture_id": "PF10-NEG-01",
        "name": "PF10-NEG-01",
        "observed": "RESOLVE_CURRENT_MARKDOWN_INDEPENDENTLY",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "SOURCE_RESOLUTION_ERROR",
        "expected_rule": "PFCANON_SOURCE_RESOLUTION",
        "fixture_id": "PF10-NEG-02",
        "name": "PF10-NEG-02",
        "observed": "SOURCE_RESOLUTION_ERROR",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "MANUAL_DRAIN_REQUIRED",
        "expected_rule": "PF10_ANCHOR_ABSENT",
        "fixture_id": "PF10-NEG-03",
        "name": "PF10-NEG-03",
        "observed": "MANUAL_DRAIN_REQUIRED",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "MANUAL_DRAIN_MISMATCH",
        "expected_rule": "PF10_ANCHOR_MISMATCH",
        "fixture_id": "PF10-NEG-04",
        "name": "PF10-NEG-04",
        "observed": "MANUAL_DRAIN_MISMATCH",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "MANUAL_DRAIN_MISMATCH",
        "expected_rule": "PF10_ANCHOR_MISMATCH",
        "fixture_variant": "PF10-NEG-04",
        "name": "PF10-NEG-04::addendum-id-mismatch",
        "observed": "MANUAL_DRAIN_MISMATCH",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "MANUAL_DRAIN_MISMATCH",
        "expected_rule": "PF10_ANCHOR_MISMATCH",
        "fixture_variant": "PF10-NEG-04",
        "name": "PF10-NEG-04::decision-id-mismatch",
        "observed": "MANUAL_DRAIN_MISMATCH",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "MANUAL_DRAIN_MISMATCH",
        "expected_rule": "PF10_ANCHOR_MISMATCH",
        "fixture_variant": "PF10-NEG-04",
        "name": "PF10-NEG-04::immutable-base-id-mismatch",
        "observed": "MANUAL_DRAIN_MISMATCH",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "MANUAL_DRAIN_MISMATCH",
        "expected_rule": "PF10_ANCHOR_MISMATCH",
        "fixture_variant": "PF10-NEG-04",
        "name": "PF10-NEG-04::later-conflicting-overlay",
        "observed": "MANUAL_DRAIN_MISMATCH",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "NO_ADDENDUM",
        "expected_rule": "PF10_NONQUALIFYING_OUTCOME",
        "fixture_id": "PF10-NEG-05",
        "name": "PF10-NEG-05",
        "observed": "NO_ADDENDUM",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "NO_ADDENDUM",
        "expected_rule": "PF10_NONQUALIFYING_OUTCOME",
        "fixture_variant": "PF10-NEG-05",
        "name": "PF10-NEG-05::reject",
        "observed": "NO_ADDENDUM",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "NO_ADDENDUM",
        "expected_rule": "PF10_NONQUALIFYING_OUTCOME",
        "fixture_variant": "PF10-NEG-05",
        "name": "PF10-NEG-05::deny",
        "observed": "NO_ADDENDUM",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "NO_ADDENDUM",
        "expected_rule": "PF10_NONQUALIFYING_OUTCOME",
        "fixture_variant": "PF10-NEG-05",
        "name": "PF10-NEG-05::revision-required",
        "observed": "NO_ADDENDUM",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "NO_ADDENDUM",
        "expected_rule": "PF10_NONQUALIFYING_OUTCOME",
        "fixture_variant": "PF10-NEG-05",
        "name": "PF10-NEG-05::pending",
        "observed": "NO_ADDENDUM",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "NO_ADDENDUM",
        "expected_rule": "PF10_NONQUALIFYING_OUTCOME",
        "fixture_variant": "PF10-NEG-05",
        "name": "PF10-NEG-05::initial-approval",
        "observed": "NO_ADDENDUM",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "IN_SCOPE_REPAIR",
        "expected_rule": null,
        "fixture_id": "RS-DECISION-01",
        "name": "RS-DECISION-01",
        "observed": "IN_SCOPE_REPAIR",
        "passed": true,
        "polarity": "POSITIVE"
      },
      {
        "expected": "SPECIFICATION_CHANGE_REQUIRED",
        "expected_rule": null,
        "fixture_id": "RS-DECISION-02",
        "name": "RS-DECISION-02",
        "observed": "SPECIFICATION_CHANGE_REQUIRED",
        "passed": true,
        "polarity": "POSITIVE"
      },
      {
        "expected": "DRAIN_VERIFIED_RESUME_PR30_DIRECT",
        "expected_rule": null,
        "fixture_id": "RS-RETURN-01",
        "name": "RS-RETURN-01",
        "observed": "DRAIN_VERIFIED_RESUME_PR30_DIRECT",
        "passed": true,
        "polarity": "POSITIVE"
      },
      {
        "expected": "DRAIN_VERIFIED_RESUME_PR35_VIA_RS40",
        "expected_rule": null,
        "fixture_id": "RS-RETURN-02",
        "name": "RS-RETURN-02",
        "observed": "DRAIN_VERIFIED_RESUME_PR35_VIA_RS40",
        "passed": true,
        "polarity": "POSITIVE"
      },
      {
        "expected": "PR_ABORTED_ESCALATED",
        "expected_rule": null,
        "fixture_id": "ABORT-POS-01",
        "name": "ABORT-POS-01",
        "observed": "PR_ABORTED_ESCALATED",
        "passed": true,
        "polarity": "POSITIVE"
      },
      {
        "expected": "VALIDATION_FAILURE",
        "expected_rule": "PR50_PRODUCT_OWNER_ONLY",
        "fixture_id": "ABORT-NEG-01",
        "name": "ABORT-NEG-01",
        "observed": "VALIDATION_FAILURE",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "VALIDATION_FAILURE",
        "expected_rule": "PR50_PRODUCT_OWNER_ONLY",
        "fixture_variant": "ABORT-NEG-01",
        "name": "ABORT-NEG-01::prompt-origin",
        "observed": "VALIDATION_FAILURE",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "VALIDATION_FAILURE",
        "expected_rule": "PR50_PRODUCT_OWNER_ONLY",
        "fixture_variant": "ABORT-NEG-01",
        "name": "ABORT-NEG-01::skill-origin",
        "observed": "VALIDATION_FAILURE",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "VALIDATION_FAILURE",
        "expected_rule": "PR50_PRODUCT_OWNER_ONLY",
        "fixture_variant": "ABORT-NEG-01",
        "name": "ABORT-NEG-01::automatic-origin",
        "observed": "VALIDATION_FAILURE",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "PR35_HANDOFF_ACCEPTED",
        "expected_rule": null,
        "fixture_id": "HANDOFF-POS-01",
        "name": "HANDOFF-POS-01",
        "observed": "PR35_HANDOFF_ACCEPTED",
        "passed": true,
        "polarity": "POSITIVE"
      },
      {
        "expected": "PR40_CONDITIONAL_HANDOFF_ACCEPTED",
        "expected_rule": null,
        "fixture_id": "HANDOFF-POS-02",
        "name": "HANDOFF-POS-02",
        "observed": "PR40_CONDITIONAL_HANDOFF_ACCEPTED",
        "passed": true,
        "polarity": "POSITIVE"
      },
      {
        "expected": "VALIDATION_FAILURE",
        "expected_rule": "HANDOFF_COMPLETE_PASTE_READY",
        "fixture_id": "HANDOFF-NEG-01",
        "name": "HANDOFF-NEG-01",
        "observed": "VALIDATION_FAILURE",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "VALIDATION_FAILURE",
        "expected_rule": "HANDOFF_COMPLETE_PASTE_READY",
        "fixture_variant": "HANDOFF-NEG-01",
        "name": "HANDOFF-NEG-01::metadata-only",
        "observed": "VALIDATION_FAILURE",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "VALIDATION_FAILURE",
        "expected_rule": "HANDOFF_COMPLETE_PASTE_READY",
        "fixture_variant": "HANDOFF-NEG-01",
        "name": "HANDOFF-NEG-01::blank-field",
        "observed": "VALIDATION_FAILURE",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "VALIDATION_FAILURE",
        "expected_rule": "HANDOFF_COMPLETE_PASTE_READY",
        "fixture_variant": "HANDOFF-NEG-01",
        "name": "HANDOFF-NEG-01::library-id",
        "observed": "VALIDATION_FAILURE",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "VALIDATION_FAILURE",
        "expected_rule": "HANDOFF_COMPLETE_PASTE_READY",
        "fixture_variant": "HANDOFF-NEG-01",
        "name": "HANDOFF-NEG-01::above-reference",
        "observed": "VALIDATION_FAILURE",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "VALIDATION_FAILURE",
        "expected_rule": "HANDOFF_COMPLETE_PASTE_READY",
        "fixture_variant": "HANDOFF-NEG-01",
        "name": "HANDOFF-NEG-01::unlinked-filename",
        "observed": "VALIDATION_FAILURE",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "PFCANON_MARKDOWN_ACCEPTED",
        "expected_rule": null,
        "fixture_id": "SOURCE-POS-01",
        "name": "SOURCE-POS-01",
        "observed": "PFCANON_MARKDOWN_ACCEPTED",
        "passed": true,
        "polarity": "POSITIVE"
      },
      {
        "expected": "SOURCE_RESOLUTION_ERROR",
        "expected_rule": "PFCANON_MARKDOWN_ONLY",
        "fixture_id": "SOURCE-NEG-01",
        "name": "SOURCE-NEG-01",
        "observed": "SOURCE_RESOLUTION_ERROR",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "SOURCE_RESOLUTION_ERROR",
        "expected_rule": "PFCANON_MARKDOWN_ONLY",
        "fixture_variant": "SOURCE-NEG-01",
        "name": "SOURCE-NEG-01::doc",
        "observed": "SOURCE_RESOLUTION_ERROR",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "SOURCE_RESOLUTION_ERROR",
        "expected_rule": "PFCANON_MARKDOWN_ONLY",
        "fixture_variant": "SOURCE-NEG-01",
        "name": "SOURCE-NEG-01::docx",
        "observed": "SOURCE_RESOLUTION_ERROR",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION",
        "expected_rule": null,
        "fixture_id": "ALPHA-POS-01",
        "name": "ALPHA-POS-01",
        "observed": "READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION",
        "passed": true,
        "polarity": "POSITIVE"
      },
      {
        "expected": "HISTORICAL_HANDOFF_REJECTED",
        "expected_rule": "ALPHA_HISTORICAL_HANDOFF_NONOPERATIVE",
        "fixture_id": "ALPHA-NEG-01",
        "name": "ALPHA-NEG-01",
        "observed": "HISTORICAL_HANDOFF_REJECTED",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "HISTORICAL_HANDOFF_REJECTED",
        "expected_rule": "ALPHA_HISTORICAL_HANDOFF_NONOPERATIVE",
        "fixture_variant": "ALPHA-NEG-01",
        "name": "ALPHA-NEG-01::old-pr02-rs20",
        "observed": "HISTORICAL_HANDOFF_REJECTED",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "REMOTE_EVIDENCE_PENDING",
        "expected_rule": null,
        "fixture_id": "OBS-POS-01",
        "name": "OBS-POS-01",
        "observed": "REMOTE_EVIDENCE_PENDING",
        "passed": true,
        "polarity": "POSITIVE"
      },
      {
        "expected": "VALIDATION_FAILURE",
        "expected_rule": "OBSERVATION_EVIDENCE_ONLY",
        "fixture_id": "OBS-NEG-01",
        "name": "OBS-NEG-01",
        "observed": "VALIDATION_FAILURE",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "VALIDATION_FAILURE",
        "expected_rule": "OBSERVATION_EVIDENCE_ONLY",
        "fixture_variant": "OBS-NEG-01",
        "name": "OBS-NEG-01::endpoint-only",
        "observed": "VALIDATION_FAILURE",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "VALIDATION_FAILURE",
        "expected_rule": "OBSERVATION_EVIDENCE_ONLY",
        "fixture_variant": "OBS-NEG-01",
        "name": "OBS-NEG-01::unsupported-platform-only",
        "observed": "VALIDATION_FAILURE",
        "passed": true,
        "polarity": "NEGATIVE"
      },
      {
        "expected": "TECHNICAL_HISTORY_ONLY",
        "expected_rule": null,
        "fixture_id": "RCA-SEPARATION-01",
        "name": "RCA-SEPARATION-01",
        "observed": "TECHNICAL_HISTORY_ONLY",
        "passed": true,
        "polarity": "POSITIVE"
      },
      {
        "expected": "VALIDATION_FAILURE",
        "name": "independent-requests_additional_proceed",
        "observed": "VALIDATION_FAILURE",
        "passed": true
      },
      {
        "expected": "VALIDATION_FAILURE",
        "name": "independent-requests_new_session",
        "observed": "VALIDATION_FAILURE",
        "passed": true
      },
      {
        "expected": "VALIDATION_FAILURE",
        "name": "independent-micro_commits",
        "observed": "VALIDATION_FAILURE",
        "passed": true
      },
      {
        "expected": "VALIDATION_FAILURE",
        "name": "independent-push_after_every_edit",
        "observed": "VALIDATION_FAILURE",
        "passed": true
      },
      {
        "expected": "VALIDATION_FAILURE",
        "name": "independent-agent_merge",
        "observed": "VALIDATION_FAILURE",
        "passed": true
      },
      {
        "expected": "VALIDATION_FAILURE",
        "name": "independent-auto_merge",
        "observed": "VALIDATION_FAILURE",
        "passed": true
      },
      {
        "expected": "VALIDATION_FAILURE",
        "name": "independent-handoff-metadata_only",
        "observed": "VALIDATION_FAILURE",
        "passed": true
      },
      {
        "expected": "VALIDATION_FAILURE",
        "name": "independent-handoff-blank_field",
        "observed": "VALIDATION_FAILURE",
        "passed": true
      },
      {
        "expected": "VALIDATION_FAILURE",
        "name": "independent-handoff-library_id",
        "observed": "VALIDATION_FAILURE",
        "passed": true
      },
      {
        "expected": "VALIDATION_FAILURE",
        "name": "independent-handoff-uses_above",
        "observed": "VALIDATION_FAILURE",
        "passed": true
      },
      {
        "expected": "VALIDATION_FAILURE",
        "name": "independent-handoff-unlinked_filename",
        "observed": "VALIDATION_FAILURE",
        "passed": true
      },
      {
        "expected": "VALIDATION_FAILURE",
        "name": "independent-observation-asserted_session_endpoint",
        "observed": "VALIDATION_FAILURE",
        "passed": true
      },
      {
        "expected": "VALIDATION_FAILURE",
        "name": "independent-observation-unsupported_platform_diagnosis",
        "observed": "VALIDATION_FAILURE",
        "passed": true
      },
      {
        "expected": "NO_ADDENDUM",
        "name": "independent-no-addendum-reject",
        "observed": "NO_ADDENDUM",
        "passed": true
      },
      {
        "expected": "NO_ADDENDUM",
        "name": "independent-no-addendum-deny",
        "observed": "NO_ADDENDUM",
        "passed": true
      },
      {
        "expected": "NO_ADDENDUM",
        "name": "independent-no-addendum-revision_required",
        "observed": "NO_ADDENDUM",
        "passed": true
      },
      {
        "expected": "NO_ADDENDUM",
        "name": "independent-no-addendum-in_scope_repair",
        "observed": "NO_ADDENDUM",
        "passed": true
      },
      {
        "expected": "NO_ADDENDUM",
        "name": "independent-no-addendum-pending",
        "observed": "NO_ADDENDUM",
        "passed": true
      },
      {
        "expected": "NO_ADDENDUM",
        "name": "independent-no-addendum-initial_approval",
        "observed": "NO_ADDENDUM",
        "passed": true
      },
      {
        "expected": "HISTORICAL_HANDOFF_REJECTED",
        "name": "independent-alpha-history-superseded_pr03_pr04",
        "observed": "HISTORICAL_HANDOFF_REJECTED",
        "passed": true
      },
      {
        "expected": "HISTORICAL_HANDOFF_REJECTED",
        "name": "independent-alpha-history-old_pr02_rs20",
        "observed": "HISTORICAL_HANDOFF_REJECTED",
        "passed": true
      },
      {
        "errors": [
          "CONTRACT_IDENTITY"
        ],
        "expected_error": "CONTRACT_IDENTITY",
        "name": "reject-54-member-candidate",
        "passed": true
      },
      {
        "errors": [
          "MEMBER_SET"
        ],
        "expected_error": "MEMBER_SET",
        "name": "reject-pr35-removal",
        "passed": true
      },
      {
        "errors": [
          "PR35_ADDED_BOUNDARY"
        ],
        "expected_error": "PR35_ADDED_BOUNDARY",
        "name": "reject-new-proceed-boundary",
        "passed": true
      },
      {
        "errors": [
          "DIRECT_PR30_PR40_EDGE"
        ],
        "expected_error": "DIRECT_PR30_PR40_EDGE",
        "name": "reject-pr30-direct-pr40",
        "passed": true
      },
      {
        "errors": [
          "DIRECT_PR35_PR40_EDGE"
        ],
        "expected_error": "DIRECT_PR35_PR40_EDGE",
        "name": "reject-pr35-direct-pr40",
        "passed": true
      },
      {
        "errors": [
          "PR30_RESULT_VOCABULARY"
        ],
        "expected_error": "PR30_RESULT_VOCABULARY",
        "name": "reject-missing-pr30-result",
        "passed": true
      },
      {
        "errors": [
          "PR35_RESULT_VOCABULARY"
        ],
        "expected_error": "PR35_RESULT_VOCABULARY",
        "name": "reject-missing-pr35-result",
        "passed": true
      },
      {
        "errors": [
          "PR_REMOTE_ACTION_LEDGER"
        ],
        "expected_error": "PR_REMOTE_ACTION_LEDGER",
        "name": "reject-missing-ledger",
        "passed": true
      },
      {
        "errors": [
          "PR_DEVELOPMENT_CONTRACT"
        ],
        "expected_error": "PR_DEVELOPMENT_CONTRACT",
        "name": "reject-agent-merge",
        "passed": true
      },
      {
        "errors": [
          "PR50_INBOUND_EDGE"
        ],
        "expected_error": "PR50_INBOUND_EDGE",
        "name": "reject-pr50-prompt-inbound",
        "passed": true
      },
      {
        "errors": [
          "CANONICAL_SOURCE_CONTRACT"
        ],
        "expected_error": "CANONICAL_SOURCE_CONTRACT",
        "name": "reject-native-pfcanon-fallback",
        "passed": true
      },
      {
        "errors": [
          "CANONICAL_SOURCE_CONTRACT"
        ],
        "expected_error": "CANONICAL_SOURCE_CONTRACT",
        "name": "reject-native-equivalence-check",
        "passed": true
      },
      {
        "errors": [
          "PF10_REPAIR_SOURCE_PIN"
        ],
        "expected_error": "PF10_REPAIR_SOURCE_PIN",
        "name": "reject-defective-pf10-repair-digest",
        "passed": true
      },
      {
        "errors": [
          "PF10_REPAIR_SOURCE_PIN"
        ],
        "expected_error": "PF10_REPAIR_SOURCE_PIN",
        "name": "reject-appended-lf-pf10-repair-size",
        "passed": true
      },
      {
        "errors": [
          "PF10_REPAIR_SOURCE_PIN"
        ],
        "expected_error": "PF10_REPAIR_SOURCE_PIN",
        "name": "reject-repair-pin-as-current-runtime-authority",
        "passed": true
      },
      {
        "errors": [
          "REPAIR_PLAN_SOURCE_PIN"
        ],
        "expected_error": "REPAIR_PLAN_SOURCE_PIN",
        "name": "reject-defective-repair-plan-digest",
        "passed": true
      },
      {
        "errors": [
          "REPAIR_SOURCE_MANIFEST_PIN"
        ],
        "expected_error": "REPAIR_SOURCE_MANIFEST_PIN",
        "name": "reject-corrected-source-snapshot-disagreement",
        "passed": true
      },
      {
        "errors": [
          "PF10_DRAIN_VOCABULARY"
        ],
        "expected_error": "PF10_DRAIN_VOCABULARY",
        "name": "reject-drain-state-conflation",
        "passed": true
      },
      {
        "errors": [
          "PR_RETURN_PHASE_ROUTES"
        ],
        "expected_error": "PR_RETURN_PHASE_ROUTES",
        "name": "reject-prepublication-rs40",
        "passed": true
      },
      {
        "errors": [
          "PF10_PRODUCER_SET"
        ],
        "expected_error": "PF10_PRODUCER_SET",
        "name": "reject-second-pf10-producer",
        "passed": true
      },
      {
        "errors": [
          "PLAN_WRITER_SET"
        ],
        "expected_error": "PLAN_WRITER_SET",
        "name": "reject-missing-pr10-writer",
        "passed": true
      },
      {
        "errors": [
          "HANDOFF_CONTRACT"
        ],
        "expected_error": "HANDOFF_CONTRACT",
        "name": "reject-incomplete-handoff",
        "passed": true
      },
      {
        "errors": [
          "ALPHA_TRIGGER"
        ],
        "expected_error": "ALPHA_TRIGGER",
        "name": "reject-alpha-execution",
        "passed": true
      },
      {
        "errors": [
          "PROTECTED_IDENTITIES"
        ],
        "expected_error": "PROTECTED_IDENTITIES",
        "name": "reject-primary-core-change",
        "passed": true
      },
      {
        "errors": [],
        "name": "accept-exact-selected-production-lifecycle",
        "passed": true
      },
      {
        "name": "accept-register-controlled-production-prompt-header",
        "passed": true
      },
      {
        "name": "reject-production-prompt-selected-status-claim",
        "passed": true
      },
      {
        "name": "reject-production-prompt-candidate-url-label",
        "passed": true
      },
      {
        "name": "reject-production-prompt-extra-staging-status",
        "passed": true
      },
      {
        "name": "reject-production-prompt-duplicate-generic-url",
        "passed": true
      },
      {
        "name": "reject-production-prompt-wrong-extra-generic-url",
        "passed": true
      },
      {
        "name": "reject-production-prompt-missing-register-authority",
        "passed": true
      },
      {
        "name": "reject-production-prompt-duplicate-register-authority",
        "passed": true
      },
      {
        "errors": [
          "PRODUCTION_SELECTION_EVIDENCE"
        ],
        "expected_error": "PRODUCTION_SELECTION_EVIDENCE",
        "name": "reject-production-candidate-contract-id",
        "passed": true
      },
      {
        "errors": [
          "PRODUCTION_MEMBER_LIFECYCLE:PR-35"
        ],
        "expected_error": "PRODUCTION_MEMBER_LIFECYCLE:PR-35",
        "name": "reject-production-stale-member-lifecycle",
        "passed": true
      },
      {
        "errors": [
          "PRODUCTION_CANDIDATE_PAGE_BINDING:PR-35"
        ],
        "expected_error": "PRODUCTION_CANDIDATE_PAGE_BINDING:PR-35",
        "name": "reject-production-candidate-page-binding",
        "passed": true
      },
      {
        "errors": [
          "PRODUCTION_PROMPT_REFERENCE_LIFECYCLE:pr30_prompt"
        ],
        "expected_error": "PRODUCTION_PROMPT_REFERENCE_LIFECYCLE:pr30_prompt",
        "name": "reject-production-stale-pr30_prompt",
        "passed": true
      },
      {
        "errors": [
          "PRODUCTION_PROMPT_REFERENCE_LIFECYCLE:pr35_prompt"
        ],
        "expected_error": "PRODUCTION_PROMPT_REFERENCE_LIFECYCLE:pr35_prompt",
        "name": "reject-production-stale-pr35_prompt",
        "passed": true
      },
      {
        "errors": [
          "PRODUCTION_PROMPT_REFERENCE_LIFECYCLE:pr40_prompt"
        ],
        "expected_error": "PRODUCTION_PROMPT_REFERENCE_LIFECYCLE:pr40_prompt",
        "name": "reject-production-stale-pr40_prompt",
        "passed": true
      },
      {
        "errors": [
          "PRODUCTION_PROMPT_REFERENCE_LIFECYCLE:continuation_prompt"
        ],
        "expected_error": "PRODUCTION_PROMPT_REFERENCE_LIFECYCLE:continuation_prompt",
        "name": "reject-production-stale-continuation_prompt",
        "passed": true
      },
      {
        "errors": [
          "PRODUCTION_PROMPT_REFERENCE_LIFECYCLE:abort_prompt"
        ],
        "expected_error": "PRODUCTION_PROMPT_REFERENCE_LIFECYCLE:abort_prompt",
        "name": "reject-production-stale-abort_prompt",
        "passed": true
      },
      {
        "errors": [
          "PRODUCTION_PROMPT_REFERENCE_LIFECYCLE:alpha_resumption_contract.successor_trigger.prompt"
        ],
        "expected_error": "PRODUCTION_PROMPT_REFERENCE_LIFECYCLE:alpha_resumption_contract.successor_trigger.prompt",
        "name": "reject-production-stale-alpha_resumption_contract-successor_trigger-prompt",
        "passed": true
      }
    ],
    "fixture_suite_ok": true,
    "profile": "GCFPE-20260914.1-091426.1-VALIDATION",
    "profile_errors": [],
    "prompt_version": "091426.1",
    "release": "GCFPE-20260914.1",
    "schema_version": "gcfpe-fixture-report/2.0",
    "section_13_fixture_count": 33,
    "section_13_passed": 33,
    "section_13_variant_count": 28,
    "section_13_variants_passed": 28,
    "selected_member_count": null,
    "validator_revision": "3.2.3"
  },
  "strict_flowmaster": {
    "advisories": [],
    "change_contract_coverage": {
      "core_rows": 26,
      "declared_rows": 46,
      "expected_rows": 46,
      "gcfpe_20260914_candidate": {
        "candidate_member_count": 55,
        "contract_sha256": "b3204610933a1d0f966dc98e884e193e4a2ff431066d9b082436ca2e7ccaa0fc",
        "contract_status": "UNSELECTED_CANDIDATE",
        "errors": [],
        "frozen_graph_edge_count": 230,
        "frozen_graph_node_count": 55,
        "frozen_graph_sha256": "47439465a46866e4f0c98a648887a822913a3a8ad18be66b6651634fb90eb7cb",
        "ok": true,
        "pf10_producers": [
          "CF-C-30",
          "CF-E-30",
          "ESC-40",
          "IA-30",
          "QA-70",
          "RS-20"
        ],
        "plan_writers": [
          "CF-C-20",
          "CF-C-40",
          "CF-E-20",
          "CF-E-40",
          "ESC-30",
          "IA-10",
          "IA-20",
          "IA-40",
          "PR-10",
          "PR-20",
          "QA-20",
          "QA-50",
          "QA-60",
          "QA-80"
        ],
        "profile": "GCFPE-20260914.1-091426.1-VALIDATION",
        "prompt_bodies_validated": true,
        "prompt_body_count": 55,
        "prompt_body_sha256": {
          "CF-C-10": "ac7746cb6f1e0d86edfd1703e1e4be81fa13f11fa0e4ac05a3c440b3793a73f2",
          "CF-C-20": "f3ad94f78b28a8609a22ee4d89998a9d5b2bcc9efdad3d29bbcc4c2f02b82539",
          "CF-C-30": "d12dab750df7fb492f937f019ed811516ef02d799622fbdad46e150bd4703064",
          "CF-C-40": "e30af7f63785bee5b9258b2d9317cf9d3f879d48c3eb40cc7bd70d0b10630f13",
          "CF-E-10": "e40f7571a569fa6331b39c4b47a0385945c0a87f06580085de9c76cc600782d2",
          "CF-E-20": "534756d5a7ba78c3695c26014164b838a088e489509a5833761b929a9769e8ff",
          "CF-E-30": "03621506ee52fe8526911c2fb46985606fde6aa196e0b771b7ae0b8c1bac53a4",
          "CF-E-40": "16c379f6d98abcf8cd819d539822e498433575e4686aa2ee27be7fd24178e8fe",
          "CF-PO-10": "d55ff76e2350634dfbd5c630adff7e9960f8d09555584f9441a4cb7718848f8d",
          "CL-20": "4f57d2292e3e44fc242f0b3af2b6a914a66f657767b89bf775bc4b430835df2d",
          "CL-30": "d39b4bc9d04db4258c2848097cf02ae2e20f7efeedc257cb148d31934ee64019",
          "CL-40": "0ac50c1fb41d4f846ae5bdbe190d62675c8c8d2b94899f41c40490f4e906b1c7",
          "CL-C-10": "bcbfffd5d2d65bdaf679f91a8b04a1581432e9cbd4a27895711b2b171deb7919",
          "CL-E-10": "67c97542ac5ae9c6c2da58d5a2f24826e918bcee8d7d3cdc5a04292b8017174d",
          "CL-E-20": "f48b1b862d46e331474ab0605d6e2475553aaa80141f7d70580f8540e8e448ad",
          "CL-E-30": "6c95b7694f90e866f19b0deb20ac15aae1132c0f4a4b65eec5235c15d7d1a4f0",
          "CL-E-40": "c9bd26b2655e7e678033ecdf3a9537f9e049332aca8e620ef8b791b2abda841f",
          "DOC-10": "d58b0799674ef65d43220de6617023fd3864d8e094958ada6c176d1b807604ee",
          "DOC-20": "a573a6fe0ec9112d4c9a1766e0d1f4860c791e69bb8fc687f281fc00dae7f582",
          "ESC-10": "b17995c37df63c50c2ec18283691b35b763050588c1b2b500291375349f7a8cf",
          "ESC-25": "9501b12844adbb23dd0f318a294577b9a5584d1f5c85ec568cc3477cd31c0764",
          "ESC-30": "7545d97147dd4cb4c73536948c3ea04afbf4c1e44c7185ad5ce8a5b5b5d51577",
          "ESC-40": "0354325faacfa0c1f48d842422dbe1d675799397a747d34b25c23cb4c9cb5037",
          "GCFPE-MGMT-10": "d50febce248792450f33f43113a470c9d45e734626230fa3db31cb2ca500b4e8",
          "IA-10": "91dab36d0d5e885a0868dae11e54ff080558b6f7cea57aae1575930d0d4224b6",
          "IA-20": "e3d1125537428cd11aeeb9c67e330e99da535f5f53f443775d8b5e6851ea0a6f",
          "IA-30": "eea92923da5ccafa8f39c538ec0669ef451b10306d7087786274ca2b67fcf242",
          "IA-40": "1db8ab68e6486aa19767bf5f32377170ea43cbc6632e15341b0c02d7706c1ba6",
          "IA-50": "f23bea75941bb6656e7f91184e9e5f0ac9a9590dfb03873f1f8a159a3b31c02c",
          "IA-60": "7f71aac8b97a74c6f797442eedf4270401d39522c9d9f1e84590dc41a727347c",
          "MGR-10": "6f8ab2e44347735cf0428f30e2be629a72426405412b94fe9b00e372a7c792cf",
          "OPS-10": "71e8de8e6ad822ce91159de9a7c3e008beede1536f047827280e04b172cc79ce",
          "OPS-20": "a2b585d096ce1037e140cb9c506e80f60a58f5ce6f982c18cd9aecce0a86abca",
          "OPS-30": "cdc21652c7b425b58b5af17dc65b527050bd774add225cdf0ce6d5667ecff271",
          "PR-10": "deb1c6f7d8733e5d5b630a2e5aba79922665fbb20b7c4e87f230ffd4194ef4aa",
          "PR-20": "d71cd112bc4c3b561fb05382bd1ffcdd7afdd01e8a8f31c3b8d39117e0cd745c",
          "PR-30": "2294b0220835fc36981dedd2eaaf04e58834b2b61ac3b7cb21e8c80f39fe474d",
          "PR-35": "c4212335c155a3c5346dd1fd2db7b77820f3203b56edd62ed44c0b193ea24bcc",
          "PR-40": "18e2c57c28ba2ead6c9e11aaaf7149c21cab8922e9d500393d8cdde64746a594",
          "PR-50": "d3acbf0943f58e88be3bf2a8e10dfdf9bd17210d90deef4a2d39ab6ccdc2b194",
          "QA-10": "9c1f64e37d65a54ef52f87cb7550b6c1631d161a8f6f26de51e1e62ecf09d20c",
          "QA-100": "398ee5931680152bbe386e0c201170cfcd35d6ebdaeafd8d2ffdea04bc82f650",
          "QA-110": "429351e900b4ff4a8048f58f4d090900c6d6fe074971b775b83cdcb0662e1af5",
          "QA-120": "25a9590701adc5d8217f7b5bd6b22ed3c7947a6a67ec8e2443d76a0992372a55",
          "QA-20": "3b3c300ebcc6d73b3a9d03d2236fb62a4ec95a5b9303e7c0739b49df7824b308",
          "QA-50": "adf0c45e0548a90d659e04a3835c85ffd4641bbe28df0831f3f87dbe1c839628",
          "QA-60": "98f385fd78602db3ed6d85dbbbdf335bc9a9411393609cdaeabf2aee7bdbd5c5",
          "QA-70": "d8bd5353331e457ac1d17c5b7ac67e5107a00d41f62c596fa26198de61bf0aab",
          "QA-80": "c04a2618acbb675e188bf7b39debca52dbeb3d184952b3a6d9bdc0b5282e2c84",
          "QA-90": "a1d52e2fb04bb279d533dfde6345bba219ff1fa310778edb92c50ea5c04a3e7c",
          "RS-10": "855dc1733922613df0449fc092ab56d9c248ed5fc2bd21d8e91e7c1fe4e61c29",
          "RS-20": "56b465b76dc342ba4b17b5bedd9849df7ef82b1d9b8c9b4ef79927168703dad2",
          "RS-30": "5159506c242aff06f57aea78a87ef42a6ca735eabae9e5d007dfc2e633d58700",
          "RS-40": "aa21d25ab08226c2a410236fc89766a562d02f93f34aaa3e33dd22f7e83a7ebf",
          "UTIL-10": "c654986cd5b0e3a056179b4ac5c910a9ad217ddf20b4283de0840ac074d994b9"
        },
        "prompt_version": "091426.1",
        "selected_alias_during_staging": {
          "member_count": 54,
          "prompt_version": "091326.2",
          "target_release": "GCFPE-20260913.1"
        },
        "selected_member_count": null,
        "selection_status": "UNSELECTED_CANDIDATE",
        "target_release": "GCFPE-20260914.1"
      },
      "gcfpe_20260914_candidate_fixtures": {
        "case_count": 126,
        "cases": [
          {
            "errors": [],
            "name": "section-13-fixture-document",
            "passed": true
          },
          {
            "errors": [],
            "name": "clean-versioned-contract",
            "passed": true
          },
          {
            "expected": "PR30_TO_PR35_SAME_SESSION",
            "expected_rule": null,
            "fixture_id": "PR-SPLIT-POS-01",
            "name": "PR-SPLIT-POS-01",
            "observed": "PR30_TO_PR35_SAME_SESSION",
            "passed": true,
            "polarity": "POSITIVE"
          },
          {
            "expected": "RECOVER_EXISTING_NO_DUPLICATE",
            "expected_rule": null,
            "fixture_id": "PR-SPLIT-POS-02",
            "name": "PR-SPLIT-POS-02",
            "observed": "RECOVER_EXISTING_NO_DUPLICATE",
            "passed": true,
            "polarity": "POSITIVE"
          },
          {
            "expected": "VALIDATION_FAILURE",
            "expected_rule": "PR35_ADDED_BOUNDARY",
            "fixture_id": "PR-SPLIT-NEG-01",
            "name": "PR-SPLIT-NEG-01",
            "observed": "VALIDATION_FAILURE",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "VALIDATION_FAILURE",
            "expected_rule": "PR35_ADDED_BOUNDARY",
            "fixture_variant": "PR-SPLIT-NEG-01",
            "name": "PR-SPLIT-NEG-01::extra-proceed-only",
            "observed": "VALIDATION_FAILURE",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "VALIDATION_FAILURE",
            "expected_rule": "PR35_ADDED_BOUNDARY",
            "fixture_variant": "PR-SPLIT-NEG-01",
            "name": "PR-SPLIT-NEG-01::new-session-only",
            "observed": "VALIDATION_FAILURE",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "VALIDATION_FAILURE",
            "expected_rule": "PR30_COHERENT_PUBLICATION",
            "fixture_id": "PR-SPLIT-NEG-02",
            "name": "PR-SPLIT-NEG-02",
            "observed": "VALIDATION_FAILURE",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "REVIEW_FIRST_COHERENT_PUSH",
            "expected_rule": null,
            "fixture_id": "PR-COST-POS-01",
            "name": "PR-COST-POS-01",
            "observed": "REVIEW_FIRST_COHERENT_PUSH",
            "passed": true,
            "polarity": "POSITIVE"
          },
          {
            "expected": "STALE_CI_LOCAL_CORRECTION",
            "expected_rule": null,
            "fixture_id": "PR-COST-POS-02",
            "name": "PR-COST-POS-02",
            "observed": "STALE_CI_LOCAL_CORRECTION",
            "passed": true,
            "polarity": "POSITIVE"
          },
          {
            "expected": "VALIDATION_FAILURE",
            "expected_rule": "PR_ACTION_ECONOMY",
            "fixture_id": "PR-COST-NEG-01",
            "name": "PR-COST-NEG-01",
            "observed": "VALIDATION_FAILURE",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "VALIDATION_FAILURE",
            "expected_rule": "PR_ACTION_ECONOMY",
            "fixture_variant": "PR-COST-NEG-01",
            "name": "PR-COST-NEG-01::micro-commit-only",
            "observed": "VALIDATION_FAILURE",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "VALIDATION_FAILURE",
            "expected_rule": "PR_ACTION_ECONOMY",
            "fixture_variant": "PR-COST-NEG-01",
            "name": "PR-COST-NEG-01::per-edit-push-only",
            "observed": "VALIDATION_FAILURE",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "VALIDATION_FAILURE",
            "expected_rule": "PR_SKIP_CI_AUTHORITY",
            "fixture_id": "PR-COST-NEG-02",
            "name": "PR-COST-NEG-02",
            "observed": "VALIDATION_FAILURE",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "MERGE_PENDING",
            "expected_rule": null,
            "fixture_id": "PR-READY-POS-01",
            "name": "PR-READY-POS-01",
            "observed": "MERGE_PENDING",
            "passed": true,
            "polarity": "POSITIVE"
          },
          {
            "expected": "VALIDATION_FAILURE",
            "expected_rule": "PR_MERGE_AUTHORITY",
            "fixture_id": "PR-MERGE-NEG-01",
            "name": "PR-MERGE-NEG-01",
            "observed": "VALIDATION_FAILURE",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "VALIDATION_FAILURE",
            "expected_rule": "PR_MERGE_AUTHORITY",
            "fixture_variant": "PR-MERGE-NEG-01",
            "name": "PR-MERGE-NEG-01::agent-merge-only",
            "observed": "VALIDATION_FAILURE",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "VALIDATION_FAILURE",
            "expected_rule": "PR_MERGE_AUTHORITY",
            "fixture_variant": "PR-MERGE-NEG-01",
            "name": "PR-MERGE-NEG-01::auto-merge-only",
            "observed": "VALIDATION_FAILURE",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "APPROVE_ONE_UNDRAINED_ADDENDUM_THEN_RS40",
            "expected_rule": null,
            "fixture_id": "PF10-POS-01",
            "name": "PF10-POS-01",
            "observed": "APPROVE_ONE_UNDRAINED_ADDENDUM_THEN_RS40",
            "passed": true,
            "polarity": "POSITIVE"
          },
          {
            "expected": "DRAIN_VERIFIED_RESUME_PR35_VIA_RS40",
            "expected_rule": null,
            "fixture_id": "PF10-POS-02",
            "name": "PF10-POS-02",
            "observed": "DRAIN_VERIFIED_RESUME_PR35_VIA_RS40",
            "passed": true,
            "polarity": "POSITIVE"
          },
          {
            "expected": "RESOLVE_CURRENT_MARKDOWN_INDEPENDENTLY",
            "expected_rule": "PF10_FRESH_CURRENT_RESOLUTION",
            "fixture_id": "PF10-NEG-01",
            "name": "PF10-NEG-01",
            "observed": "RESOLVE_CURRENT_MARKDOWN_INDEPENDENTLY",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "SOURCE_RESOLUTION_ERROR",
            "expected_rule": "PFCANON_SOURCE_RESOLUTION",
            "fixture_id": "PF10-NEG-02",
            "name": "PF10-NEG-02",
            "observed": "SOURCE_RESOLUTION_ERROR",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "MANUAL_DRAIN_REQUIRED",
            "expected_rule": "PF10_ANCHOR_ABSENT",
            "fixture_id": "PF10-NEG-03",
            "name": "PF10-NEG-03",
            "observed": "MANUAL_DRAIN_REQUIRED",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "MANUAL_DRAIN_MISMATCH",
            "expected_rule": "PF10_ANCHOR_MISMATCH",
            "fixture_id": "PF10-NEG-04",
            "name": "PF10-NEG-04",
            "observed": "MANUAL_DRAIN_MISMATCH",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "MANUAL_DRAIN_MISMATCH",
            "expected_rule": "PF10_ANCHOR_MISMATCH",
            "fixture_variant": "PF10-NEG-04",
            "name": "PF10-NEG-04::addendum-id-mismatch",
            "observed": "MANUAL_DRAIN_MISMATCH",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "MANUAL_DRAIN_MISMATCH",
            "expected_rule": "PF10_ANCHOR_MISMATCH",
            "fixture_variant": "PF10-NEG-04",
            "name": "PF10-NEG-04::decision-id-mismatch",
            "observed": "MANUAL_DRAIN_MISMATCH",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "MANUAL_DRAIN_MISMATCH",
            "expected_rule": "PF10_ANCHOR_MISMATCH",
            "fixture_variant": "PF10-NEG-04",
            "name": "PF10-NEG-04::immutable-base-id-mismatch",
            "observed": "MANUAL_DRAIN_MISMATCH",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "MANUAL_DRAIN_MISMATCH",
            "expected_rule": "PF10_ANCHOR_MISMATCH",
            "fixture_variant": "PF10-NEG-04",
            "name": "PF10-NEG-04::later-conflicting-overlay",
            "observed": "MANUAL_DRAIN_MISMATCH",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "NO_ADDENDUM",
            "expected_rule": "PF10_NONQUALIFYING_OUTCOME",
            "fixture_id": "PF10-NEG-05",
            "name": "PF10-NEG-05",
            "observed": "NO_ADDENDUM",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "NO_ADDENDUM",
            "expected_rule": "PF10_NONQUALIFYING_OUTCOME",
            "fixture_variant": "PF10-NEG-05",
            "name": "PF10-NEG-05::reject",
            "observed": "NO_ADDENDUM",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "NO_ADDENDUM",
            "expected_rule": "PF10_NONQUALIFYING_OUTCOME",
            "fixture_variant": "PF10-NEG-05",
            "name": "PF10-NEG-05::deny",
            "observed": "NO_ADDENDUM",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "NO_ADDENDUM",
            "expected_rule": "PF10_NONQUALIFYING_OUTCOME",
            "fixture_variant": "PF10-NEG-05",
            "name": "PF10-NEG-05::revision-required",
            "observed": "NO_ADDENDUM",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "NO_ADDENDUM",
            "expected_rule": "PF10_NONQUALIFYING_OUTCOME",
            "fixture_variant": "PF10-NEG-05",
            "name": "PF10-NEG-05::pending",
            "observed": "NO_ADDENDUM",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "NO_ADDENDUM",
            "expected_rule": "PF10_NONQUALIFYING_OUTCOME",
            "fixture_variant": "PF10-NEG-05",
            "name": "PF10-NEG-05::initial-approval",
            "observed": "NO_ADDENDUM",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "IN_SCOPE_REPAIR",
            "expected_rule": null,
            "fixture_id": "RS-DECISION-01",
            "name": "RS-DECISION-01",
            "observed": "IN_SCOPE_REPAIR",
            "passed": true,
            "polarity": "POSITIVE"
          },
          {
            "expected": "SPECIFICATION_CHANGE_REQUIRED",
            "expected_rule": null,
            "fixture_id": "RS-DECISION-02",
            "name": "RS-DECISION-02",
            "observed": "SPECIFICATION_CHANGE_REQUIRED",
            "passed": true,
            "polarity": "POSITIVE"
          },
          {
            "expected": "DRAIN_VERIFIED_RESUME_PR30_DIRECT",
            "expected_rule": null,
            "fixture_id": "RS-RETURN-01",
            "name": "RS-RETURN-01",
            "observed": "DRAIN_VERIFIED_RESUME_PR30_DIRECT",
            "passed": true,
            "polarity": "POSITIVE"
          },
          {
            "expected": "DRAIN_VERIFIED_RESUME_PR35_VIA_RS40",
            "expected_rule": null,
            "fixture_id": "RS-RETURN-02",
            "name": "RS-RETURN-02",
            "observed": "DRAIN_VERIFIED_RESUME_PR35_VIA_RS40",
            "passed": true,
            "polarity": "POSITIVE"
          },
          {
            "expected": "PR_ABORTED_ESCALATED",
            "expected_rule": null,
            "fixture_id": "ABORT-POS-01",
            "name": "ABORT-POS-01",
            "observed": "PR_ABORTED_ESCALATED",
            "passed": true,
            "polarity": "POSITIVE"
          },
          {
            "expected": "VALIDATION_FAILURE",
            "expected_rule": "PR50_PRODUCT_OWNER_ONLY",
            "fixture_id": "ABORT-NEG-01",
            "name": "ABORT-NEG-01",
            "observed": "VALIDATION_FAILURE",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "VALIDATION_FAILURE",
            "expected_rule": "PR50_PRODUCT_OWNER_ONLY",
            "fixture_variant": "ABORT-NEG-01",
            "name": "ABORT-NEG-01::prompt-origin",
            "observed": "VALIDATION_FAILURE",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "VALIDATION_FAILURE",
            "expected_rule": "PR50_PRODUCT_OWNER_ONLY",
            "fixture_variant": "ABORT-NEG-01",
            "name": "ABORT-NEG-01::skill-origin",
            "observed": "VALIDATION_FAILURE",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "VALIDATION_FAILURE",
            "expected_rule": "PR50_PRODUCT_OWNER_ONLY",
            "fixture_variant": "ABORT-NEG-01",
            "name": "ABORT-NEG-01::automatic-origin",
            "observed": "VALIDATION_FAILURE",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "PR35_HANDOFF_ACCEPTED",
            "expected_rule": null,
            "fixture_id": "HANDOFF-POS-01",
            "name": "HANDOFF-POS-01",
            "observed": "PR35_HANDOFF_ACCEPTED",
            "passed": true,
            "polarity": "POSITIVE"
          },
          {
            "expected": "PR40_CONDITIONAL_HANDOFF_ACCEPTED",
            "expected_rule": null,
            "fixture_id": "HANDOFF-POS-02",
            "name": "HANDOFF-POS-02",
            "observed": "PR40_CONDITIONAL_HANDOFF_ACCEPTED",
            "passed": true,
            "polarity": "POSITIVE"
          },
          {
            "expected": "VALIDATION_FAILURE",
            "expected_rule": "HANDOFF_COMPLETE_PASTE_READY",
            "fixture_id": "HANDOFF-NEG-01",
            "name": "HANDOFF-NEG-01",
            "observed": "VALIDATION_FAILURE",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "VALIDATION_FAILURE",
            "expected_rule": "HANDOFF_COMPLETE_PASTE_READY",
            "fixture_variant": "HANDOFF-NEG-01",
            "name": "HANDOFF-NEG-01::metadata-only",
            "observed": "VALIDATION_FAILURE",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "VALIDATION_FAILURE",
            "expected_rule": "HANDOFF_COMPLETE_PASTE_READY",
            "fixture_variant": "HANDOFF-NEG-01",
            "name": "HANDOFF-NEG-01::blank-field",
            "observed": "VALIDATION_FAILURE",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "VALIDATION_FAILURE",
            "expected_rule": "HANDOFF_COMPLETE_PASTE_READY",
            "fixture_variant": "HANDOFF-NEG-01",
            "name": "HANDOFF-NEG-01::library-id",
            "observed": "VALIDATION_FAILURE",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "VALIDATION_FAILURE",
            "expected_rule": "HANDOFF_COMPLETE_PASTE_READY",
            "fixture_variant": "HANDOFF-NEG-01",
            "name": "HANDOFF-NEG-01::above-reference",
            "observed": "VALIDATION_FAILURE",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "VALIDATION_FAILURE",
            "expected_rule": "HANDOFF_COMPLETE_PASTE_READY",
            "fixture_variant": "HANDOFF-NEG-01",
            "name": "HANDOFF-NEG-01::unlinked-filename",
            "observed": "VALIDATION_FAILURE",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "PFCANON_MARKDOWN_ACCEPTED",
            "expected_rule": null,
            "fixture_id": "SOURCE-POS-01",
            "name": "SOURCE-POS-01",
            "observed": "PFCANON_MARKDOWN_ACCEPTED",
            "passed": true,
            "polarity": "POSITIVE"
          },
          {
            "expected": "SOURCE_RESOLUTION_ERROR",
            "expected_rule": "PFCANON_MARKDOWN_ONLY",
            "fixture_id": "SOURCE-NEG-01",
            "name": "SOURCE-NEG-01",
            "observed": "SOURCE_RESOLUTION_ERROR",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "SOURCE_RESOLUTION_ERROR",
            "expected_rule": "PFCANON_MARKDOWN_ONLY",
            "fixture_variant": "SOURCE-NEG-01",
            "name": "SOURCE-NEG-01::doc",
            "observed": "SOURCE_RESOLUTION_ERROR",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "SOURCE_RESOLUTION_ERROR",
            "expected_rule": "PFCANON_MARKDOWN_ONLY",
            "fixture_variant": "SOURCE-NEG-01",
            "name": "SOURCE-NEG-01::docx",
            "observed": "SOURCE_RESOLUTION_ERROR",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION",
            "expected_rule": null,
            "fixture_id": "ALPHA-POS-01",
            "name": "ALPHA-POS-01",
            "observed": "READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION",
            "passed": true,
            "polarity": "POSITIVE"
          },
          {
            "expected": "HISTORICAL_HANDOFF_REJECTED",
            "expected_rule": "ALPHA_HISTORICAL_HANDOFF_NONOPERATIVE",
            "fixture_id": "ALPHA-NEG-01",
            "name": "ALPHA-NEG-01",
            "observed": "HISTORICAL_HANDOFF_REJECTED",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "HISTORICAL_HANDOFF_REJECTED",
            "expected_rule": "ALPHA_HISTORICAL_HANDOFF_NONOPERATIVE",
            "fixture_variant": "ALPHA-NEG-01",
            "name": "ALPHA-NEG-01::old-pr02-rs20",
            "observed": "HISTORICAL_HANDOFF_REJECTED",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "REMOTE_EVIDENCE_PENDING",
            "expected_rule": null,
            "fixture_id": "OBS-POS-01",
            "name": "OBS-POS-01",
            "observed": "REMOTE_EVIDENCE_PENDING",
            "passed": true,
            "polarity": "POSITIVE"
          },
          {
            "expected": "VALIDATION_FAILURE",
            "expected_rule": "OBSERVATION_EVIDENCE_ONLY",
            "fixture_id": "OBS-NEG-01",
            "name": "OBS-NEG-01",
            "observed": "VALIDATION_FAILURE",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "VALIDATION_FAILURE",
            "expected_rule": "OBSERVATION_EVIDENCE_ONLY",
            "fixture_variant": "OBS-NEG-01",
            "name": "OBS-NEG-01::endpoint-only",
            "observed": "VALIDATION_FAILURE",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "VALIDATION_FAILURE",
            "expected_rule": "OBSERVATION_EVIDENCE_ONLY",
            "fixture_variant": "OBS-NEG-01",
            "name": "OBS-NEG-01::unsupported-platform-only",
            "observed": "VALIDATION_FAILURE",
            "passed": true,
            "polarity": "NEGATIVE"
          },
          {
            "expected": "TECHNICAL_HISTORY_ONLY",
            "expected_rule": null,
            "fixture_id": "RCA-SEPARATION-01",
            "name": "RCA-SEPARATION-01",
            "observed": "TECHNICAL_HISTORY_ONLY",
            "passed": true,
            "polarity": "POSITIVE"
          },
          {
            "expected": "VALIDATION_FAILURE",
            "name": "independent-requests_additional_proceed",
            "observed": "VALIDATION_FAILURE",
            "passed": true
          },
          {
            "expected": "VALIDATION_FAILURE",
            "name": "independent-requests_new_session",
            "observed": "VALIDATION_FAILURE",
            "passed": true
          },
          {
            "expected": "VALIDATION_FAILURE",
            "name": "independent-micro_commits",
            "observed": "VALIDATION_FAILURE",
            "passed": true
          },
          {
            "expected": "VALIDATION_FAILURE",
            "name": "independent-push_after_every_edit",
            "observed": "VALIDATION_FAILURE",
            "passed": true
          },
          {
            "expected": "VALIDATION_FAILURE",
            "name": "independent-agent_merge",
            "observed": "VALIDATION_FAILURE",
            "passed": true
          },
          {
            "expected": "VALIDATION_FAILURE",
            "name": "independent-auto_merge",
            "observed": "VALIDATION_FAILURE",
            "passed": true
          },
          {
            "expected": "VALIDATION_FAILURE",
            "name": "independent-handoff-metadata_only",
            "observed": "VALIDATION_FAILURE",
            "passed": true
          },
          {
            "expected": "VALIDATION_FAILURE",
            "name": "independent-handoff-blank_field",
            "observed": "VALIDATION_FAILURE",
            "passed": true
          },
          {
            "expected": "VALIDATION_FAILURE",
            "name": "independent-handoff-library_id",
            "observed": "VALIDATION_FAILURE",
            "passed": true
          },
          {
            "expected": "VALIDATION_FAILURE",
            "name": "independent-handoff-uses_above",
            "observed": "VALIDATION_FAILURE",
            "passed": true
          },
          {
            "expected": "VALIDATION_FAILURE",
            "name": "independent-handoff-unlinked_filename",
            "observed": "VALIDATION_FAILURE",
            "passed": true
          },
          {
            "expected": "VALIDATION_FAILURE",
            "name": "independent-observation-asserted_session_endpoint",
            "observed": "VALIDATION_FAILURE",
            "passed": true
          },
          {
            "expected": "VALIDATION_FAILURE",
            "name": "independent-observation-unsupported_platform_diagnosis",
            "observed": "VALIDATION_FAILURE",
            "passed": true
          },
          {
            "expected": "NO_ADDENDUM",
            "name": "independent-no-addendum-reject",
            "observed": "NO_ADDENDUM",
            "passed": true
          },
          {
            "expected": "NO_ADDENDUM",
            "name": "independent-no-addendum-deny",
            "observed": "NO_ADDENDUM",
            "passed": true
          },
          {
            "expected": "NO_ADDENDUM",
            "name": "independent-no-addendum-revision_required",
            "observed": "NO_ADDENDUM",
            "passed": true
          },
          {
            "expected": "NO_ADDENDUM",
            "name": "independent-no-addendum-in_scope_repair",
            "observed": "NO_ADDENDUM",
            "passed": true
          },
          {
            "expected": "NO_ADDENDUM",
            "name": "independent-no-addendum-pending",
            "observed": "NO_ADDENDUM",
            "passed": true
          },
          {
            "expected": "NO_ADDENDUM",
            "name": "independent-no-addendum-initial_approval",
            "observed": "NO_ADDENDUM",
            "passed": true
          },
          {
            "expected": "HISTORICAL_HANDOFF_REJECTED",
            "name": "independent-alpha-history-superseded_pr03_pr04",
            "observed": "HISTORICAL_HANDOFF_REJECTED",
            "passed": true
          },
          {
            "expected": "HISTORICAL_HANDOFF_REJECTED",
            "name": "independent-alpha-history-old_pr02_rs20",
            "observed": "HISTORICAL_HANDOFF_REJECTED",
            "passed": true
          },
          {
            "errors": [
              "CONTRACT_IDENTITY"
            ],
            "expected_error": "CONTRACT_IDENTITY",
            "name": "reject-54-member-candidate",
            "passed": true
          },
          {
            "errors": [
              "MEMBER_SET"
            ],
            "expected_error": "MEMBER_SET",
            "name": "reject-pr35-removal",
            "passed": true
          },
          {
            "errors": [
              "PR35_ADDED_BOUNDARY"
            ],
            "expected_error": "PR35_ADDED_BOUNDARY",
            "name": "reject-new-proceed-boundary",
            "passed": true
          },
          {
            "errors": [
              "DIRECT_PR30_PR40_EDGE"
            ],
            "expected_error": "DIRECT_PR30_PR40_EDGE",
            "name": "reject-pr30-direct-pr40",
            "passed": true
          },
          {
            "errors": [
              "DIRECT_PR35_PR40_EDGE"
            ],
            "expected_error": "DIRECT_PR35_PR40_EDGE",
            "name": "reject-pr35-direct-pr40",
            "passed": true
          },
          {
            "errors": [
              "PR30_RESULT_VOCABULARY"
            ],
            "expected_error": "PR30_RESULT_VOCABULARY",
            "name": "reject-missing-pr30-result",
            "passed": true
          },
          {
            "errors": [
              "PR35_RESULT_VOCABULARY"
            ],
            "expected_error": "PR35_RESULT_VOCABULARY",
            "name": "reject-missing-pr35-result",
            "passed": true
          },
          {
            "errors": [
              "PR_REMOTE_ACTION_LEDGER"
            ],
            "expected_error": "PR_REMOTE_ACTION_LEDGER",
            "name": "reject-missing-ledger",
            "passed": true
          },
          {
            "errors": [
              "PR_DEVELOPMENT_CONTRACT"
            ],
            "expected_error": "PR_DEVELOPMENT_CONTRACT",
            "name": "reject-agent-merge",
            "passed": true
          },
          {
            "errors": [
              "PR50_INBOUND_EDGE"
            ],
            "expected_error": "PR50_INBOUND_EDGE",
            "name": "reject-pr50-prompt-inbound",
            "passed": true
          },
          {
            "errors": [
              "CANONICAL_SOURCE_CONTRACT"
            ],
            "expected_error": "CANONICAL_SOURCE_CONTRACT",
            "name": "reject-native-pfcanon-fallback",
            "passed": true
          },
          {
            "errors": [
              "CANONICAL_SOURCE_CONTRACT"
            ],
            "expected_error": "CANONICAL_SOURCE_CONTRACT",
            "name": "reject-native-equivalence-check",
            "passed": true
          },
          {
            "errors": [
              "PF10_REPAIR_SOURCE_PIN"
            ],
            "expected_error": "PF10_REPAIR_SOURCE_PIN",
            "name": "reject-defective-pf10-repair-digest",
            "passed": true
          },
          {
            "errors": [
              "PF10_REPAIR_SOURCE_PIN"
            ],
            "expected_error": "PF10_REPAIR_SOURCE_PIN",
            "name": "reject-appended-lf-pf10-repair-size",
            "passed": true
          },
          {
            "errors": [
              "PF10_REPAIR_SOURCE_PIN"
            ],
            "expected_error": "PF10_REPAIR_SOURCE_PIN",
            "name": "reject-repair-pin-as-current-runtime-authority",
            "passed": true
          },
          {
            "errors": [
              "REPAIR_PLAN_SOURCE_PIN"
            ],
            "expected_error": "REPAIR_PLAN_SOURCE_PIN",
            "name": "reject-defective-repair-plan-digest",
            "passed": true
          },
          {
            "errors": [
              "REPAIR_SOURCE_MANIFEST_PIN"
            ],
            "expected_error": "REPAIR_SOURCE_MANIFEST_PIN",
            "name": "reject-corrected-source-snapshot-disagreement",
            "passed": true
          },
          {
            "errors": [
              "PF10_DRAIN_VOCABULARY"
            ],
            "expected_error": "PF10_DRAIN_VOCABULARY",
            "name": "reject-drain-state-conflation",
            "passed": true
          },
          {
            "errors": [
              "PR_RETURN_PHASE_ROUTES"
            ],
            "expected_error": "PR_RETURN_PHASE_ROUTES",
            "name": "reject-prepublication-rs40",
            "passed": true
          },
          {
            "errors": [
              "PF10_PRODUCER_SET"
            ],
            "expected_error": "PF10_PRODUCER_SET",
            "name": "reject-second-pf10-producer",
            "passed": true
          },
          {
            "errors": [
              "PLAN_WRITER_SET"
            ],
            "expected_error": "PLAN_WRITER_SET",
            "name": "reject-missing-pr10-writer",
            "passed": true
          },
          {
            "errors": [
              "HANDOFF_CONTRACT"
            ],
            "expected_error": "HANDOFF_CONTRACT",
            "name": "reject-incomplete-handoff",
            "passed": true
          },
          {
            "errors": [
              "ALPHA_TRIGGER"
            ],
            "expected_error": "ALPHA_TRIGGER",
            "name": "reject-alpha-execution",
            "passed": true
          },
          {
            "errors": [
              "PROTECTED_IDENTITIES"
            ],
            "expected_error": "PROTECTED_IDENTITIES",
            "name": "reject-primary-core-change",
            "passed": true
          },
          {
            "errors": [],
            "name": "accept-exact-selected-production-lifecycle",
            "passed": true
          },
          {
            "name": "accept-register-controlled-production-prompt-header",
            "passed": true
          },
          {
            "name": "reject-production-prompt-selected-status-claim",
            "passed": true
          },
          {
            "name": "reject-production-prompt-candidate-url-label",
            "passed": true
          },
          {
            "name": "reject-production-prompt-extra-staging-status",
            "passed": true
          },
          {
            "name": "reject-production-prompt-duplicate-generic-url",
            "passed": true
          },
          {
            "name": "reject-production-prompt-wrong-extra-generic-url",
            "passed": true
          },
          {
            "name": "reject-production-prompt-missing-register-authority",
            "passed": true
          },
          {
            "name": "reject-production-prompt-duplicate-register-authority",
            "passed": true
          },
          {
            "errors": [
              "PRODUCTION_SELECTION_EVIDENCE"
            ],
            "expected_error": "PRODUCTION_SELECTION_EVIDENCE",
            "name": "reject-production-candidate-contract-id",
            "passed": true
          },
          {
            "errors": [
              "PRODUCTION_MEMBER_LIFECYCLE:PR-35"
            ],
            "expected_error": "PRODUCTION_MEMBER_LIFECYCLE:PR-35",
            "name": "reject-production-stale-member-lifecycle",
            "passed": true
          },
          {
            "errors": [
              "PRODUCTION_CANDIDATE_PAGE_BINDING:PR-35"
            ],
            "expected_error": "PRODUCTION_CANDIDATE_PAGE_BINDING:PR-35",
            "name": "reject-production-candidate-page-binding",
            "passed": true
          },
          {
            "errors": [
              "PRODUCTION_PROMPT_REFERENCE_LIFECYCLE:pr30_prompt"
            ],
            "expected_error": "PRODUCTION_PROMPT_REFERENCE_LIFECYCLE:pr30_prompt",
            "name": "reject-production-stale-pr30_prompt",
            "passed": true
          },
          {
            "errors": [
              "PRODUCTION_PROMPT_REFERENCE_LIFECYCLE:pr35_prompt"
            ],
            "expected_error": "PRODUCTION_PROMPT_REFERENCE_LIFECYCLE:pr35_prompt",
            "name": "reject-production-stale-pr35_prompt",
            "passed": true
          },
          {
            "errors": [
              "PRODUCTION_PROMPT_REFERENCE_LIFECYCLE:pr40_prompt"
            ],
            "expected_error": "PRODUCTION_PROMPT_REFERENCE_LIFECYCLE:pr40_prompt",
            "name": "reject-production-stale-pr40_prompt",
            "passed": true
          },
          {
            "errors": [
              "PRODUCTION_PROMPT_REFERENCE_LIFECYCLE:continuation_prompt"
            ],
            "expected_error": "PRODUCTION_PROMPT_REFERENCE_LIFECYCLE:continuation_prompt",
            "name": "reject-production-stale-continuation_prompt",
            "passed": true
          },
          {
            "errors": [
              "PRODUCTION_PROMPT_REFERENCE_LIFECYCLE:abort_prompt"
            ],
            "expected_error": "PRODUCTION_PROMPT_REFERENCE_LIFECYCLE:abort_prompt",
            "name": "reject-production-stale-abort_prompt",
            "passed": true
          },
          {
            "errors": [
              "PRODUCTION_PROMPT_REFERENCE_LIFECYCLE:alpha_resumption_contract.successor_trigger.prompt"
            ],
            "expected_error": "PRODUCTION_PROMPT_REFERENCE_LIFECYCLE:alpha_resumption_contract.successor_trigger.prompt",
            "name": "reject-production-stale-alpha_resumption_contract-successor_trigger-prompt",
            "passed": true
          }
        ],
        "fixture_suite_ok": true,
        "profile": "GCFPE-20260914.1-091426.1-VALIDATION",
        "profile_errors": [],
        "prompt_version": "091426.1",
        "release": "GCFPE-20260914.1",
        "schema_version": "gcfpe-fixture-report/2.0",
        "section_13_fixture_count": 33,
        "section_13_passed": 33,
        "section_13_variant_count": 28,
        "section_13_variants_passed": 28,
        "selected_member_count": null,
        "validator_revision": "3.2.3"
      },
      "gcfpe_current_direct_handoff": {
        "contract_status": "SELECTED_PRODUCTION",
        "errors": [],
        "ok": true,
        "pf10_producers": [
          "CF-C-30",
          "CF-E-30",
          "ESC-40",
          "IA-30",
          "QA-70",
          "RS-20"
        ],
        "plan_writers": [
          "CF-C-20",
          "CF-C-40",
          "CF-E-20",
          "CF-E-40",
          "IA-10",
          "IA-20",
          "IA-40",
          "PR-20",
          "QA-20",
          "QA-50",
          "QA-60",
          "QA-80"
        ],
        "prompt_bodies_validated": false,
        "prompt_version": "091326.2",
        "selected_member_count": 54,
        "target_release": "GCFPE-20260913.1"
      },
      "gcfpe_current_fixtures": {
        "case_count": 82,
        "cases": [
          {
            "errors": [],
            "name": "six-required-successor-scenarios",
            "passed": true
          },
          {
            "errors": [],
            "name": "clean-successor-contract",
            "passed": true
          },
          {
            "errors": [
              "MEMBER_SET"
            ],
            "name": "reject-wrong-member-count",
            "passed": true
          },
          {
            "errors": [
              "ASSESSMENT_MIDDLEWARE_NOT_ZERO"
            ],
            "name": "reject-assessment-middleware",
            "passed": true
          },
          {
            "errors": [
              "HANDOFF_CONTRACT"
            ],
            "name": "reject-metadata-only-handoff",
            "passed": true
          },
          {
            "errors": [
              "CANONICAL_SOURCE_CONTRACT"
            ],
            "name": "reject-google-docs-pfcanon-fallback",
            "passed": true
          },
          {
            "errors": [
              "IMMUTABLE_BASE_CONTRACT"
            ],
            "name": "reject-live-base-rewrite",
            "passed": true
          },
          {
            "errors": [
              "IMMUTABLE_BASE_CONTRACT"
            ],
            "name": "reject-undrained-delta-reliance",
            "passed": true
          },
          {
            "errors": [
              "RESCOPE_CONTRACT"
            ],
            "name": "reject-rescope-restart",
            "passed": true
          },
          {
            "errors": [
              "RESCOPE_CONTRACT"
            ],
            "name": "reject-second-proceed",
            "passed": true
          },
          {
            "errors": [
              "RESCOPE_CONTRACT"
            ],
            "name": "reject-mandatory-rs10-in-pr-rescope",
            "passed": true
          },
          {
            "errors": [
              "RESCOPE_CONTRACT"
            ],
            "name": "reject-rs10-blanket-open-pr-restriction",
            "passed": true
          },
          {
            "errors": [
              "ROUTE_GRAPH_EXACT:normal_request"
            ],
            "name": "reject-normal-request-via-rs10",
            "passed": true
          },
          {
            "errors": [
              "ROUTE_GRAPH_EXACT:bounded_rescope_rejected"
            ],
            "name": "reject-obsolete-rs10-rescope-route",
            "passed": true
          },
          {
            "errors": [
              "ROUTE_GRAPH_EXACT:bounded_rescope_approved"
            ],
            "name": "reject-approved-rescope-without-manual-drain",
            "passed": true
          },
          {
            "errors": [
              "ROUTE_GRAPH_EXACT:approved_crd_specification_delta"
            ],
            "name": "reject-approved-crd-specification-delta-without-manual-drain",
            "passed": true
          },
          {
            "errors": [
              "ROUTE_GRAPH_EXACT:approved_epic_specification_delta"
            ],
            "name": "reject-approved-epic-specification-delta-without-manual-drain",
            "passed": true
          },
          {
            "errors": [
              "ROUTE_GRAPH_EXACT:approved_implementation_plan_delta"
            ],
            "name": "reject-approved-implementation-plan-delta-without-manual-drain",
            "passed": true
          },
          {
            "errors": [
              "ROUTE_GRAPH_EXACT:approved_qa_plan_delta"
            ],
            "name": "reject-approved-qa-plan-delta-without-manual-drain",
            "passed": true
          },
          {
            "errors": [
              "ROUTE_GRAPH_EXACT:approved_escalation_or_remediation"
            ],
            "name": "reject-approved-escalation-or-remediation-without-manual-drain",
            "passed": true
          },
          {
            "errors": [
              "ABORT_REACHABILITY"
            ],
            "name": "reject-agent-routable-abort",
            "passed": true
          },
          {
            "errors": [
              "CONTINUATION_PAGE_COHERENCE"
            ],
            "name": "reject-continuation-page-url-mismatch",
            "passed": true
          },
          {
            "errors": [
              "ABORT_PAGE_COHERENCE"
            ],
            "name": "reject-abort-page-url-mismatch",
            "passed": true
          },
          {
            "errors": [
              "PF10_PRODUCER_SET"
            ],
            "name": "reject-missing-semantic-producer",
            "passed": true
          },
          {
            "errors": [
              "PF10_PRODUCER_SET"
            ],
            "name": "reject-wrong-producer-outcome-semantics",
            "passed": true
          },
          {
            "errors": [
              "PF10_ADDENDUM_CONTRACT"
            ],
            "name": "reject-premature-addendum-canonicality",
            "passed": true
          },
          {
            "errors": [
              "PF10_ADDENDUM_CONTRACT"
            ],
            "name": "reject-addendum-reliance-before-drain",
            "passed": true
          },
          {
            "errors": [
              "PLAN_WRITER_SET"
            ],
            "name": "reject-missing-plan-writer",
            "passed": true
          },
          {
            "errors": [
              "PR_DEVELOPMENT_CONTRACT"
            ],
            "name": "reject-ci-before-review",
            "passed": true
          },
          {
            "errors": [
              "PROTECTED_IDENTITIES"
            ],
            "name": "reject-primary-core-change",
            "passed": true
          },
          {
            "errors": [
              "PROHIBITED_ACTIVE_ROUTING"
            ],
            "name": "reject-missing-prohibited-routing-contract",
            "passed": true
          },
          {
            "errors": [
              "CONTROL_MANIFEST",
              "CONTROL_MANIFEST_DRIVE:direct_handoff_procedure_v2_0_0",
              "CONTROL_MANIFEST_DRIVE:successor_operating_procedure",
              "CONTROL_MANIFEST_PREDECESSOR_CATALOG",
              "CONTROL_MANIFEST_PREDECESSOR_MANAGEMENT",
              "CONTROL_MANIFEST_PREDECESSOR_PE",
              "CONTROL_MANIFEST_SUCCESSOR_CATALOG",
              "CONTROL_MANIFEST_SUCCESSOR_PE",
              "CONTROL_MANIFEST_SUCCESSOR_PROCEDURE",
              "CONTROL_MANIFEST_SUCCESSOR_VALIDATION"
            ],
            "name": "reject-empty-control-manifest",
            "passed": true
          },
          {
            "errors": [
              "CONTROL_MANIFEST_NOTION:successor_catalog"
            ],
            "name": "reject-successor-catalog-control-mismatch",
            "passed": true
          },
          {
            "errors": [
              "CONTROL_MANIFEST_DRIVE:successor_operating_procedure"
            ],
            "name": "reject-successor-procedure-control-mismatch",
            "passed": true
          },
          {
            "errors": [
              "CONTROL_MANIFEST_SUCCESSOR_VALIDATION"
            ],
            "name": "reject-successor-validation-report-control-mismatch",
            "passed": true
          },
          {
            "errors": [
              "CONTINUATION_PAGE_COHERENCE",
              "NOTION_PAGE_MANIFEST"
            ],
            "name": "reject-unresolved-continuation-page",
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 0,
              "destination": "RS-20",
              "disposition": "PROPOSAL",
              "handoff_count": 1
            },
            "name": "PR-10-proposal-intake",
            "observed": {
              "addendum_count": 0,
              "destination": "RS-20",
              "disposition": "PROPOSAL",
              "handoff_count": 1
            },
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 1,
              "authority_expanded": false,
              "base_rewrite": false,
              "destination_after_drain": "PR-10",
              "disposition": "APPROVED_AWAIT_MANUAL_DRAIN",
              "new_proceed": false
            },
            "name": "PR-10-bounded-delta-native-return",
            "observed": {
              "addendum_count": 1,
              "authority_expanded": false,
              "base_rewrite": false,
              "destination_after_drain": "PR-10",
              "disposition": "APPROVED_AWAIT_MANUAL_DRAIN",
              "new_proceed": false
            },
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 0,
              "destination": "RS-20",
              "disposition": "PROPOSAL",
              "handoff_count": 1
            },
            "name": "PR-20-proposal-intake",
            "observed": {
              "addendum_count": 0,
              "destination": "RS-20",
              "disposition": "PROPOSAL",
              "handoff_count": 1
            },
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 1,
              "authority_expanded": false,
              "base_rewrite": false,
              "destination_after_drain": "PR-20",
              "disposition": "APPROVED_AWAIT_MANUAL_DRAIN",
              "new_proceed": false
            },
            "name": "PR-20-bounded-delta-native-return",
            "observed": {
              "addendum_count": 1,
              "authority_expanded": false,
              "base_rewrite": false,
              "destination_after_drain": "PR-20",
              "disposition": "APPROVED_AWAIT_MANUAL_DRAIN",
              "new_proceed": false
            },
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 0,
              "destination": "RS-20",
              "disposition": "PROPOSAL",
              "handoff_count": 1
            },
            "name": "DOC-10-proposal-intake",
            "observed": {
              "addendum_count": 0,
              "destination": "RS-20",
              "disposition": "PROPOSAL",
              "handoff_count": 1
            },
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 1,
              "authority_expanded": false,
              "base_rewrite": false,
              "destination_after_drain": "DOC-10",
              "disposition": "APPROVED_AWAIT_MANUAL_DRAIN",
              "new_proceed": false
            },
            "name": "DOC-10-bounded-delta-native-return",
            "observed": {
              "addendum_count": 1,
              "authority_expanded": false,
              "base_rewrite": false,
              "destination_after_drain": "DOC-10",
              "disposition": "APPROVED_AWAIT_MANUAL_DRAIN",
              "new_proceed": false
            },
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 0,
              "destination": "RS-20",
              "disposition": "PROPOSAL",
              "handoff_count": 1
            },
            "name": "DOC-20-proposal-intake",
            "observed": {
              "addendum_count": 0,
              "destination": "RS-20",
              "disposition": "PROPOSAL",
              "handoff_count": 1
            },
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 1,
              "authority_expanded": false,
              "base_rewrite": false,
              "destination_after_drain": "DOC-20",
              "disposition": "APPROVED_AWAIT_MANUAL_DRAIN",
              "new_proceed": false
            },
            "name": "DOC-20-bounded-delta-native-return",
            "observed": {
              "addendum_count": 1,
              "authority_expanded": false,
              "base_rewrite": false,
              "destination_after_drain": "DOC-20",
              "disposition": "APPROVED_AWAIT_MANUAL_DRAIN",
              "new_proceed": false
            },
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 0,
              "destination": "RS-20",
              "disposition": "PROPOSAL",
              "handoff_count": 1
            },
            "name": "OPS-10-proposal-intake",
            "observed": {
              "addendum_count": 0,
              "destination": "RS-20",
              "disposition": "PROPOSAL",
              "handoff_count": 1
            },
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 1,
              "authority_expanded": false,
              "base_rewrite": false,
              "destination_after_drain": "OPS-10",
              "disposition": "APPROVED_AWAIT_MANUAL_DRAIN",
              "new_proceed": false
            },
            "name": "OPS-10-bounded-delta-native-return",
            "observed": {
              "addendum_count": 1,
              "authority_expanded": false,
              "base_rewrite": false,
              "destination_after_drain": "OPS-10",
              "disposition": "APPROVED_AWAIT_MANUAL_DRAIN",
              "new_proceed": false
            },
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 0,
              "destination": "RS-20",
              "disposition": "PROPOSAL",
              "handoff_count": 1
            },
            "name": "OPS-20-proposal-intake",
            "observed": {
              "addendum_count": 0,
              "destination": "RS-20",
              "disposition": "PROPOSAL",
              "handoff_count": 1
            },
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 1,
              "authority_expanded": false,
              "base_rewrite": false,
              "destination_after_drain": "OPS-20",
              "disposition": "APPROVED_AWAIT_MANUAL_DRAIN",
              "new_proceed": false
            },
            "name": "OPS-20-bounded-delta-native-return",
            "observed": {
              "addendum_count": 1,
              "authority_expanded": false,
              "base_rewrite": false,
              "destination_after_drain": "OPS-20",
              "disposition": "APPROVED_AWAIT_MANUAL_DRAIN",
              "new_proceed": false
            },
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 0,
              "destination": "RS-20",
              "disposition": "PROPOSAL",
              "handoff_count": 1
            },
            "name": "OPS-30-proposal-intake",
            "observed": {
              "addendum_count": 0,
              "destination": "RS-20",
              "disposition": "PROPOSAL",
              "handoff_count": 1
            },
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 1,
              "authority_expanded": false,
              "base_rewrite": false,
              "destination_after_drain": "OPS-30",
              "disposition": "APPROVED_AWAIT_MANUAL_DRAIN",
              "new_proceed": false
            },
            "name": "OPS-30-bounded-delta-native-return",
            "observed": {
              "addendum_count": 1,
              "authority_expanded": false,
              "base_rewrite": false,
              "destination_after_drain": "OPS-30",
              "disposition": "APPROVED_AWAIT_MANUAL_DRAIN",
              "new_proceed": false
            },
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 0,
              "destination": "RS-20",
              "disposition": "PROPOSAL",
              "handoff_count": 1
            },
            "name": "PR-40-proposal-intake",
            "observed": {
              "addendum_count": 0,
              "destination": "RS-20",
              "disposition": "PROPOSAL",
              "handoff_count": 1
            },
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 1,
              "authority_expanded": false,
              "base_rewrite": false,
              "destination_after_drain": "PR-40",
              "disposition": "APPROVED_AWAIT_MANUAL_DRAIN",
              "new_proceed": false
            },
            "name": "PR-40-bounded-delta-native-return",
            "observed": {
              "addendum_count": 1,
              "authority_expanded": false,
              "base_rewrite": false,
              "destination_after_drain": "PR-40",
              "disposition": "APPROVED_AWAIT_MANUAL_DRAIN",
              "new_proceed": false
            },
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 1,
              "authority_expanded": false,
              "base_rewrite": false,
              "destination_after_drain": "RS-40",
              "disposition": "APPROVED_AWAIT_MANUAL_DRAIN",
              "new_proceed": false
            },
            "name": "open-pr-direct-request",
            "observed": {
              "addendum_count": 1,
              "authority_expanded": false,
              "base_rewrite": false,
              "destination_after_drain": "RS-40",
              "disposition": "APPROVED_AWAIT_MANUAL_DRAIN",
              "new_proceed": false
            },
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 0,
              "base_rewrite": false,
              "disposition": "CONTINUE_SAME_PR",
              "execution_state": "SAME_PR_IMPLEMENTATION",
              "new_proceed": false,
              "new_prompt_invocation": false
            },
            "name": "drained-open-pr-rescope",
            "observed": {
              "addendum_count": 0,
              "base_rewrite": false,
              "disposition": "CONTINUE_SAME_PR",
              "execution_state": "SAME_PR_IMPLEMENTATION",
              "new_proceed": false,
              "new_prompt_invocation": false
            },
            "passed": true
          },
          {
            "expected": {
              "abort": false,
              "closure": false,
              "disposition": "TERMINAL_TO_OPERATOR",
              "handoff_count": 0,
              "reason": "MISSING_DRAIN_OR_ORIGINAL_AUTHORITY"
            },
            "name": "no-drain-terminal",
            "observed": {
              "abort": false,
              "closure": false,
              "disposition": "TERMINAL_TO_OPERATOR",
              "handoff_count": 0,
              "reason": "MISSING_DRAIN_OR_ORIGINAL_AUTHORITY"
            },
            "passed": true
          },
          {
            "expected": {
              "abort": false,
              "closure": false,
              "disposition": "TERMINAL_TO_OPERATOR",
              "handoff_count": 0,
              "reason": "MISSING_REQUIRED_EVIDENCE_OR_UNRECOVERABLE"
            },
            "name": "missing-source-terminal",
            "observed": {
              "abort": false,
              "closure": false,
              "disposition": "TERMINAL_TO_OPERATOR",
              "handoff_count": 0,
              "reason": "MISSING_REQUIRED_EVIDENCE_OR_UNRECOVERABLE"
            },
            "passed": true
          },
          {
            "expected": {
              "abort": false,
              "closure": false,
              "disposition": "TERMINAL_TO_OPERATOR",
              "handoff_count": 0,
              "reason": "MISSING_REQUIRED_EVIDENCE_OR_UNRECOVERABLE"
            },
            "name": "missing-owner-terminal",
            "observed": {
              "abort": false,
              "closure": false,
              "disposition": "TERMINAL_TO_OPERATOR",
              "handoff_count": 0,
              "reason": "MISSING_REQUIRED_EVIDENCE_OR_UNRECOVERABLE"
            },
            "passed": true
          },
          {
            "expected": {
              "abort": false,
              "closure": false,
              "disposition": "TERMINAL_TO_OPERATOR",
              "handoff_count": 0,
              "reason": "MISSING_REQUIRED_EVIDENCE_OR_UNRECOVERABLE"
            },
            "name": "unrecoverable-terminal",
            "observed": {
              "abort": false,
              "closure": false,
              "disposition": "TERMINAL_TO_OPERATOR",
              "handoff_count": 0,
              "reason": "MISSING_REQUIRED_EVIDENCE_OR_UNRECOVERABLE"
            },
            "passed": true
          },
          {
            "expected": {
              "abort": false,
              "closure": false,
              "disposition": "TERMINAL_TO_OPERATOR",
              "handoff_count": 0,
              "reason": "INCOMPATIBLE_APPROVAL_OR_PR_STATE"
            },
            "name": "merged-pr-not-rs40",
            "observed": {
              "abort": false,
              "closure": false,
              "disposition": "TERMINAL_TO_OPERATOR",
              "handoff_count": 0,
              "reason": "INCOMPATIBLE_APPROVAL_OR_PR_STATE"
            },
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 0,
              "base_rewrite": false,
              "destination": "PR-30",
              "disposition": "CONTINUE_NATIVE_DELIVERY",
              "new_proceed": false,
              "originating_verification_return": true
            },
            "name": "current-remediation-native-pr30",
            "observed": {
              "addendum_count": 0,
              "base_rewrite": false,
              "destination": "PR-30",
              "disposition": "CONTINUE_NATIVE_DELIVERY",
              "new_proceed": false,
              "originating_verification_return": true
            },
            "passed": true
          },
          {
            "expected": {
              "abort": false,
              "closure": false,
              "disposition": "TERMINAL_TO_OPERATOR",
              "handoff_count": 0,
              "reason": "INCOMPATIBLE_APPROVAL_OR_PR_STATE"
            },
            "name": "remediation-not-rs20-approval",
            "observed": {
              "abort": false,
              "closure": false,
              "disposition": "TERMINAL_TO_OPERATOR",
              "handoff_count": 0,
              "reason": "INCOMPATIBLE_APPROVAL_OR_PR_STATE"
            },
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 0,
              "base_rewrite": false,
              "destination": "PR-30",
              "disposition": "CONTINUE_NATIVE_DELIVERY",
              "new_proceed": false,
              "originating_verification_return": true
            },
            "name": "verified-legacy-remediation",
            "observed": {
              "addendum_count": 0,
              "base_rewrite": false,
              "destination": "PR-30",
              "disposition": "CONTINUE_NATIVE_DELIVERY",
              "new_proceed": false,
              "originating_verification_return": true
            },
            "passed": true
          },
          {
            "expected": {
              "abort": false,
              "closure": false,
              "disposition": "TERMINAL_TO_OPERATOR",
              "handoff_count": 0,
              "reason": "INCOMPATIBLE_APPROVAL_OR_PR_STATE"
            },
            "name": "unverified-legacy-remediation",
            "observed": {
              "abort": false,
              "closure": false,
              "disposition": "TERMINAL_TO_OPERATOR",
              "handoff_count": 0,
              "reason": "INCOMPATIBLE_APPROVAL_OR_PR_STATE"
            },
            "passed": true
          },
          {
            "expected": {
              "abort": false,
              "closure": false,
              "disposition": "TERMINAL_TO_OPERATOR",
              "handoff_count": 0,
              "reason": "ACCEPTED_FINAL_PRESERVED"
            },
            "name": "accepted-final-never-replayed",
            "observed": {
              "abort": false,
              "closure": false,
              "disposition": "TERMINAL_TO_OPERATOR",
              "handoff_count": 0,
              "reason": "ACCEPTED_FINAL_PRESERVED"
            },
            "passed": true
          },
          {
            "expected": {
              "abort": false,
              "closure": false,
              "disposition": "TERMINAL_TO_OPERATOR",
              "handoff_count": 0,
              "reason": "INCOMPATIBLE_REQUEST_ARTIFACT"
            },
            "name": "wrong-artifact-receiver",
            "observed": {
              "abort": false,
              "closure": false,
              "disposition": "TERMINAL_TO_OPERATOR",
              "handoff_count": 0,
              "reason": "INCOMPATIBLE_REQUEST_ARTIFACT"
            },
            "passed": true
          },
          {
            "expected": {
              "abort": false,
              "closure": false,
              "disposition": "TERMINAL_TO_OPERATOR",
              "handoff_count": 0,
              "reason": "NATIVE_DECISION_AUTHORITY_REQUIRED"
            },
            "name": "native-approval-owner-preserved",
            "observed": {
              "abort": false,
              "closure": false,
              "disposition": "TERMINAL_TO_OPERATOR",
              "handoff_count": 0,
              "reason": "NATIVE_DECISION_AUTHORITY_REQUIRED"
            },
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 1,
              "authority_expanded": false,
              "base_rewrite": false,
              "destination_after_drain": "PR-30",
              "disposition": "APPROVED_AWAIT_MANUAL_DRAIN",
              "new_proceed": false
            },
            "name": "proceeded-prepublication-rescope-native-return",
            "observed": {
              "addendum_count": 1,
              "authority_expanded": false,
              "base_rewrite": false,
              "destination_after_drain": "PR-30",
              "disposition": "APPROVED_AWAIT_MANUAL_DRAIN",
              "new_proceed": false
            },
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 0,
              "base_rewrite": false,
              "destination": "PR-30",
              "disposition": "CONTINUE_NATIVE_DELIVERY",
              "new_proceed": false,
              "originating_verification_return": true
            },
            "name": "proceeded-prepublication-native-pr30-receiver",
            "observed": {
              "addendum_count": 0,
              "base_rewrite": false,
              "destination": "PR-30",
              "disposition": "CONTINUE_NATIVE_DELIVERY",
              "new_proceed": false,
              "originating_verification_return": true
            },
            "passed": true
          },
          {
            "expected": {
              "abort": false,
              "closure": false,
              "disposition": "TERMINAL_TO_OPERATOR",
              "handoff_count": 0,
              "reason": "NATIVE_OWNER_UNRESOLVED"
            },
            "name": "no-pr-cannot-use-rs40-as-native-stage",
            "observed": {
              "abort": false,
              "closure": false,
              "disposition": "TERMINAL_TO_OPERATOR",
              "handoff_count": 0,
              "reason": "NATIVE_OWNER_UNRESOLVED"
            },
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 0,
              "destination": "RS-20",
              "disposition": "REVISED_SAME_ARTIFACT",
              "handoff_count": 1,
              "output_artifact": "RESCOPE_REQUEST"
            },
            "name": "rescope_request-revision-same-ia",
            "observed": {
              "addendum_count": 0,
              "destination": "RS-20",
              "disposition": "REVISED_SAME_ARTIFACT",
              "handoff_count": 1,
              "output_artifact": "RESCOPE_REQUEST"
            },
            "passed": true
          },
          {
            "expected": {
              "abort": false,
              "addendum_count": 0,
              "closure": false,
              "disposition": "TERMINAL_TO_OPERATOR",
              "handoff_count": 0,
              "output_artifact": "RESCOPE_REQUEST",
              "reason": "PRODUCT_OWNER_DECISION_PENDING"
            },
            "name": "rescope_request-po-correction-terminal",
            "observed": {
              "abort": false,
              "addendum_count": 0,
              "closure": false,
              "disposition": "TERMINAL_TO_OPERATOR",
              "handoff_count": 0,
              "output_artifact": "RESCOPE_REQUEST",
              "reason": "PRODUCT_OWNER_DECISION_PENDING"
            },
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 0,
              "destination": "RS-20",
              "disposition": "REVISED_SAME_ARTIFACT",
              "handoff_count": 1,
              "output_artifact": "RESCOPE_PROPOSAL"
            },
            "name": "rescope_proposal-revision-same-ia",
            "observed": {
              "addendum_count": 0,
              "destination": "RS-20",
              "disposition": "REVISED_SAME_ARTIFACT",
              "handoff_count": 1,
              "output_artifact": "RESCOPE_PROPOSAL"
            },
            "passed": true
          },
          {
            "expected": {
              "abort": false,
              "addendum_count": 0,
              "closure": false,
              "disposition": "TERMINAL_TO_OPERATOR",
              "handoff_count": 0,
              "output_artifact": "RESCOPE_PROPOSAL",
              "reason": "PRODUCT_OWNER_DECISION_PENDING"
            },
            "name": "rescope_proposal-po-correction-terminal",
            "observed": {
              "abort": false,
              "addendum_count": 0,
              "closure": false,
              "disposition": "TERMINAL_TO_OPERATOR",
              "handoff_count": 0,
              "output_artifact": "RESCOPE_PROPOSAL",
              "reason": "PRODUCT_OWNER_DECISION_PENDING"
            },
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 1,
              "base_review_replaced": false,
              "base_rewrite": false,
              "ia40_route": false,
              "output_artifact": "MATERIAL_PLAN_DELTA_REVIEW"
            },
            "name": "material-plan-delta-approve",
            "observed": {
              "addendum_count": 1,
              "base_review_replaced": false,
              "base_rewrite": false,
              "ia40_route": false,
              "output_artifact": "MATERIAL_PLAN_DELTA_REVIEW"
            },
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 0,
              "base_review_replaced": false,
              "base_rewrite": false,
              "ia40_route": false,
              "output_artifact": "MATERIAL_PLAN_DELTA_REVIEW"
            },
            "name": "material-plan-delta-deny",
            "observed": {
              "addendum_count": 0,
              "base_review_replaced": false,
              "base_rewrite": false,
              "ia40_route": false,
              "output_artifact": "MATERIAL_PLAN_DELTA_REVIEW"
            },
            "passed": true
          },
          {
            "expected": {
              "addendum_count": 0,
              "output_artifact": "IMPLEMENTATION_PLAN_REVIEW"
            },
            "name": "initial-plan-review-distinct",
            "observed": {
              "addendum_count": 0,
              "output_artifact": "IMPLEMENTATION_PLAN_REVIEW"
            },
            "passed": true
          },
          {
            "errors": [
              "RECEIVER_CONTRACT:RS-10"
            ],
            "name": "reject-missing-RS-10-receiver-contract",
            "passed": true
          },
          {
            "errors": [
              "RECEIVER_CONTRACT:RS-20"
            ],
            "name": "reject-missing-RS-20-receiver-contract",
            "passed": true
          },
          {
            "errors": [
              "RECEIVER_CONTRACT:RS-30"
            ],
            "name": "reject-missing-RS-30-receiver-contract",
            "passed": true
          },
          {
            "errors": [
              "RECEIVER_CONTRACT:RS-40"
            ],
            "name": "reject-missing-RS-40-receiver-contract",
            "passed": true
          },
          {
            "errors": [
              "RECEIVER_CONTRACT:PR-30"
            ],
            "name": "reject-missing-PR-30-receiver-contract",
            "passed": true
          },
          {
            "errors": [
              "NATIVE_REMEDIATION_CONTRACT"
            ],
            "name": "reject-remediation-rs40-incompatible-approval",
            "passed": true
          }
        ],
        "fixture_suite_ok": true,
        "prompt_version": "091326.2",
        "receiver_case_count": 40,
        "release": "GCFPE-20260913.1",
        "required_scenario_count": 6
      },
      "interfaces_closed": true,
      "material_rows": 20,
      "rows_exact": true
    },
    "finding_counts": {
      "ADVISORY": 0,
      "BLOCKER": 0,
      "ERROR": 0,
      "WARNING": 0
    },
    "findings": [],
    "fixtures": {
      "expectation_failures": [],
      "failed_expectations": 0,
      "fixture_source": "/root/.codex/skills/remote-skills/skill-6a8f973972a88191ae25426f5a818169/fixtures/change-flow/scenarios.json",
      "fixture_suite_ok": true,
      "negative_count": 19,
      "oracle_profile": "GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260831_1",
      "passed_expectations": 31,
      "positive_count": 12,
      "results": [
        {
          "actual_pass": true,
          "actual_rule_ids": [],
          "expectation_met": true,
          "expected_pass": true,
          "expected_rule_ids": [],
          "finding_count": 0,
          "id": "positive_epic_happy_path",
          "kind": "POSITIVE"
        },
        {
          "actual_pass": true,
          "actual_rule_ids": [],
          "expectation_met": true,
          "expected_pass": true,
          "expected_rule_ids": [],
          "finding_count": 0,
          "id": "positive_crd_happy_path",
          "kind": "POSITIVE"
        },
        {
          "actual_pass": true,
          "actual_rule_ids": [],
          "expectation_met": true,
          "expected_pass": true,
          "expected_rule_ids": [],
          "finding_count": 0,
          "id": "positive_specification_denial_same_thoth",
          "kind": "POSITIVE"
        },
        {
          "actual_pass": true,
          "actual_rule_ids": [],
          "expectation_met": true,
          "expected_pass": true,
          "expected_rule_ids": [],
          "finding_count": 0,
          "id": "positive_mandatory_whole_change_ia_order",
          "kind": "POSITIVE"
        },
        {
          "actual_pass": true,
          "actual_rule_ids": [],
          "expectation_met": true,
          "expected_pass": true,
          "expected_rule_ids": [],
          "finding_count": 0,
          "id": "positive_isis_review_boundary",
          "kind": "POSITIVE"
        },
        {
          "actual_pass": true,
          "actual_rule_ids": [],
          "expectation_met": true,
          "expected_pass": true,
          "expected_rule_ids": [],
          "finding_count": 0,
          "id": "positive_pr_proceed_runtime_approval",
          "kind": "POSITIVE"
        },
        {
          "actual_pass": true,
          "actual_rule_ids": [],
          "expectation_met": true,
          "expected_pass": true,
          "expected_rule_ids": [],
          "finding_count": 0,
          "id": "positive_implementation_rescope",
          "kind": "POSITIVE"
        },
        {
          "actual_pass": true,
          "actual_rule_ids": [],
          "expectation_met": true,
          "expected_pass": true,
          "expected_rule_ids": [],
          "finding_count": 0,
          "id": "positive_escalation_discovery_reentry",
          "kind": "POSITIVE"
        },
        {
          "actual_pass": true,
          "actual_rule_ids": [],
          "expectation_met": true,
          "expected_pass": true,
          "expected_rule_ids": [],
          "finding_count": 0,
          "id": "positive_qa_readiness_pf23_closure",
          "kind": "POSITIVE"
        },
        {
          "actual_pass": true,
          "actual_rule_ids": [],
          "expectation_met": true,
          "expected_pass": true,
          "expected_rule_ids": [],
          "finding_count": 0,
          "id": "positive_post_closure_adr_drainage",
          "kind": "POSITIVE"
        },
        {
          "actual_pass": true,
          "actual_rule_ids": [],
          "expectation_met": true,
          "expected_pass": true,
          "expected_rule_ids": [],
          "finding_count": 0,
          "id": "positive_post_closure_pf09_drainage",
          "kind": "POSITIVE"
        },
        {
          "actual_pass": true,
          "actual_rule_ids": [],
          "expectation_met": true,
          "expected_pass": true,
          "expected_rule_ids": [],
          "finding_count": 0,
          "id": "positive_ops_execution_boundary",
          "kind": "POSITIVE"
        },
        {
          "actual_pass": false,
          "actual_rule_ids": [
            "FMV-GCF-OBSOLETE-001"
          ],
          "expectation_met": true,
          "expected_pass": false,
          "expected_rule_ids": [
            "FMV-GCF-OBSOLETE-001"
          ],
          "finding_count": 1,
          "id": "negative_obsolete_plan_ia_manual_hold",
          "kind": "NEGATIVE"
        },
        {
          "actual_pass": false,
          "actual_rule_ids": [
            "FMV-GCF-ORDER-001"
          ],
          "expectation_met": true,
          "expected_pass": false,
          "expected_rule_ids": [
            "FMV-GCF-ORDER-001"
          ],
          "finding_count": 1,
          "id": "negative_specification_approved_ia_held",
          "kind": "NEGATIVE"
        },
        {
          "actual_pass": false,
          "actual_rule_ids": [
            "FMV-GCF-EDGE-003",
            "FMV-GCF-ORDER-002"
          ],
          "expectation_met": true,
          "expected_pass": false,
          "expected_rule_ids": [
            "FMV-GCF-ORDER-002"
          ],
          "finding_count": 2,
          "id": "negative_plan_before_audit",
          "kind": "NEGATIVE"
        },
        {
          "actual_pass": false,
          "actual_rule_ids": [
            "FMV-GCF-SESSION-THOTH-001"
          ],
          "expectation_met": true,
          "expected_pass": false,
          "expected_rule_ids": [
            "FMV-GCF-SESSION-THOTH-001"
          ],
          "finding_count": 1,
          "id": "negative_different_thoth_session",
          "kind": "NEGATIVE"
        },
        {
          "actual_pass": false,
          "actual_rule_ids": [
            "FMV-GCF-LINEAGE-001"
          ],
          "expectation_met": true,
          "expected_pass": false,
          "expected_rule_ids": [
            "FMV-GCF-LINEAGE-001"
          ],
          "finding_count": 1,
          "id": "negative_caller_supplied_lineage",
          "kind": "NEGATIVE"
        },
        {
          "actual_pass": false,
          "actual_rule_ids": [
            "FMV-GCF-APPROVAL-001"
          ],
          "expectation_met": true,
          "expected_pass": false,
          "expected_rule_ids": [
            "FMV-GCF-APPROVAL-001"
          ],
          "finding_count": 1,
          "id": "negative_approval_binding",
          "kind": "NEGATIVE"
        },
        {
          "actual_pass": false,
          "actual_rule_ids": [
            "FMV-GCF-APPROVAL-002"
          ],
          "expectation_met": true,
          "expected_pass": false,
          "expected_rule_ids": [
            "FMV-GCF-APPROVAL-002"
          ],
          "finding_count": 1,
          "id": "negative_runtime_approval_drift",
          "kind": "NEGATIVE"
        },
        {
          "actual_pass": false,
          "actual_rule_ids": [
            "FMV-GCF-COVERAGE-001"
          ],
          "expectation_met": true,
          "expected_pass": false,
          "expected_rule_ids": [
            "FMV-GCF-COVERAGE-001"
          ],
          "finding_count": 1,
          "id": "negative_partial_activation",
          "kind": "NEGATIVE"
        },
        {
          "actual_pass": false,
          "actual_rule_ids": [
            "FMV-GCF-COVERAGE-002"
          ],
          "expectation_met": true,
          "expected_pass": false,
          "expected_rule_ids": [
            "FMV-GCF-COVERAGE-002"
          ],
          "finding_count": 1,
          "id": "negative_crd_only_operation",
          "kind": "NEGATIVE"
        },
        {
          "actual_pass": false,
          "actual_rule_ids": [
            "FMV-GCF-ROLE-OPS-001"
          ],
          "expectation_met": true,
          "expected_pass": false,
          "expected_rule_ids": [
            "FMV-GCF-ROLE-OPS-001"
          ],
          "finding_count": 1,
          "id": "negative_kronos_ops_execution",
          "kind": "NEGATIVE"
        },
        {
          "actual_pass": false,
          "actual_rule_ids": [
            "FMV-GCF-ROLE-QA-001"
          ],
          "expectation_met": true,
          "expected_pass": false,
          "expected_rule_ids": [
            "FMV-GCF-ROLE-QA-001"
          ],
          "finding_count": 1,
          "id": "negative_kronos_qa_execution",
          "kind": "NEGATIVE"
        },
        {
          "actual_pass": false,
          "actual_rule_ids": [
            "FMV-GCF-QA-REPORT-001"
          ],
          "expectation_met": true,
          "expected_pass": false,
          "expected_rule_ids": [
            "FMV-GCF-QA-REPORT-001"
          ],
          "finding_count": 1,
          "id": "negative_missing_final_qa_report",
          "kind": "NEGATIVE"
        },
        {
          "actual_pass": false,
          "actual_rule_ids": [
            "FMV-GCF-QA-RCA-001"
          ],
          "expectation_met": true,
          "expected_pass": false,
          "expected_rule_ids": [
            "FMV-GCF-QA-RCA-001"
          ],
          "finding_count": 1,
          "id": "negative_missing_final_qa_rca",
          "kind": "NEGATIVE"
        },
        {
          "actual_pass": false,
          "actual_rule_ids": [
            "FMV-GCF-PRODUCER-001"
          ],
          "expectation_met": true,
          "expected_pass": false,
          "expected_rule_ids": [
            "FMV-GCF-PRODUCER-001"
          ],
          "finding_count": 1,
          "id": "negative_duplicate_producer",
          "kind": "NEGATIVE"
        },
        {
          "actual_pass": false,
          "actual_rule_ids": [
            "FMV-GCF-INPUT-001"
          ],
          "expectation_met": true,
          "expected_pass": false,
          "expected_rule_ids": [
            "FMV-GCF-INPUT-001"
          ],
          "finding_count": 1,
          "id": "negative_unproducible_input",
          "kind": "NEGATIVE"
        },
        {
          "actual_pass": false,
          "actual_rule_ids": [
            "FMV-GCF-OUTPUT-001"
          ],
          "expectation_met": true,
          "expected_pass": false,
          "expected_rule_ids": [
            "FMV-GCF-OUTPUT-001"
          ],
          "finding_count": 1,
          "id": "negative_orphan_output",
          "kind": "NEGATIVE"
        },
        {
          "actual_pass": false,
          "actual_rule_ids": [
            "FMV-GCF-EDGE-001"
          ],
          "expectation_met": true,
          "expected_pass": false,
          "expected_rule_ids": [
            "FMV-GCF-EDGE-001"
          ],
          "finding_count": 1,
          "id": "negative_dead_end",
          "kind": "NEGATIVE"
        },
        {
          "actual_pass": false,
          "actual_rule_ids": [
            "FMV-GCF-EDGE-003",
            "FMV-GCF-ORDER-001"
          ],
          "expectation_met": true,
          "expected_pass": false,
          "expected_rule_ids": [
            "FMV-GCF-EDGE-003",
            "FMV-GCF-ORDER-001"
          ],
          "finding_count": 2,
          "id": "negative_bypass_approved_specification_to_plan",
          "kind": "NEGATIVE"
        },
        {
          "actual_pass": false,
          "actual_rule_ids": [
            "FMV-GCF-ACTOR-001"
          ],
          "expectation_met": true,
          "expected_pass": false,
          "expected_rule_ids": [
            "FMV-GCF-ACTOR-001"
          ],
          "finding_count": 1,
          "id": "negative_actor_drift",
          "kind": "NEGATIVE"
        }
      ],
      "schema_version": "change-flow-fixture-report-v1",
      "total": 31
    },
    "oracle_authority": {
      "r1_contract_matrix_library_id": "libfile_9caa654f4a648191bb970b2f32970f22",
      "r1_contract_matrix_sha256": "faa7fb7d77066cc491bde957b6d2f7d3255c74833936e3952f97873da27ea2f1",
      "r1_frozen_snapshot_sha256": "5a6d89ed366f467ee75a5c71d23bf1a613dc79bb4d56791e812e20d53e53db67",
      "r1_source_manifest_library_id": "libfile_e66c0851b3d88191a6d3e39e34e987c6",
      "r1_verdict": "R1_CANONICAL_TRUTH_LOCK_PASS"
    },
    "oracle_profile": "GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260831_1",
    "primary_prerequisite": {
      "errors": [],
      "status": "PASS",
      "warnings": []
    },
    "primary_revision": "1.0.2",
    "primary_sha256": "495c2ca6f33a8b6b837754a518b1cbc64570e9c911e137fd5b81004d487e498c",
    "schema_version": "flowmaster-validation-report-v2",
    "skills": {
      "change-flow": {
        "core_sync": true,
        "errors": [],
        "status": "PASS",
        "warnings": []
      }
    },
    "suite_ok": true,
    "validator_revision": "3.2.3",
    "verdict": "FLOWMASTER_SUITE_PASS",
    "warnings": []
  },
  "source_truth_limit": "The corrected raw Drive bytes were separately pinned and read back in the source manifest. These local validators establish agreement with those pins; they do not retrieve live Drive content."
}
```
