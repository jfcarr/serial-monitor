ARDCMD=arduino-cli
FQBN=arduino:avr:uno
PORT=/dev/ttyACM0
SKETCHNAME=TestSketch
FORMATTER=clang-format -i

default:
	@echo 'Targets:'
	@echo '  compile  -- Compile sketch, but don''t upload it.'
	@echo '  upload   -- Compile and upload sketch.'
	@echo '  edit     -- Edit the source file.'
	@echo '  format   -- Beautify your sketch code.'
	@echo '  reset    -- Use to resolve Device Busy error.'
	@echo '  clean    -- Remove binaries and object files.'

compile:
	$(ARDCMD) compile --fqbn $(FQBN) $(SKETCHNAME)

upload: compile
	$(ARDCMD) upload -p $(PORT) --fqbn $(FQBN) $(SKETCHNAME)

edit:
	gvim $(SKETCHNAME)/$(SKETCHNAME).ino

format:
	$(FORMATTER) $(SKETCHNAME)/$(SKETCHNAME).ino

reset:
	fuser -k $(PORT)

clean:
	-rm -rf $(SKETCHNAME)/build
	-rm -f $(SKETCHNAME)/*.hex
	-rm -f $(SKETCHNAME)/*.elf
