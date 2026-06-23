# TOOLS.md — Environment Configuration

## Purpose

This file stores environment-specific notes that your AI tools need to know: SSH hosts, device names, API preferences, local paths, and other configuration that varies between setups.

## Important

**This file should stay local and not be committed to version control.** It contains environment-specific information that is different for every team member.

Add `TOOLS.md` to your `.gitignore` to prevent accidental commits.

## Template

| Category | Name | Value / Notes |
|----------|------|---------------|
| SSH Host | [alias] | [host:port, user, key path] |
| Device | [device-name] | [description, IP, location] |
| Local Path | [alias] | [absolute path to project or resource] |
| Tool Config | [tool-name] | [preferences, common flags] |

## Notes

- Each team member maintains their own `TOOLS.md`
- Never commit credentials, tokens, or private keys to this (or any) file
- For shared team configuration, use `workspace-config/` instead
- Reference secrets by name or environment variable, never paste actual values
