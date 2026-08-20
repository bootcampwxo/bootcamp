# Image Placeholders for Car Buying Lab

This directory contains placeholder references for images used in the lab guides. Replace these with actual screenshots during lab setup.

## Required Images

### For Student Guide (hands-on-lab-car-buying.md)

1. **orchestrate-home.png**
   - Screenshot of watsonx Orchestrate home page
   - Shows main navigation and interface
   - Recommended size: 1200x800px

2. **skills-list.png**
   - Screenshot showing the Skills page
   - Highlights "Car Buying Assistant" skill
   - Recommended size: 1200x600px

3. **chat-interface.png**
   - Screenshot of empty chat interface
   - Shows where users type messages
   - Recommended size: 1200x800px

4. **search-results-camry.png**
   - Screenshot of search results for Toyota Camry
   - Shows formatted search results with titles, content, and URLs
   - Recommended size: 1000x800px

5. **user-reviews-accord.png**
   - Screenshot of user review search results
   - Shows owner feedback and ratings
   - Recommended size: 1000x800px

6. **search-porsche.png**
   - Screenshot showing results for Porsche 911 (not in catalog)
   - Demonstrates agent's ability to search any car
   - Recommended size: 1000x800px

7. **comparison-camry-accord.png**
   - Screenshot of comparison search results
   - Shows side-by-side information
   - Recommended size: 1200x800px

### For Instructor Guide (DEPLOY_MANUAL.md)

1. **architecture-diagram.png**
   - Visual representation of the system architecture
   - Shows watsonx Orchestrate → LangGraph Agent → Tavily API
   - Can be created using draw.io or similar tool
   - Recommended size: 1400x800px

2. **code-engine-dashboard.png**
   - Screenshot of IBM Cloud Code Engine dashboard
   - Shows deployed application
   - Recommended size: 1200x600px

3. **orchestrate-skill-config.png**
   - Screenshot of skill configuration page
   - Shows A2A protocol settings
   - Recommended size: 1200x800px

4. **api-test-success.png**
   - Screenshot of successful API test
   - Shows curl command and response
   - Recommended size: 1000x400px

5. **monitoring-dashboard.png**
   - Screenshot of Code Engine monitoring
   - Shows metrics and logs
   - Recommended size: 1200x600px

## Image Guidelines

### Screenshot Best Practices
- Use high-resolution displays (Retina/4K preferred)
- Crop to relevant content only
- Highlight important UI elements with red boxes or arrows
- Use consistent browser/window size
- Remove sensitive information (API keys, personal data)

### File Formats
- Use PNG for screenshots (better quality)
- Use JPG for photos (smaller file size)
- Use SVG for diagrams (scalable)

### Naming Convention
- Use lowercase with hyphens
- Be descriptive: `orchestrate-skill-configuration.png`
- Include version if needed: `chat-interface-v2.png`

### Optimization
- Compress images to reduce file size
- Target: < 500KB per image
- Use tools like TinyPNG or ImageOptim

## Creating Placeholder Images

If you need to create temporary placeholders before taking actual screenshots:

```bash
# Using ImageMagick (install via: brew install imagemagick)
convert -size 1200x800 xc:lightgray -pointsize 48 -fill black \
  -gravity center -annotate +0+0 "Orchestrate Home\n(Screenshot Placeholder)" \
  orchestrate-home.png
```

Or use online tools:
- https://placeholder.com/
- https://via.placeholder.com/

Example: `https://via.placeholder.com/1200x800.png?text=Orchestrate+Home`

## Image Attribution

If using images from external sources:
- Ensure you have permission to use them
- Provide attribution if required
- Prefer original screenshots from your own environment

## Updating Images

When updating images:
1. Keep the same filename
2. Maintain similar dimensions
3. Update the date in this README
4. Test that markdown links still work

---

**Last Updated**: 2026-05-11  
**Status**: Placeholders - Awaiting actual screenshots  
**Contact**: Lab administrator for image capture assistance