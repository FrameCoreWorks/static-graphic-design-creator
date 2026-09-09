# Installation, updates and personal extensions

Read this reference for Skill maintenance, source-versus-personal differences or an approved extension. Maintenance never starts design production. The user's chosen destination governs: repository work changes repository sources; an installed-Skill task uses the active creator for that same existing Skill. Neither destination silently authorizes editing the other.

## Source identity and actual content

`references/source-release.json` names the upstream base, not the newest similar feature set. A personal extension preserves this record; it cannot claim a release that has not been applied. A verified upstream update replaces the record in the same proposed result as all approved source changes and safe removals. Never advance only the record to conceal unresolved conflicts.

Three Git IDs may legitimately differ: the commit containing the source files, the later commit containing the manifest that hashes those source files, and the host's save commit. Compare file hashes against the declared **source** commit. Do not require these three commits to be identical or use the newest commit indiscriminately in source URLs. A clean Git working tree only means no uncommitted edits; committed personal changes still differ from upstream.

Keep installation evidence in a real host-supported receipt/history outside the canonical upstream files: Skill identity, upstream release, immutable source commit, immutable manifest commit and digest, upstream file digests, actual saved file digests, extra/deleted/modified paths, approved resolutions, save/readback result and rollback reference. Do not include credentials or unrelated private content. A receipt describes observed evidence, never creates proof of an unexecuted save, and must not hash itself. If durable evidence is unavailable, report that limitation and retain the upstream record for baseline resolution.

## Existing-Skill updates

Follow the repository's current `CHATGPT_UPDATE.md` or `CODEX_UPDATE.md` after resolving their discovery commit. The [read-only lifecycle helper](../scripts/skill_lifecycle.py) verifies two retrieved source bundles against their manifests, compares them with the installed files and emits conflict previews. It cannot fetch, install, overwrite, save, publish or grant approval. A host without Python follows the same byte/digest algorithm and reports any verification limitation.

Prepare a complete proposed resolution during the read-only comparison; no separate user approval is needed to inspect files, compute differences or prepare an in-memory merge. For a new upstream path also created locally, the old baseline is **absent**: review both additions, rather than inventing a common ancestor. Distinguish files already equal to the target from actual outstanding differences.

For wording-only provenance differences, propose adopting the target's release wording and explain the exact change. For real personal behavior, propose a reviewed merge or retain it as an explicit local deviation. Do not infer equivalence from a filename, a style count or similar behavior alone. Never silently discard differences because a merge tool reports no conflict. Show all resolved changes, remaining deviations and preserved assets for one approval before saving. If an actual behavior choice cannot be resolved from the brief, ask that specific question with the alternatives already prepared.

An unresolved conflict blocks the **entire update**, including otherwise safe files and the source record. Recheck the installed snapshot and pinned target before the approved save; concurrent changes invalidate the proposal. Verify the complete resulting inventory, bytes, source record, safe deletions and retained local files after the actual host save. A failed or partial save is not `updated`: restore the complete snapshot and verify rollback where supported. A second comparison after a successful update returns `already_up_to_date` for an exact copy or `local_customizations_preserved` for the recorded personalized result.

## Personal extension storage

Use the active creator on the existing Skill only. First inspect the relevant current files and clarify the desired behavior; prepare concrete changes and obtain any required approval before writing. Preserve the installed upstream record. A personal extension is not a source update or a new release.

Prefer `local/SKILL_EXTENSIONS.md` as the entry point for approved personal instructions, with supporting assets/data under `local/`. This namespace is reserved for personal files and excluded from public releases. Create it only when an actual extension is requested; no empty placeholders are installed. Keep the extension self-contained and scoped to the user's requested behavior. Runtime instructions in SKILL.md discover this optional entry after explicit activation. A missing local entry is normal and requires no question or new file.

In that entry, record the feature purpose, approved behavior and relevant local resource paths. Keep change/evaluation evidence in actual host-supported history; if a local extension record is used, treat it as personal data, not a new source manifest. Never copy personal files into a public repository as part of ordinary release preparation.

An extension can require a canonical-file change when the optional entry cannot implement the requested behavior. Explain that reason, capture the previous and new bytes/digests and retain it as a tracked personal override; do not promise conflict-free future updates. Existing extensions embedded in upstream paths are not automatically moved or deleted. During a later approved update, migrate the actual personal behavior to `local/` only when the proposed integration preserves its meaning and avoids duplicate or contradictory execution. Host metadata and icons also remain explicit local differences, not ignored verification exceptions.

Local instructions do not override the current user's explicit brief, factual/reference locks, safety requirements or execution permissions. When a local extension conflicts with a new source contract, report the concrete incompatibility and resolve it before using that part of the workflow. Do not load unrelated personal assets or run local scripts merely because they exist.
