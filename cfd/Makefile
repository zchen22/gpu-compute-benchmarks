BENCHMARK = cfd

CWD = $(shell pwd)
SRCDIR = src
OBJDIR = obj
BINDIR = bin
DATADIR = $(CWD)/../../benchmarks_data/$(BENCHMARK)

SRC = $(wildcard $(SRCDIR)/*.cu)
LIBSRC = $(wildcard $(SRCDIR)/*.cpp)
OBJ = $(patsubst $(SRCDIR)/%.cu,$(OBJDIR)/%.o,$(SRC))
LIBOBJ = $(patsubst $(SRCDIR)/%.cpp,$(OBJDIR)/%.o,$(LIBSRC))
BIN = $(patsubst $(SRCDIR)/%.cu,$(BINDIR)/%,$(SRC))
DATA = $(DATADIR)/fvcorr.domn.097K
CMD = ./euler3d $(DATA) | tee sim.out
CMD1 = PTX_SIM_MODE_FUNC=1 $(CMD)
CMD2 = $(CMD)

INC = -I$(SRCDIR)
NVFLAGS = -arch sm_20 $(INC)

all: makedir $(BIN)

makedir:
	mkdir -p $(OBJDIR)
	mkdir -p $(BINDIR)

$(BINDIR)/%: $(OBJDIR)/%.o $(OBJDIR)/libcutil.a
	nvcc -o $@ $^

$(OBJDIR)/%.o: $(SRCDIR)/%.cu
	nvcc -o $@ $(NVFLAGS) -c $<

$(OBJDIR)/%.o: $(SRCDIR)/%.cpp
	nvcc -o $@ $(NVFLAGS) -c $<

$(OBJDIR)/libcutil.a: $(LIBOBJ)
	ar rucv $@ $^

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
	rm -fr $(BINDIR) $(OBJDIR)

