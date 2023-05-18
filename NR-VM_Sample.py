# This script uses CairoSVG to show off New Relic Vulnerability Management 
# See (github repo) for details.

import newrelic.agent
import time
import cairosvg
newrelic.agent.initialize('newrelic.ini') #This is required!

@newrelic.agent.background_task(name="NameyMcNameyFace", group='GroupyMcGroupFace')
def execute_task():
    cairosvg.svg2pdf(url='https://dev.w3.org/SVG/tools/svgweb/samples/svg-files/USStates.svg', write_to='image.pdf')

print ("Script has started. Use Ctrl-C to break and end.")
counter = 0
while True:
    counter += 1
    print("Loop counter is "+str(counter))
    execute_task()
    time.sleep(1)
newrelic.agent.shutdown_agent(timeout=100)
