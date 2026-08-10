#!/usr/bin/env bash
# Prove you can still build/run from a cold start (run at phase deloads).
echo "Cold-start check - $(date +%F)"
echo "Do these manually, in order, from a CLEAN state:"
echo " 1. Fresh clone/checkout of the current milestone code"
echo " 2. Rebuild from scratch (no cached objects)"
echo " 3. Flash / run it"
echo " 4. Confirm the last known-good behavior reproduces"
echo ""
echo "If any step fails, that is the real state of your toolchain. Fix it before moving on."
