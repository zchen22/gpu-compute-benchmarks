makedir:
	mkdir -p $(OBJDIR)
	mkdir -p $(BINDIR)

$(BIN): $(OBJ)
	nvcc -o $@ $^

$(OBJDIR)/%.o: $(SRCDIR)/%.cu
	nvcc -o $@ $(NVFLAGS) -c $<

$(OBJDIR)/%.o: $(SRCDIR)/%.c
	nvcc -o $@ $(NVFLAGS) -c $<

$(OBJDIR)/%.o: $(SRCDIR)/%.cc
	nvcc -o $@ $(NVFLAGS) -c $<

$(OBJDIR)/%.o: $(SRCDIR)/%.cpp
	nvcc -o $@ $(NVFLAGS) -c $<

run0-func:
	cp ../vanilla.config $(BINDIR)/gpgpusim.config
	cp ../config_fermi_islip.icnt $(BINDIR)
	cp ../gpuwattch_gtx480.xml $(BINDIR)
	cd $(BINDIR); $(CMD1); mv sim.out sim-func.out

run0-timing:
	cp ../vanilla.config $(BINDIR)/gpgpusim.config
	cp ../config_fermi_islip.icnt $(BINDIR)
	cp ../gpuwattch_gtx480.xml $(BINDIR)
	cd $(BINDIR); $(CMD2); mv sim.out sim-timing.out

run1:
	cp ../base.config $(BINDIR)/gpgpusim.config
	cp ../config_fermi_islip.icnt $(BINDIR)
	cp ../gpuwattch_gtx480.xml $(BINDIR)
	cd $(BINDIR); $(CMD1); mv sim.out sim-func.out

run2:
	cp ../base.config $(BINDIR)/gpgpusim.config
	cp ../config_fermi_islip.icnt $(BINDIR)
	cp ../gpuwattch_gtx480.xml $(BINDIR)
	cd $(BINDIR); $(CMD2); mv sim.out sim-base.out
	cp ../sv.config $(BINDIR)/gpgpusim.config
	cp ../config_fermi_islip.icnt $(BINDIR)
	cp ../gpuwattch_gtx480.xml $(BINDIR)
	cd $(BINDIR); $(CMD2); mv sim.out sim-sv.out

clean:
	rm -fr $(BINDIR) $(OBJDIR)

