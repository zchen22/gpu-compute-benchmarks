BENCHMARK = leukocyte

CWD = $(shell pwd)
SRCDIR = src
OBJDIR = obj
BINDIR = bin
DATADIR = $(CWD)/../../benchmarks_data/$(BENCHMARK)

CUSRC = $(wildcard $(SRCDIR)/*.cu)
CSRC = $(wildcard $(SRCDIR)/*.c)
OBJ = $(patsubst $(SRCDIR)/%.cu,$(OBJDIR)/%.o,$(CUSRC)) \
      $(patsubst $(SRCDIR)/%.c,$(OBJDIR)/%.o,$(CSRC)) \
      $(OBJDIR)/meschach.a
BIN = $(BINDIR)/$(BENCHMARK)
DATA = $(DATADIR)/testfile.avi
CMD = ./$(BENCHMARK) $(DATA) 1 | tee sim.out
CMD1 = PTX_SIM_MODE_FUNC=1 $(CMD)
CMD2 = $(CMD)

INC = -I$(SRCDIR)/meschach_lib
NVFLAGS = -arch sm_20 $(INC)

all: makedir $(BIN)

makedir:
	mkdir -p $(OBJDIR)
	mkdir -p $(BINDIR)

$(BIN): $(OBJ)
	nvcc -o $@ $^

$(OBJDIR)/%.o: $(SRCDIR)/%.cu
	nvcc -o $@ $(NVFLAGS) -c $<

$(OBJDIR)/%.o: $(SRCDIR)/%.c
	nvcc -o $@ $(NVFLAGS) -c $<

$(OBJDIR)/meschach.a: $(SRCDIR)/meschach_lib/meschach.a
	cp $< $(OBJDIR)

$(SRCDIR)/meschach_lib/meschach.a:
	make -C $(SRCDIR)/meschach_lib

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
	cd $(BINDIR); $(CMD1)

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
	make -C $(SRCDIR)/meschach_lib clean
	rm -fr $(SRCDIR)/meschach_lib/meschach.a
	rm -fr $(BINDIR) $(OBJDIR)

